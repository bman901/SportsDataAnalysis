import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from Tools.DataAnalysis.data_analysis_class import DataAnalysis
from Tools.DataAccess.sports_data_class import SportsData
from Tools.Sports.sports_dicts import leagues_dict


def report_percentage_favourite():
    df = pd.read_csv("sportsdata.csv")
    for data in leagues_dict:
        sport = data["sport"]
        sport_data = SportsData(sport, data["version"])
        for i in data["leagues"]:
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


def plot_percentage_favourite():
    df = pd.read_csv("sportsdata.csv")
    x_axis = []
    y_axis = []
    for data in leagues_dict:
        sport = data["sport"]
        sport_data = SportsData(sport, data["version"])
        for i in data["leagues"]:
            league_id = i["league_id"]
            league_name = i["league_name"]
            season = i["current_season"]
            data_analysis = DataAnalysis(
                sport_data.get_sport(), sport_data.get_version(), df, league_id, season
            )
            percentage = data_analysis.percentage_fav_win()
            if type(percentage) != str:
                x_axis.append(league_name)
                y_axis.append(percentage)
    xpos = np.arange(len(x_axis))
    plt.xticks(xpos, x_axis)
    plt.xlabel("League")
    plt.ylabel("Percentage favourite win")
    plt.title("Percentage favourite wins by league")
    plt.bar(xpos, y_axis)
    plt.show()


def bet_on_fav(bet=10):
    df = pd.read_csv("sportsdata.csv")
    for data in leagues_dict:
        sport = data["sport"]
        sport_data = SportsData(sport, data["version"])
        for i in data["leagues"]:
            league_id = i["league_id"]
            league_name = i["league_name"]
            season = i["current_season"]
            data_analysis = DataAnalysis(
                sport_data.get_sport(), sport_data.get_version(), df, league_id, season
            )
            total_games = data_analysis.count_dataframe_length(df)
            if total_games == 0:
                pass
            else:
                total_bet = bet * total_games
                total_fav_return = bet * data_analysis.get_winning_fav_odds_total(df)
                total_winnings = total_fav_return - total_bet
                if total_winnings < 0:
                    won_lost = "lost"
                else:
                    won_lost = "won"
                print(
                    f"If you'd bet ${bet} on the favourites in every game in the {league_name} you would've {won_lost} ${abs(total_winnings):,.2f}"
                )


bet_on_fav(20)
