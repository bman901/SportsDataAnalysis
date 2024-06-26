from flask import Flask, render_template, url_for, request, jsonify
from Tools.Sports.sports_dicts import leagues_dict
from data_analysis import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", sports=leagues_dict)


@app.route("/analysis")
def analysis():
    chosen_sport = request.args.get("btn_sport")
    perc_fav = get_perc_fav(chosen_sport, 1, 2024)
    if request.is_json:
        return perc_fav
    return render_template("analysis.html", sports=leagues_dict)


if __name__ == "__main__":
    app.run(debug=True)
