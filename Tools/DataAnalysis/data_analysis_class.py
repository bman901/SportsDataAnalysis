""" Set up the Sport Analysis class which analyses the data frames passed in """

import pandas as pd

from Tools.Sports.sport_class import Sport as SportClass


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
        percentage = favourite_wins / total_games
        return percentage
