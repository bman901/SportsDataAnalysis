import key, pathlib, requests, json

class Sport(object):
    def __init__(self, sport, version):
        self.sport = sport
        self.version = version
        self.url = "https://"+self.version+"."+self.sport+".api-sports.io"
        self.sport_folder = "Data_Download/Sports_Data/"+str(self.sport).capitalize()
        self.payload={}
        self.headers = {
            'x-apisports-key': key.API_key
        }

    def get_sport(self):
        return(self.sport)

    def set_sport(self, sport):
        self.sport = sport

    def get_version(self):
        return(self.version)

    def set_version(self, version):
        self.version = version

    def create_folder(self, folder):
        path = pathlib.Path(folder) #set folder filepath
        path.mkdir(parents=True, exist_ok=True) #create folder
        return(path)
        
    def create_file(self, path, filename, result):
        fn = filename+".json" #set up json file name
        filepath = path+"/"+fn #set file filepath
        with open(filepath, "w", encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4) #create file

    def call_API(self, url):
        response = requests.request("GET", url, headers=self.headers, data=self.payload).json()
        return(response)
    
    def API_request(self, call, qualifiers=""):
        url = self.url+"/"+call+"?"+qualifiers #Set URL for API
        response = self.call_API(url) #Get data
        return(response)
        
    def download_data(self, folder, call, qualifiers=""):
        response = self.API_request(call, qualifiers)
        #folder = self.sport_folder+"/"+str(call).capitalize() #Folder filepath for storage
        if "/" in call:
            self.create_file(folder, str(call).capitalize().rsplit("/", 1)[1], response) #Create data file within folder
        else:
            self.create_file(folder, str(call).capitalize(), response)

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
        self.create_folder(self.sport_folder)
        self.get_status()
        self.get_leagues()
        self.get_seasons()