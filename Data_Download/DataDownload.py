import key, pathlib, requests, json

sports = ['afl','basketball'] #Note, there is an identified issue with football being v3; need to update this to a dictionary

class Sport(object):
    def __init__(self, sport):
        self.sport = sport
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

    def get_status(self):
        url = "https://v1."+self.sport+".api-sports.io/status"
        response = requests.request("GET", url, headers=self.headers, data=self.payload).json() #Get status data
        folder = self.sport_folder+'/Status' #Status folder filepath
        self.create_file(self.create_folder(folder), 'Status', response)
        return(response)

for i in sports:
    i = Sport(i)
    i.get_status()