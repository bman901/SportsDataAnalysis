""" Set up the Sport Analysis class which analyses the data frames passed in """

import pandas as pd

from Tools.Sports.sport_class import Sport as SportClass
from Tools.Sports.sports_dicts import leagues_dict


class DataAnalysis(SportClass):
    """The Data Analysis class which analyses the data"""

    def __init__(self, sport, version, data_frame, league_id, season):
        super().__init__(sport, version)
        self.data_frame = data_frame
        self.league_id = league_id
        self.season = season

    def get_data_frame(self):
        """Returns the data frame"""
        return self.data_frame

    def set_data_frame(self, data_frame):
        """Allows you to set a new data frame"""
        self.data_frame = data_frame

    def get_league_id(self):
        """Returns the league_id"""
        return self.league_id

    def set_league_id(self, league_id):
        """Allows you to set a new league_id"""
        self.league_id = league_id

    def get_season(self):
        """Returns the season"""
        return self.season

    def set_season(self, season):
        """Allows you to set a new season"""
        self.season = season

    def group_data(self, column):
        """Groups data by specified column"""
        data_frame = self.get_data_frame()
        df = pd.DataFrame(data=data_frame)
        groupeddf = df.groupby(by=column)
        return groupeddf

    def get_league_name(self, league_id):
        """Gets the league name for a particular league by using the leagues_dict"""
        sport = self.get_sport()
        for data in leagues_dict:
            if data["sport"] == sport:
                for i in data["leagues"]:
                    if i["league_id"] == league_id:
                        return i["league_name"]

    def compare_equal(self, data_frame, column1, column2):
        """Compare two columns to find if they are equal"""
        df = pd.DataFrame(data=data_frame)
        equaldf = df[df[column1] == df[column2]]
        return equaldf

    def count_dataframe_length(self, data_frame):
        """Count all equal columns for a specific league and season"""
        df = pd.DataFrame(data=data_frame)
        sport = self.get_sport()
        league_id = self.get_league_id()
        season = self.get_season()
        df_sport = df[df["sport"] == sport]
        df_league = df_sport[df_sport["league_id"] == league_id]
        df_season = df_league[df_league["season"] == season]
        count = len(df_season)
        return count

    def percentage_fav_win(self):
        """Calculate the percentage of favourite wins"""
        df = self.get_data_frame()
        equal = self.compare_equal(df, "result", "favourite")
        favourite_wins = self.count_dataframe_length(equal)
        total_games = self.count_dataframe_length(df)
        if total_games > 0:
            percentage = favourite_wins / total_games
        else:
            percentage = "No games played"
        return percentage

    def get_winning_fav_odds_total(self, data_frame):
        df = pd.DataFrame(data=data_frame)
        sport = self.get_sport()
        league_id = self.get_league_id()
        season = self.get_season()
        df_sport = df[df["sport"] == sport]
        df_league = df_sport[df_sport["league_id"] == league_id]
        df_season = df_league[df_league["season"] == season]
        df_fav_winners = self.compare_equal(df_season, "result", "favourite")
        df_odds = df_fav_winners[["odds_home", "odds_away", "odds_draw"]]
        df_min_odds = df_odds.min(axis=1)
        sum_min_odds = df_min_odds.sum()
        return sum_min_odds

    def report_percentage_favourite(self):
        percentage = self.percentage_fav_win()
        league_name = self.get_league_name(self.league_id)
        season = self.get_season()
        sport = self.get_sport()
        if type(percentage) != str:
            return f"In the {season} season of {sport}'s {league_name}, the favourite won {percentage:.0%} of the time"
        else:
            pass
