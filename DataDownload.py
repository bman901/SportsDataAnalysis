from Tools.Sports import SportClass, sports
from Tools.DataDownload.DownloadClass import DownloadManager

from time import perf_counter

def file_setup():
    for value in sports.versions_dic:
        sport = SportClass.Sport(value, sports.versions_dic[value])
        dm = DownloadManager(sport.get_sport(), sport.get_version())
        dm.set_up_sport()

def get_seasons():
    for value in sports.leagues_dic:
        sport = SportClass.Sport(value, sports.versions_dic[value])
        dm = DownloadManager(sport.get_sport(), sport.get_version())
        for value in sports.leagues_dic[value]:
            # name = get_league_name(value)
            # for year in SEASONSLIST
                # dm.download_seasons(name,year)
            dm.download_seasons(value,2021)

def download_data():
    t1_start = perf_counter()
    print('Downloading data...')
    file_setup()
    t2_end = perf_counter()
    time_elapsed = round(t2_end - t1_start,2)
    print('Download complete in '+str(time_elapsed)+' seconds')

# download_data()
    
get_seasons()