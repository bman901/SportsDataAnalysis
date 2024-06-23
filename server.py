from flask import Flask, render_template
from Tools.Sports.sports_dicts import leagues_dict

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", sports=leagues_dict)


for data in leagues_dict:
    sport = data["sport"]

    @app.route("/<sport>", endpoint=sport)
    def create_page(sport):
        return render_template(sport + ".html")


if __name__ == "__main__":
    app.run(debug=True)
