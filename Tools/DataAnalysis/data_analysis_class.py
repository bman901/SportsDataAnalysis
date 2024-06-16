""" Set up the Sport Analysis class which analyses the data frames passed in """

import pandas as pd


class DataAnalysis:
    """The Data Analysis class which analyses the data"""

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def get_data_frame(self):
        """Returns the data frame"""
        return self.data_frame

    def set_data_frame(self, data_frame):
        """Allows you to set a new data frame"""
        self.data_frame = data_frame

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

    def count_dataframe_length(self, data_frame, sport, league_id, season):
        """Count all equal columns for a specific league and season"""
        df = pd.DataFrame(data=data_frame)
        df_sport = df[df["sport"] == sport]
        df_league = df_sport[df_sport["league_id"] == league_id]
        df_season = df_league[df_league["season"] == season]
        count = len(df_season)
        return count

    def percentage_fav_win(self, sport, league_id, season):
        """Calculate the percentage of favourite wins"""
        df = self.get_data_frame()
        equal = self.compare_equal(df, "result", "favourite")
        favourite_wins = self.count_dataframe_length(equal, sport, league_id, season)
        total_games = self.count_dataframe_length(df, sport, league_id, season)
        percentage = favourite_wins / total_games
        return percentage
