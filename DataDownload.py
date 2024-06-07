from Tools.Sports import SportClass, sports
from Tools.DataDownload.DownloadClass import DownloadManager

def download_data():

    for value in sports.sports_dic:
        sport = SportClass.Sport(value, sports.sports_dic[value])
        dm = DownloadManager(sport.get_sport(), sport.get_version())
        dm.set_up_sport()

download_data()