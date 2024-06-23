"""Download class to download data to files/folders"""

from Tools.Sports.sport_class import Sport as SportClass
from Tools.APICaller.api_class import APICall
from Tools.FileManager.file_class import FileManager


class DownloadManager(SportClass):
    """Download manager class"""

    def __init__(self, sport):
        super().__init__(sport)
        self.sport_folder = "Sports_Data/" + str(self.sport).capitalize()

    def get_folder(self):
        """returns the folder for the sport"""
        return self.sport_folder

    def download_data(self, folder, call, qualifiers=""):
        """Calls the API & downloads the data"""
        api = APICall(self.get_sport())
        fm = FileManager(self.get_sport())
        url = api.api_url(call, qualifiers)
        response = api.call_api(url)
        if "/" in call:
            fm.create_file(
                folder, str(call).capitalize().rsplit("/", 1)[1], response
            )  # Set the filename to anything beyond the '/' in the call, then create data file
        else:
            fm.create_file(
                folder, str(call).capitalize(), response
            )  # Create data file within folder

    def get_status(self):
        """Downloads the current status of the API"""
        self.download_data(self.get_folder(), "status")

    def get_leagues(self):
        """Downloads details of all the leagues available for the sport"""
        self.download_data(self.get_folder(), "leagues")

    def get_seasons(self):
        """Downloads details of all the available seasons for the sport"""
        if self.get_sport() == "football":
            self.download_data(self.get_folder(), "leagues/seasons")
        else:
            self.download_data(self.get_folder(), "seasons")

    def set_up_sport(self):
        """Sets up the sport file with the status of the API
        and details of all leagues & seasons available"""
        fm = FileManager(self.get_sport())
        folder = self.get_folder()
        fm.create_folder(folder)
        self.get_status()
        self.get_leagues()
        self.get_seasons()

    def download_games(self, name, league_id, season):
        """Downloads the game data per season"""
        fm = FileManager(self.get_sport())
        folder = self.get_folder() + "/" + str(name) + "/" + str(season)
        fm.create_folder(folder)
        self.download_data(
            folder, "games", "league=" + str(league_id) + "&season=" + str(season)
        )
        print(f"Games downloaded for {name} - {season}")

    def download_odds(self, name, league_id, season):
        """Downloads the odds data per season"""
        fm = FileManager(self.get_sport())
        folder = self.get_folder() + "/" + str(name) + "/" + str(season)
        fm.create_folder(folder)
        self.download_data(
            folder, "odds", "league=" + str(league_id) + "&season=" + str(season)
        )
        print(f"Odds downloaded for {name} - {season}")
