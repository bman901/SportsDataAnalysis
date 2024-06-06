from Tools.FileManager import manager
from Tools.APICaller import caller

class Sport(object):
    def __init__(self, sport, version):
        self.sport = sport
        self.version = version

    def get_sport(self):
        return(self.sport)

    def set_sport(self, sport):
        self.sport = sport

    def get_version(self):
        return(self.version)

    def set_version(self, version):
        self.version = version

    def set_up_sport(self):
        manager.FileManager.create_folder(caller.APICall.sport_folder)
        caller.APICall.get_status()
        caller.APICall.get_leagues()
        caller.APICall.get_seasons()