import sports, SportClass

def download_data():
    for value in sports.sports_dic:
        sport = SportClass.Sport(value, sports.sports_dic[value])
        sport.get_status()
        sport.get_leagues()
        sport.get_seasons()

download_data()