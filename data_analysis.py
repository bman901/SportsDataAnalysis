from Tools.DataAnalysis.data_analysis_class import DataAnalysis
from Tools.DataAccess.sports_data_class import SportsData
from Tools.Sports.sports_dicts import versions_dict

import pandas as pd


def find_percentage_favourite(sport, league_id, season):
    df = pd.read_csv("sportsdata.csv")
    sport_data = SportsData(sport, versions_dict[sport])
    data_analysis = DataAnalysis(
        sport_data.get_sport(), sport_data.get_version(), df, league_id, season
    )
    percentage = data_analysis.percentage_fav_win()
    league_name = sport_data.get_league_name(league_id)
    print(
        f"In the {season} season of {sport}'s {league_name}, the favourite won {percentage:.0%} of the time"
    )


find_percentage_favourite("afl", 1, 2024)
