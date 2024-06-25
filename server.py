from flask import Flask, render_template, url_for, request
from Tools.Sports.sports_dicts import leagues_dict
from data_analysis import *

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", sports=leagues_dict)


@app.route("/analysis")
def analysis():
    chosen_sport = request.args.get("btn_sport")
    print("Chosen sport", chosen_sport)
    return render_template("analysis.html", sports=leagues_dict)


if __name__ == "__main__":
    app.run(debug=True)
