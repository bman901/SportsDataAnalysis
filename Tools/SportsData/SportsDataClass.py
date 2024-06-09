from Tools.Sports.SportClass import Sport as SportClass
from Tools.APICaller.APIClass import APICall

class SportsData(SportClass):
  def __init__(self, sport, version):
    super().__init__(sport, version)

  def get_leagues(self):
    API = APICall(self.get_sport(), self.get_version())
    url = API.API_URL("leagues")
    leagues = API.call_API(url)
    return(leagues)
  
  def get_seasons(self, id):
    API = APICall(self.get_sport(), self.get_version())
    if self.get_sport() == "afl":
      url = API.API_URL("seasons")
      seasons = API.call_API(url)["response"]
      return(seasons)
    else:
      data = self.get_leagues()
      for value in range(len(data["response"])):
        if self.get_sport == "football":
          if data["response"][value]["league"]["id"] == id:
            seasons = data["response"][value]["league"]["seasons"]
            return(seasons)
        else:
          if data["response"][value]["id"] == id:
            seasons = data["response"][value]["seasons"]
            return(seasons)

  def get_league_name(self, id):
    data = self.get_leagues()
    for value in range(len(data["response"])):
      if self.get_sport == "football":
        if data["response"][value]["league"]["id"] == id:
          return(data["response"][value]["league"]["name"])
      else:
        if data["response"][value]["id"] == id:
          return(data["response"][value]["name"])