from flask import Flask, render_template, url_for, request, jsonify
from Tools.Sports.sports_dicts import leagues_dict
from data_analysis import *
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("sportsdata.csv")


@app.route("/")
def home():
    return render_template("home.html", sports=leagues_dict)


@app.route("/analysis")
def analysis():
    if request.is_json:
        chosen_sport = request.args.get("chosen_sport")
        sport = DataAnalysis(chosen_sport, df, 1, 2024)
        league_names = sport.get_league_name(1)
        perc_fav = get_perc_fav(chosen_sport, 1, 2024)
        return jsonify({"perc_fav": perc_fav, "league_names": league_names})
    return render_template("analysis.html", sports=leagues_dict)


if __name__ == "__main__":
    app.run(debug=True)
