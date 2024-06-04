import key, pathlib, requests, json, sports

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
    
    def get_version(self):
        return(self.version)

    def set_sport(self, sport):
        self.sport = sport
    
    def set_version(self, version):
        self.version = version

    def create_folder(self, folder):
        path = pathlib.Path(folder) #set folder filepath
        path.mkdir(parents=True, exist_ok=True) #create folder
        return(path)
        
    def create_file(self, path, filename, result):
        fn = filename+".json" #set up json file name
        filepath = path / fn #set file filepath
        with open(filepath, "w", encoding='utf-8') as f:
            json.dump(result, f, ensure_ascii=False, indent=4) #create file

    def call_API(self, url):
        response = requests.request("GET", url, headers=self.headers, data=self.payload).json()
        return(response)
    
    def API_request(self, call):
        url = self.url+"/"+call #Set URL for API
        response = self.call_API(url) #Get data
        folder = self.sport_folder+"/"+str(call).capitalize() #Folder filepath for storage
        self.create_file(self.create_folder(folder), str(call).capitalize(), response) #Create data file within folder

    def get_status(self):
        self.API_request('status')

    def get_leagues(self):
        self.API_request('leagues')
    
    def get_seasons(self):
        self.API_request('seasons')


def download_data():
    for value in sports.sports_dic:
        sport = Sport(value, sports.sports_dic[value])
        sport.get_status()
        sport.get_leagues()
        sport.get_seasons()

download_data()