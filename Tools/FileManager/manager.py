import pathlib, json
from Tools.Sports.sportclass import Sport as Class

from Tools.APICaller import caller

class FileManager(Class):
    def __init__(self, sport, version):
        super().__init__(sport, version)

    def create_folder(self, folder):
        path = pathlib.Path(folder) #set folder filepath
        path.mkdir(parents=True, exist_ok=True) #create folder
        return(path)
        
    def create_file(self, path, filename, result):
        fn = filename+".json" #set up json file name
        filepath = path+"/"+fn #set file filepath
        with open(filepath, "w", encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4) #create file

    def download_data(self, folder, call, qualifiers=""):
        API = caller.APICall(self.sport, self.version)
        response = API.API_request(call, qualifiers)
        if "/" in call:
            self.create_file(folder, str(call).capitalize().rsplit("/", 1)[1], response) #Set the filename to anything beyond the '/' in the call, then create data file
        else:
            self.create_file(folder, str(call).capitalize(), response) #Create data file within folder

    def set_up_sport(self):
        API = caller.APICall(self.sport, self.version)
        getfolder = str(API.get_folder())
        self.create_folder(getfolder)
        API.get_status()
        API.get_leagues()
        API.get_seasons()