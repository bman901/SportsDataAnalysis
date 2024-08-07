""" Set up the Sport Data class which sources the sport data from the API """

import statistics
import pandas as pd

from Tools.Sports.sport_class import Sport as SportClass
from Tools.Sports.sports_dicts import leagues_dict
from Tools.APICaller.api_class import APICall


class SportsData(SportClass):
    """The Sports Data class which gets the data for each sport"""

    def get_leagues(self):
        """Gets the leagues data for a particular sport"""
        api = APICall(self.get_sport())
        url = api.api_url("leagues")
        leagues = api.call_api(url)
        return leagues

    def get_seasons(self, league_id):
        """Gets the seasons data for a particular sport"""
        api = APICall(self.get_sport())
        if self.get_sport() == "afl":
            url = api.api_url("seasons")
            data = api.call_api(url)
            seasons = data["response"]
            return seasons
        else:
            data = self.get_leagues()
            for value in range(len(data["response"])):
                if self.get_sport == "football":
                    if data["response"][value]["league"]["id"] == league_id:
                        seasons = data["response"][value]["league"]["seasons"]
                        return seasons
                else:
                    if data["response"][value]["id"] == league_id:
                        seasons = data["response"][value]["seasons"]
                        return seasons

    def get_league_name_by_api(self, league_id):
        """Gets the league name for a particular league via API"""
        data = self.get_leagues()
        for value in range(len(data["response"])):
            if self.get_sport == "football":
                if data["response"][value]["league"]["id"] == league_id:
                    league_name = data["response"][value]["league"]["name"]
                    return league_name
            else:
                if data["response"][value]["id"] == league_id:
                    league_name = data["response"][value]["name"]
                    return league_name

    def get_games(self, league_id, season, date):
        """Gets games from a specific league, season & date"""
        api = APICall(self.get_sport())
        if self.get_sport() != "football":
            url = api.api_url(
                "games",
                f"league={league_id}&season={season}&date={date}",
            )
            games = api.call_api(url)
        else:
            url = api.api_url(
                "fixtures",
                f"league={league_id}&season={season}&date={date}",
            )
            games = api.call_api(url)
        return games

    def get_result(self, games, index):
        if self.get_sport() == "football":
            param = "goals"
        else:
            param = "scores"
        scores = games["response"][index][param]
        if self.get_sport() == "football":
            if scores["home"] > scores["away"]:
                result = "home"
            elif scores["away"] > scores["home"]:
                result = "away"
            else:
                result = "draw"
        else:
            try:
                if scores["home"]["score"] > scores["away"]["score"]:
                    result = "home"
                elif scores["away"]["score"] > scores["home"]["score"]:
                    result = "away"
                else:
                    result = "draw"
            except:
                if scores["home"]["total"] > scores["away"]["total"]:
                    result = "home"
                elif scores["away"]["total"] > scores["home"]["total"]:
                    result = "away"
                else:
                    result = "draw"
        return result

    def get_odds(self, game_id):
        api = APICall(self.get_sport())
        if self.get_sport() == "football":
            url = api.api_url("odds", "fixture=" + str(game_id))
        else:
            url = api.api_url("odds", "game=" + str(game_id))
        odds = api.call_api(url)
        return odds

    def get_mean_home_odds(self, odds):
        home_odds = []
        bookmakers = odds["response"][0]["bookmakers"]
        if self.get_sport() != "football":
            bet = "Home/Away"
        else:
            bet = "Match Winner"
        for i in range(len(bookmakers)):
            bets = bookmakers[i]["bets"]
            for j in range(len(bets)):
                if bets[j]["name"] == bet:
                    for k in range(len(bets[j]["values"])):
                        if bets[j]["values"][k]["value"] == "Home":
                            home = bets[j]["values"][k]["odd"]
                            if type(home) != None:
                                home_odds.append(float(home))
        mean_home_odds = statistics.mean(home_odds)
        return mean_home_odds

    def get_mean_away_odds(self, odds):
        away_odds = []
        bookmakers = odds["response"][0]["bookmakers"]
        if self.get_sport() != "football":
            bet = "Home/Away"
        else:
            bet = "Match Winner"
        for i in range(len(bookmakers)):
            bets = bookmakers[i]["bets"]
            for j in range(len(bets)):
                if bets[j]["name"] == bet:
                    for k in range(len(bets[j]["values"])):
                        if bets[j]["values"][k]["value"] == "Away":
                            away = bets[j]["values"][k]["odd"]
                            if type(away) != None:
                                away_odds.append(float(away))
        mean_away_odds = statistics.mean(away_odds)
        return mean_away_odds

    def get_mean_draw_odds(self, odds):
        draw_odds = []
        bookmakers = odds["response"][0]["bookmakers"]
        if self.get_sport() != "football":
            bet = "Home/Away"
        else:
            bet = "Match Winner"
        for i in range(len(bookmakers)):
            bets = bookmakers[i]["bets"]
            for j in range(len(bets)):
                if bets[j]["name"] == bet:
                    for k in range(len(bets[j]["values"])):
                        if bets[j]["values"][k]["value"] == "Draw":
                            draw = bets[j]["values"][k]["odd"]
                            if type(draw) != None:
                                draw_odds.append(float(draw))
        if draw_odds:
            mean_draw_odds = statistics.mean(draw_odds)
        else:
            mean_draw_odds = 10000
        return mean_draw_odds

    def get_favourite(self, home, away, draw):
        lowest_odds = min(home, away, draw)
        if lowest_odds == home:
            return "home"
        elif lowest_odds == away:
            return "away"
        else:
            return "draw"

    def get_dataframe_data(self, games, index, league_id, league_name, season):
        if (
            self.get_sport() == "football"
            and games["response"][index]["fixture"]["status"]["short"] != "FT"
            or self.get_sport() != "football"
            and games["response"][index]["status"]["short"] != "FT"
        ):
            pass
        else:
            if self.get_sport() == "afl":
                game_id = games["response"][index]["game"]["id"]
                game_date = games["response"][index]["date"]
            elif self.get_sport() == "football":
                game_id = games["response"][index]["fixture"]["id"]
                game_date = games["response"][index]["fixture"]["date"]
            else:
                game_id = games["response"][index]["id"]
                game_date = games["response"][index]["date"]
            odds = self.get_odds(game_id)
            if odds["results"] != 0:
                teams = games["response"][index]["teams"]
                home_team_id = teams["home"]["id"]
                home_team_name = teams["home"]["name"]
                away_team_id = teams["away"]["id"]
                away_team_name = teams["away"]["name"]
                result = self.get_result(games, index)
                odds_home = self.get_mean_home_odds(odds)
                odds_away = self.get_mean_away_odds(odds)
                odds_draw = self.get_mean_draw_odds(odds)
                favourite = self.get_favourite(odds_home, odds_draw, odds_draw)

                data_export = {
                    "sport": [self.get_sport()],
                    "game_id": [game_id],
                    "game_date": [game_date],
                    "league_id": [league_id],
                    "league_name": [league_name],
                    "season": [season],
                    "home_team_id": [home_team_id],
                    "home_team_name": [home_team_name],
                    "away_team_id": [away_team_id],
                    "away_team_name": [away_team_name],
                    "result": [result],
                    "odds_home": [odds_home],
                    "odds_away": [odds_away],
                    "odds_draw": [odds_draw],
                    "favourite": [favourite],
                }

                return data_export

    def fill_in_game_dates(self, games, index):
        """Used to fill in game dates as this wasn't originally part of the downloaded data"""
        df = pd.read_csv("sportsdata.csv")
        # df.insert(2, "game_date", "")
        if self.get_sport() == "afl":
            game_id = games["response"][index]["game"]["id"]
            game_date = games["response"][index]["date"]
        elif self.get_sport() == "football":
            game_id = games["response"][index]["fixture"]["id"]
            game_date = games["response"][index]["fixture"]["date"]
        else:
            game_id = games["response"][index]["id"]
            game_date = games["response"][index]["date"]
        for value in df["game_id"]:
            if value == game_id:
                index = df.loc[(df == value).any(axis=1)].index[0]
                df.loc[index, "game_date"] = game_date
                df.to_csv("sportsdata.csv", index=False)

    def get_dataframe(self, data_input):
        df = pd.DataFrame(data=data_input)
        return df

    def save_dataframe(self, dataframe):
        df = pd.read_csv("sportsdata.csv")
        if not dataframe.empty:
            if dataframe["game_id"][0] not in df.values:
                newdf = pd.concat([df, dataframe], ignore_index=True)
                newdf.to_csv("sportsdata.csv", index=False)
                return 1
            else:
                return 0
        else:
            return 0
