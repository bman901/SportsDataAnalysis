from Tools.Sports import SportClass, sports
from Tools.DataDownload.DownloadClass import DownloadManager
from Tools.SportsData.SportsDataClass import SportsData

from time import perf_counter

def file_setup():
    for value in sports.versions_dic:
        sport = SportClass.Sport(value, sports.versions_dic[value])
        dm = DownloadManager(sport.get_sport(), sport.get_version())
        dm.set_up_sport()

def download_seasons():
    for value in sports.leagues_dic:
        sport = SportsData(value, sports.versions_dic[value])
        dm = DownloadManager(sport.get_sport(), sport.get_version())
        for id in sports.leagues_dic[value]:
            name = sport.get_league_name(id)
            for year in sport.get_seasons()["response"]:
                dm.download_seasons(name,id,year)

def download_data():
    t1_start = perf_counter()
    print('Downloading data...')
    file_setup()
    download_seasons()
    t2_end = perf_counter()
    time_elapsed = round(t2_end - t1_start,2)
    print('Download complete in '+str(time_elapsed)+' seconds')

download_data()