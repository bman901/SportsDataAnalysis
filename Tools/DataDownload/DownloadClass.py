from Tools.Sports.SportClass import Sport as SportClass
from Tools.APICaller import APIClass
from Tools.FileManager.FileClass import FileManager

class DownloadManager(SportClass):
    def __init__(self, sport, version):
      super().__init__(sport, version)
      self.sport_folder = "Sports_Data/"+str(self.sport).capitalize()
    
    def get_folder(self):
        return(self.sport_folder)

    def download_data(self, folder, call, qualifiers=""):
        API = APIClass.APICall(self.get_sport(), self.get_version())
        fm = FileManager(self.sport, self.version)
        response = API.API_request(call, qualifiers)
        if "/" in call:
            fm.create_file(folder, str(call).capitalize().rsplit("/", 1)[1], response) #Set the filename to anything beyond the '/' in the call, then create data file
        else:
            fm.create_file(folder, str(call).capitalize(), response) #Create data file within folder

    def get_status(self):
        self.download_data(self.sport_folder,"status")

    def get_leagues(self):
        self.download_data(self.sport_folder,"leagues")
    
    def get_seasons(self):
        if self.sport == "football":
            self.download_data(self.sport_folder,"leagues/seasons")
        else:
            self.download_data(self.sport_folder,"seasons")

    def set_up_sport(self):
        fm = FileManager(self.sport, self.version)
        folder = self.get_folder()
        fm.create_folder(folder)
        self.get_status()
        self.get_leagues()
        self.get_seasons()