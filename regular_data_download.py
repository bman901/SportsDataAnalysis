"""The Python file to download game and odds data each day for two days prior
(two days was chosen because that allows for timezone variance)"""

from datetime import datetime, timedelta

from Tools.Sports import sports_dicts
from Tools.DataAccess.sports_data_class import SportsData


def save_data():
    """
    Works through the leagues specified in the leagues dictionary and downloads games and odds from two days ago
    """
    two_days_ago = datetime.now() - timedelta(2)
    date = datetime.strftime(two_days_ago, "%Y-%m-%d")

    for sport, leagues in sports_dicts.leagues_dict.items():
        sport = SportsData(sport, sports_dicts.versions_dict[sport])
        count = 0
        saved = 0
        for i in leagues:
            league_id = i["league_id"]
            league_name = i["league_name"]
            current_season = i["current_season"]
            games = sport.get_games(league_id, current_season, date)
            for result in range(len(games["response"]) - 1):
                data = sport.get_dataframe_data(
                    games, result, league_id, league_name, current_season
                )
                data_frame = sport.get_dataframe(data)
                saved += sport.save_dataframe(data_frame)
                count += 1

        print(f"Save complete: {count} games found, {saved} downloaded")


save_data()
