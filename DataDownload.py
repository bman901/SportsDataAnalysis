from Tools.Sports import sportclass, sports
from Tools.FileManager.manager import FileManager

def download_data():

    for value in sports.sports_dic:
        sport = sportclass.Sport(value, sports.sports_dic[value])
        fm = FileManager(sport.get_sport(), sport.get_version())
        fm.set_up_sport()

download_data()