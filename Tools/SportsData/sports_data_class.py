""" Set up the Sport Data class which sources the historic sport data from the API """

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
