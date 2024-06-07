import Tools.APICaller.key as key
import requests
from Tools.Sports.SportClass import Sport as SportClass

class APICall(SportClass):
    def __init__(self, sport, version):
        super().__init__(sport,version)
        self.url = "https://"+self.version+"."+self.sport+".api-sports.io"
        self.payload={}
        self.headers = {
            'x-apisports-key': key.API_key
        }

    def call_API(self, url):
        s = requests.Session()
        response = s.request("GET", url, headers=self.headers, data=self.payload).json()
        return(response)
    
    def API_request(self, call, qualifiers=""):
        url = self.url+"/"+call+"?"+qualifiers #Set URL for API
        response = self.call_API(url) #Get data
        return(response)