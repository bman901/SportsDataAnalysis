import key, pathlib, requests, json

sports = ['afl']

class Sport(object):
    def __init__(self, sport):
        self.sport = sport
        self.url = "https://v1."+sport+".api-sports.io/status"

        self.payload={}
        self.headers = {
            'x-apisports-key': key.API_key
        }

    def get_status(self):
        response = requests.request("GET", self.url, headers=self.headers, data=self.payload).json()
        print(response)

AFL = Sport('afl')

AFL.get_status()

AFL_folder = 'Data_Download/'+'AFL'

p = pathlib.Path(AFL_folder)

p.mkdir(parents=True, exist_ok=True)

fn = "test.json"

result = AFL.get_status()

filepath = p / fn

with filepath.open("w") as json_file:
    json.dump(result, json_file)
