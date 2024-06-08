from Tools.Sports.SportClass import Sport as SportClass
from Tools.APICaller import APIClass
from Tools.FileManager.FileClass import FileManager

class DownloadManager(SportClass):
    def __init__(self, sport, version):
      super().__init__(sport, version)
      self.sport_folder = "Sports_Data/"+str(self.sport).capitalize()
    
    def get_folder(self):
        # returns the folder for the sport
        return(self.sport_folder)

    def download_data(self, folder, call, qualifiers=""):
        # Calls the API & downloads the data
        API = APIClass.APICall(self.get_sport(), self.get_version())
        fm = FileManager(self.get_sport(), self.get_version())
        url = API.API_URL(call, qualifiers)
        response = API.call_API(url)
        if "/" in call:
            fm.create_file(folder, str(call).capitalize().rsplit("/", 1)[1], response) #Set the filename to anything beyond the '/' in the call, then create data file
        else:
            fm.create_file(folder, str(call).capitalize(), response) #Create data file within folder

    def get_status(self):
        # Downloads the current status of the API
        self.download_data(self.get_folder(),"status")

    def get_leagues(self):
        # Downloads details of all the leagues available for the sport
        self.download_data(self.get_folder(),"leagues")
    
    def get_seasons(self):
        # Downloads details of all the available seasons for the sport
        if self.get_sport() == "football":
            self.download_data(self.get_folder(),"leagues/seasons")
        else:
            self.download_data(self.get_folder(),"seasons")

    def set_up_sport(self):
        # Sets up the sport file with the status of the API and details of all leagues & seasons available
        fm = FileManager(self.get_sport(), self.get_version())
        folder = self.get_folder()
        fm.create_folder(folder)
        self.get_status()
        self.get_leagues()
        self.get_seasons()

    def download_seasons(self, name, id, season):
        # Downloads the game data per season
        fm = FileManager(self.get_sport(), self.get_version())
        folder = self.get_folder()+"/"+str(name)+"/"+str(season)
        fm.create_folder(folder)
        self.download_data(folder, "games", "league="+str(id)+"&season="+str(season))