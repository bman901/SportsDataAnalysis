""" The 'Sport' class which acts as the parent for other classes """

from Tools.Sports.sports_dicts import leagues_dict


class Sport:
    """The 'Sport' class which acts as the parent for other classes"""

    def __init__(self, sport):
        self.sport = sport
        for data in leagues_dict:
            if self.sport == data["sport"]:
                self.version = data["version"]

    def get_sport(self):
        """Returns the name of the sport"""
        return self.sport

    def set_sport(self, sport):
        """Allows you to change the sport"""
        self.sport = sport

    def get_version(self):
        """Returns the version of the API"""
        return self.version

    def set_version(self, version):
        """Allows you to change the version of the API"""
        self.version = version

    def get_leagues(self):
        for data in leagues_dict:
            if self.get_sport() == data["sport"]:
                return data["leagues"]
