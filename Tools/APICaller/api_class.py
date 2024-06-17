""" API Caller """

import requests
import time
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
        # count = 0
        # while count < 2:
        response = s.request("GET", url, headers=self.headers, data=self.payload).json()
        # if type(response["errors"]) != dict:
        #     break
        # elif (
        #     response["errors"]["rateLimit"]
        #     == "Too many requests. Your rate limit is 10 requests per minute."
        # ):
        #     print(
        #         "API limit request exceeded, waiting 60 seconds and then trying once more"
        #     )
        #     time.sleep(60)
        #     count += 1
        # else:
        #     print("API call returned an error")
        #     break
        return response

    def api_url(self, call, qualifiers=""):
        """Sets up the URL for the API"""
        url = self.url + "/" + call + "?" + qualifiers  # Set URL for API
        return url
