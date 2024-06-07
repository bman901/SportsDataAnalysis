import pathlib, json
from Tools.Sports.SportClass import Sport as SportClass

from Tools.APICaller import APIClass

class FileManager(SportClass):
    def __init__(self, sport, version):
        super().__init__(sport, version)
        self.sport_folder = "Sports_Data/"+str(self.sport).capitalize()

    def create_folder(self, folder):
        path = pathlib.Path(folder) #set folder filepath
        path.mkdir(parents=True, exist_ok=True) #create folder
        return(path)

    def get_folder(self):
        return(self.sport_folder)

    def create_file(self, path, filename, result):
        fn = filename+".json" #set up json file name
        filepath = path+"/"+fn #set file filepath
        with open(filepath, "w", encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4) #create file

    def download_data(self, folder, call, qualifiers=""):
        API = APIClass.APICall(self.sport, self.version)
        response = API.API_request(call, qualifiers)
        if "/" in call:
            self.create_file(folder, str(call).capitalize().rsplit("/", 1)[1], response) #Set the filename to anything beyond the '/' in the call, then create data file
        else:
            self.create_file(folder, str(call).capitalize(), response) #Create data file within folder

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
        self.create_folder(self.get_folder())
        self.get_status()
        self.get_leagues()
        self.get_seasons()