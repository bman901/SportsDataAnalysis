"""The Python file to download game and odds data each day for the previous day"""

from datetime import datetime, timedelta

import pandas as pd

from Tools.APICaller.api_class import APICall
from Tools.Sports import sport_class, sports
from Tools.SportsData.sports_data_class import SportsData


def save_data():
    """
    Works through the leagues specified in the leagues dictionary and downloads yesterday's games and odds
    """
    yesterday = datetime.now() - timedelta(1)
    date = "2024-06-08"
    # date = datetime.strftime(yesterday, "%Y-%m-%d")
    current_season = 2024  # Here as a test, will need to change to dynamic

    for sport, leagues in sports.leagues_dict.items():
        sport = SportsData(sport, sports.versions_dict[sport])
        dm = APICall(sport.get_sport(), sport.get_version())
        for league_id in leagues:
            name = sport.get_league_name(league_id)
            url = dm.api_url(
                "games",
                f"league={league_id}&season={current_season}&date={date}",
            )
            data = dm.call_api(url)
            for result in range(len(data["response"])):
                game_id = data["response"][result]["game"]["id"]

                # Remember to put league_id, current season & date into df
                print(game_id)


save_data()
