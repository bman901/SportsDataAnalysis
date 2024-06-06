import Tools.APICaller.key as key, requests

from Tools.FileManager import manager

class APICall(object):
    def __init__(self, sport, version):
        self.sport = sport
        self.version = version
        self.url = "https://"+self.version+"."+self.sport+".api-sports.io"
        self.sport_folder = "Data_Download/Sports_Data/"+str(self.sport).capitalize()
        self.payload={}
        self.headers = {
            'x-apisports-key': key.API_key
        }

    def call_API(self, url):
        response = requests.request("GET", url, headers=self.headers, data=self.payload).json()
        return(response)
    
    def API_request(self, call, qualifiers=""):
        url = self.url+"/"+call+"?"+qualifiers #Set URL for API
        response = self.call_API(url) #Get data
        return(response)
        
    def get_status(self):
        manager.FileManager.download_data(self.sport_folder,"status")

    def get_leagues(self):
        manager.FileManager.download_data(self.sport_folder,"leagues")
    
    def get_seasons(self):
        if self.sport == "football":
            manager.FileManager.download_data(self.sport_folder,"leagues/seasons")
        else:
            manager.FileManager.download_data(self.sport_folder,"seasons")