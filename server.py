from flask import Flask, render_template
from Tools.Sports.sports_dicts import leagues_dict

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", sports=leagues_dict)


@app.route("/analysis")
def analysis():
    return render_template("analysis.html")


if __name__ == "__main__":
    app.run(debug=True)
