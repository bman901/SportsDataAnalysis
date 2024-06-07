from Tools.Sports import SportClass, sports
from Tools.FileManager.FileClass import FileManager

def download_data():

    for value in sports.sports_dic:
        sport = SportClass.Sport(value, sports.sports_dic[value])
        fm = FileManager(sport.get_sport(), sport.get_version())
        fm.set_up_sport()

download_data()