from Tools.DataAnalysis.data_analysis_class import DataAnalysis
from Tools.DataAccess.sports_data_class import SportsData
from Tools.Sports import sports_dicts

import pandas as pd


def find_percentage_favourite():
    df = pd.read_csv("sportsdata.csv")
    for sport, leagues in sports_dicts.leagues_dict.items():
        sport_data = SportsData(sport, sports_dicts.versions_dict[sport])
        for i in leagues:
            league_id = i["league_id"]
            league_name = i["league_name"]
            season = i["current_season"]
            data_analysis = DataAnalysis(
                sport_data.get_sport(), sport_data.get_version(), df, league_id, season
            )
            percentage = data_analysis.percentage_fav_win()
            if type(percentage) != str:
                print(
                    f"In the {season} season of {sport}'s {league_name}, the favourite won {percentage:.0%} of the time"
                )
            else:
                print(f"{sport}'s {league_name} season is yet to start")


find_percentage_favourite()
