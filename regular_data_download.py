"""The Python file to download game and odds data each day for two days prior
(two days was chosen because that allows for timezone variance)"""

from datetime import datetime, timedelta

import pandas as pd

from Tools.APICaller.api_class import APICall
from Tools.Sports import sport_class, sports_dicts
from Tools.DataAccess.sports_data_class import SportsData


def save_data():
    """
    Works through the leagues specified in the leagues dictionary and downloads yesterday's games and odds
    """
    two_days_ago = datetime.now() - timedelta(2)
    date = "2024-06-08"
    # date = datetime.strftime(two_days_ago, "%Y-%m-%d")
    # current_season = 2024  # Here as a test, will need to change to dynamic

    for sport, leagues in sports_dicts.leagues_dict.items():
        sport = SportsData(sport, sports_dicts.versions_dict[sport])
        # dm = APICall(sport.get_sport(), sport.get_version())
        for i in leagues:
            league_id = i["league_id"]
            name = i["league_name"]
            current_season = i["current_season"]
            data = sport.get_games(league_id, current_season, date)
            for result in range(len(data["response"])):
                if data["response"][result]["status"]["short"] != "FT":
                    pass
                else:
                    game_id = data["response"][result]["game"]["id"]
                    teams = data["response"][result]["teams"]
                    home_team_id = teams["home"]["id"]
                    home_team_name = teams["home"]["name"]
                    away_team_id = teams["away"]["id"]
                    away_team_name = teams["away"]["name"]
                    scores = data["response"][result]["scores"]
                    if scores["home"]["score"] > scores["away"]["score"]:
                        result = "home"

                    d = {
                        "sport": [sport.get_sport()],
                        "game_id": [game_id],
                        "league_id": [league_id],
                        "league_name": [name],
                        "season": [current_season],
                        "home_team_id": [home_team_id],
                        "home_team_name": [home_team_name],
                        "away_team_id": [away_team_id],
                        "away_team_name": [away_team_name],
                        "score": [10],
                    }
                # Remember to put league_id, current season & date into df
                print(game_id)


save_data()
