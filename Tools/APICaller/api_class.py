""" API Caller """

import requests
from tenacity import retry, wait_random_exponential, stop_after_delay
from Tools.APICaller import key
from Tools.Sports.sport_class import Sport as SportClass


class APICall(SportClass):
    """API Class to call the API"""

    def __init__(self, sport):
        super().__init__(sport)
        self.url = (
            "https://" + self.get_version() + "." + self.get_sport() + ".api-sports.io"
        )
        self.payload = {}
        self.headers = {"x-apisports-key": key.API_key}

    @retry(wait=wait_random_exponential(multiplier=1, max=60) + stop_after_delay(10))
    def call_api(self, url):
        """Calls the API based on the URL provided"""
        s = requests.Session()
        try:
            response = s.request(
                "GET", url, headers=self.headers, data=self.payload
            ).json()
        except:
            print("Rate limit reached, trying again")
        return response

    def api_url(self, call, qualifiers=""):
        """Sets up the URL for the API"""
        url = self.url + "/" + call + "?" + qualifiers  # Set URL for API
        return url
