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
        API = caller.APICall(self.sport, self.version)
        foldermaker = manager.FileManager(self.sport, self.version)
        getfolder = str(API.get_folder)
        foldermaker.create_folder(getfolder)
        API.get_status()
        API.get_leagues()
        API.get_seasons()