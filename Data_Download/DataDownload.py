import sports, SportClass

def download_data():
    for value in sports.sports_dic:
        sport = SportClass.Sport(value, sports.sports_dic[value])
        sport.set_up_sport()

download_data()