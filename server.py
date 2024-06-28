from flask import Flask, render_template, url_for, request, jsonify
from Tools.Sports.sports_dicts import leagues_dict
from data_analysis import *
from Tools.Sports.sport_class import Sport

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
        sport_class = Sport(chosen_sport)
        leagues = sport_class.get_leagues()
        result = get_data(chosen_sport, leagues)

        return jsonify(result)
    return render_template("analysis.html", sports=leagues_dict)


def get_data(chosen_sport, leagues):
    result = {}
    league_list = []
    for data in leagues:
        league_id = data["league_id"]
        current_season = data["current_season"]
        sport = DataAnalysis(chosen_sport, df, league_id, current_season)
        league_name = sport.get_league_name(league_id)
        league_list.append(
            {
                "league_id": league_id,
                "league_name": league_name,
                "current_season": current_season,
                "perc_fav": get_perc_fav(chosen_sport, league_id, current_season),
            }
        )
    result["data"] = league_list

    return result


if __name__ == "__main__":
    app.run(debug=True)
