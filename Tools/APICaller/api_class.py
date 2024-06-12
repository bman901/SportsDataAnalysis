""" API Caller """

import requests
from Tools.APICaller import key
from Tools.Sports.sport_class import Sport as SportClass


class APICall(SportClass):
    """API Class to call the API"""

    def __init__(self, sport, version):
        super().__init__(sport, version)
        self.url = "https://" + self.version + "." + self.sport + ".api-sports.io"
        self.payload = {}
        self.headers = {"x-apisports-key": key.API_key}

    def call_api(self, url):
        """Calls the API based on the URL provided"""
        s = requests.Session()
        response = s.request("GET", url, headers=self.headers, data=self.payload).json()
        return response

    def api_url(self, call, qualifiers=""):
        """Sets up the URL for the API"""
        url = self.url + "/" + call + "?" + qualifiers  # Set URL for API
        return url
