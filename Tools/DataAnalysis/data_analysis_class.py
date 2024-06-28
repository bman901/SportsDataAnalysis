""" Set up the Sport Analysis class which analyses the data frames passed in """

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from Tools.GetRoot import get_root

from Tools.Sports.sport_class import Sport as SportClass
from Tools.Sports.sports_dicts import leagues_dict


class DataAnalysis(SportClass):
    """The Data Analysis class which analyses the data"""

    def __init__(self, sport, data_frame, league_id, season):
        super().__init__(sport)
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

    def get_season_df(self, data_frame):
        df = pd.DataFrame(data=data_frame)
        sport = self.get_sport()
        league_id = self.get_league_id()
        season = self.get_season()
        df_sport = df[df["sport"] == sport]
        df_league = df_sport[df_sport["league_id"] == league_id]
        df_season = df_league[df_league["season"] == season]
        return df_season

    def count_specific_dataframe_length(self, data_frame):
        """Count all columns for a specific league and season"""
        df_season = self.get_season_df(data_frame)
        count = len(df_season)
        return count

    def count_self_dataframe_length(self):
        """Count all columns for a specific league and season"""
        df_season = self.get_season_df(self.get_data_frame())
        count = len(df_season)
        return count

    def percentage_fav_win(self):
        """Calculate the percentage of favourite wins"""
        df = self.get_data_frame()
        equal = self.compare_equal(df, "result", "favourite")
        favourite_wins = self.count_specific_dataframe_length(equal)
        total_games = self.count_specific_dataframe_length(df)
        if total_games > 0:
            percentage = favourite_wins / total_games
        else:
            percentage = "No games played"
        return percentage

    def get_winning_fav_odds_total(self):
        """Get the sum of the odds on each favourite within a sport & league"""
        df_season = self.get_season_df(self.get_data_frame())
        df_fav_winners = self.compare_equal(df_season, "result", "favourite")
        df_odds = df_fav_winners[["odds_home", "odds_away", "odds_draw"]]
        df_min_odds = df_odds.min(axis=1)
        sum_min_odds = df_min_odds.sum()
        return sum_min_odds

    def get_percentage_favourite(self):
        """Report the % wins for the favourite within a sport & league"""
        percentage = self.percentage_fav_win()
        # Probably move the below into 'report percentage'
        league_name = self.get_league_name(self.league_id)
        season = self.get_season()
        sport = self.get_sport()
        if type(percentage) != str:
            return f"In the {season} season of {sport}'s {league_name}, the favourite won {percentage:.0%} of the time"
        else:
            pass

    def report_percentage_favourite(self):
        report = self.get_percentage_favourite()
        if report:
            print(report)
        else:
            print("No data for the chosen season")

    def get_bet_on_fav(self, bet):
        """Report the winnings if you'd bet on the favourite every game within a sport & league"""
        total_games = self.count_self_dataframe_length()
        if total_games == 0:
            pass
        else:
            total_bet = bet * total_games
            total_fav_return = bet * self.get_winning_fav_odds_total()
            total_winnings = total_fav_return - total_bet
            return total_winnings

    def report_bet_on_fav(self, bet):
        total_winnings = self.get_bet_on_fav(bet)
        league_name = self.get_league_name(self.get_league_id())
        if total_winnings:
            if total_winnings < 0:
                won_lost = "lost"
            else:
                won_lost = "won"
            return f"If you'd bet ${bet} on the favourites in every game in the {league_name} you would've {won_lost} ${abs(total_winnings):,.2f}"

    def plot_season(self):
        """Use MatPlotLib to plot the favourite win % in a given season for a league within a sport"""
        x_axis = []
        y_axis = []
        league_name = self.get_league_name(self.get_league_id())
        season = self.get_season()
        percentage = self.percentage_fav_win()
        if type(percentage) != str:
            x_axis.append(season)
            y_axis.append(percentage)
        xpos = np.arange(len(x_axis))
        plt.xticks(xpos, x_axis)
        plt.ylabel("Percentage favourite win")
        plt.title(f"Percentage favourite wins in the {league_name}")
        plt.bar(xpos, y_axis)
        proj_root = get_root.get_project_root()
        plt.savefig(str(proj_root) + "/static/img/fav_plot.png")
        plt.clf()
