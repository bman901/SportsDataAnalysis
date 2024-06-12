""" The 'Sport' class which acts as the parent for other classes """


class Sport:
    """The 'Sport' class which acts as the parent for other classes"""

    def __init__(self, sport, version):
        self.sport = sport
        self.version = version

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
