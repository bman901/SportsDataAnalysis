import Tools.APICaller.key as key
import requests
from Tools.Sports.sportclass import Sport as Class

from Tools.FileManager import manager

class APICall(Class):
    def __init__(self, sport, version):
        super().__init__(sport,version)
        self.url = "https://"+self.version+"."+self.sport+".api-sports.io"
        self.sport_folder = "Sports_Data/"+str(self.sport).capitalize()
        self.payload={}
        self.headers = {
            'x-apisports-key': key.API_key
        }

    def get_folder(self):
        return(self.sport_folder)

    def call_API(self, url):
        response = requests.request("GET", url, headers=self.headers, data=self.payload).json()
        return(response)
    
    def API_request(self, call, qualifiers=""):
        url = self.url+"/"+call+"?"+qualifiers #Set URL for API
        response = self.call_API(url) #Get data
        return(response)
        
    def get_status(self):
        filemanager = manager.FileManager(self.sport, self.version)
        filemanager.download_data(self.sport_folder,"status")

    def get_leagues(self):
        filemanager = manager.FileManager(self.sport, self.version)
        filemanager.download_data(self.sport_folder,"leagues")
    
    def get_seasons(self):
        filemanager = manager.FileManager(self.sport, self.version)
        if self.sport == "football":
            filemanager.download_data(self.sport_folder,"leagues/seasons")
        else:
            filemanager.download_data(self.sport_folder,"seasons")