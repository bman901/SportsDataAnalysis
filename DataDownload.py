from Tools.Sports import SportClass, sports
from Tools.DataDownload.DownloadClass import DownloadManager

from time import perf_counter

def download_data():
    t1_start = perf_counter()
    print('Downloading data...')
    for value in sports.sports_dic:
        sport = SportClass.Sport(value, sports.sports_dic[value])
        dm = DownloadManager(sport.get_sport(), sport.get_version())
        dm.set_up_sport()
    t2_end = perf_counter()
    time_elapsed = round(t2_end - t1_start,2)
    print('Download complete in '+str(time_elapsed)+' seconds')

download_data()