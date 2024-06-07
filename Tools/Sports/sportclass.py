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