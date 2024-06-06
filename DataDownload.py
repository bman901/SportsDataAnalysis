from Tools.Sports import sportclass, sports

def download_data():

    for value in sports.sports_dic:
        sport = sportclass.Sport(value, sports.sports_dic[value])
        sport.set_up_sport()

download_data()