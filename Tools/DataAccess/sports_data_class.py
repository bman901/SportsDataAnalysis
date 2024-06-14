""" Set up the Sport Data class which sources the sport data from the API """

from Tools.Sports.sport_class import Sport as SportClass
from Tools.APICaller.api_class import APICall


class SportsData(SportClass):
    """The Sports Data class which gets the data for each sport"""

    def get_leagues(self):
        """Gets the leagues data for a particular sport"""
        api = APICall(self.get_sport(), self.get_version())
        url = api.api_url("leagues")
        leagues = api.call_api(url)
        return leagues

    def get_seasons(self, league_id):
        """Gets the seasons data for a particular sport"""
        api = APICall(self.get_sport(), self.get_version())
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

    def get_league_name(self, league_id):
        """Gets the league name for a particular league"""
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
        api = APICall(self.get_sport(), self.get_version())
        url = api.api_url(
            "games",
            f"league={league_id}&season={season}&date={date}",
        )
        games = api.call_api(url)
        return games

    def get_dataframe_data(self, games, index):
        if games["response"][index]["status"]["short"] != "FT":
            pass
        else:
            game_id = games["response"][index]["game"]["id"]
            teams = games["response"][index]["teams"]
            home_team_id = teams["home"]["id"]
            home_team_name = teams["home"]["name"]
            away_team_id = teams["away"]["id"]
            away_team_name = teams["away"]["name"]
            result = self.get_result(games, index)

    def get_result(self, games, index):
        scores = games["response"][index]["scores"]
        if scores["home"]["score"] > scores["away"]["score"]:
            result = "home"
        elif scores["away"]["score"] > scores["home"]["score"]:
            result = "away"
        else:
            result = "draw"
        return result

    def set_up_dataframe(
        self,
        game_id,
        league_id,
        league_name,
        season,
        home_team_id,
        home_team_name,
        away_team_id,
        away_team_name,
    ):
        d = {
            "sport": [self.get_sport()],
            "game_id": [game_id],
            "league_id": [league_id],
            "league_name": [league_name],
            "season": [season],
            "home_team_id": [home_team_id],
            "home_team_name": [home_team_name],
            "away_team_id": [away_team_id],
            "away_team_name": [away_team_name],
            "score": [10],
        }
