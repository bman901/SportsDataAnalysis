""" Functions for running the data analysis on all sports """

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from Tools.DataAnalysis.data_analysis_class import DataAnalysis
from Tools.Sports.sports_dicts import leagues_dict
from Tools.GetRoot import get_root


def get_all_sports(data, leagues):
    """Get all sports"""
    df = pd.read_csv("sportsdata.csv")
    sport = data["sport"]
    league_id = leagues["league_id"]
    season = leagues["current_season"]
    data_analysis = DataAnalysis(sport, df, league_id, season)
    return data_analysis


def report_percentage_favourite_all_seasons(sport, league_id):
    """Report the percentage favourite for a specfic sport"""
    df = pd.read_csv("sportsdata.csv")
    for data in leagues_dict:
        if data["sport"] == sport:
            for league in data["leagues"]:
                if league["league_id"] == league_id:
                    current_season = league["current_season"]
                    data_analysis = DataAnalysis(sport, df, league_id, current_season)
                    data_analysis.report_percentage_favourite()
                    for previous_season in league["previous_seasons"]:
                        prev_season_analysis = DataAnalysis(
                            sport, df, league_id, previous_season
                        )
                        prev_season_analysis.report_percentage_favourite()


def report_percentage_favourite_all_sports_all_time():
    """Report the percentage favourite in each sport"""
    for data in leagues_dict:
        for league in data["leagues"]:
            data_analysis = get_all_sports(data, league)
            report = data_analysis.get_percentage_favourite()
            if report:
                print(report)


def plot_percentage_favourite_all_sports():
    """Use MatPlotLib to plot the favourite win % in each sport"""
    x_axis = []
    y_axis = []
    for data in leagues_dict:
        for league in data["leagues"]:
            data_analysis = get_all_sports(data, league)
            percentage = data_analysis.percentage_fav_win()
            league_name = data_analysis.get_league_name(data_analysis.get_league_id())
            if type(percentage) != str:
                x_axis.append(league_name)
                y_axis.append(percentage)
    xpos = np.arange(len(x_axis))
    plt.xticks(xpos, x_axis)
    plt.xlabel("League")
    plt.ylabel("Percentage favourite win")
    plt.title("Percentage favourite wins by league")
    plt.bar(xpos, y_axis)
    proj_root = get_root.get_project_root()
    plt.savefig(str(proj_root) + "/static/img/fav_plot.png")
    plt.show()
    plt.clf()


def bet_on_fav_all_sports(bet=10):
    """Establish how much you would win or lose if betting on the favourite in each game"""
    for data in leagues_dict:
        for league in data["leagues"]:
            data_analysis = get_all_sports(data, league)
            bet_return = data_analysis.bet_on_fav(bet)
            if bet_return:
                print(bet_return)


# report_percentage_favourite_all_sports_all_time()
# plot_percentage_favourite_all_sports()
# bet_on_fav_all_sports(20)
