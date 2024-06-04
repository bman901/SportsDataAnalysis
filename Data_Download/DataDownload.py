import key, pathlib, requests, json

sports = {'afl':'v1','basketball':'v1'}

class Sport(object):
    def __init__(self, sport, version):
        self.sport = sport
        self.version = version
        self.url = "https://"+self.version+"."+self.sport+".api-sports.io"
        self.sport_folder = 'Data_Download/'+self.sport
        self.payload={}
        self.headers = {
            'x-apisports-key': key.API_key
        }

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

    def get_status(self):
        url = self.url+"/status" #Set status URL for API
        response = self.call_API(url) #Get status data
        folder = self.sport_folder+"/Status" #Status folder filepath
        self.create_file(self.create_folder(folder), 'Status', response) #Create Status data file
        return(response)

for value in sports:
    sport = Sport(value, sports[value])
    sport.get_status()