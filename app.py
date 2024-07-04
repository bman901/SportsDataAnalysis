from flask import Flask, render_template, url_for, request, jsonify
from Tools.Sports.sports_dicts import leagues_dict
from data_analysis import *
from Tools.Sports.sport_class import Sport
import matplotlib

matplotlib.use("agg")

app = Flask(__name__)

df = pd.read_csv("sportsdata.csv")


@app.route("/")
def home():
    return render_template("home.html", sports=leagues_dict)


@app.route("/analysis")
def analysis():
    if request.is_json:
        chosen_sport = request.args.get("chosen_sport")
        chosen_league = request.args.get("chosen_league")
        chosen_season = request.args.get("chosen_season")
        chosen_bet = request.args.get("chosen_bet")
        if chosen_sport != "all-sports":
            sport_class = Sport(chosen_sport)
            leagues = sport_class.get_leagues()
            result = get_data(chosen_sport, leagues)
            if chosen_season:
                result["analysis"] = get_anaylsis(
                    chosen_sport, chosen_league, chosen_season, chosen_bet
                )
        else:
            result = {}
            result["data"] = report_percentage_favourite_all_sports()
            print(result["data"])
        return jsonify(result)
    return render_template("analysis.html", sports=leagues_dict)


def get_data(chosen_sport, leagues):
    result = {}
    league_list = []
    for data in leagues:
        league_id = data["league_id"]
        current_season = data["current_season"]
        seasons = list(reversed(data["previous_seasons"]))
        seasons.insert(0, current_season)
        sport = DataAnalysis(chosen_sport, df, league_id, current_season)
        league_name = sport.get_league_name(league_id)
        league_list.append(
            {
                "league_id": league_id,
                "league_name": league_name,
                "seasons": seasons,
            }
        )
    result["data"] = league_list

    return result


def get_anaylsis(chosen_sport, chosen_league, chosen_season, chosen_bet):
    analysis_dict = {}
    if "-" not in chosen_season:
        chosen_season = int(chosen_season)
    sport = DataAnalysis(chosen_sport, df, int(chosen_league), chosen_season)
    perc_fav = round(sport.percentage_fav_win(), 4)
    analysis_dict["perc_fav"] = perc_fav
    league_name = sport.get_league_name(int(chosen_league))
    analysis_dict["league_name"] = league_name
    bet_on_fav = sport.report_bet_on_fav(int(chosen_bet))
    analysis_dict["bet_on_fav"] = bet_on_fav
    sport.plot_season()
    return analysis_dict


if __name__ == "__main__":
    app.run(debug=True)
