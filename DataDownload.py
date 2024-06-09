from Tools.Sports import SportClass, sports
from Tools.DataDownload.DownloadClass import DownloadManager
from Tools.SportsData.SportsDataClass import SportsData
from Tools.APICaller.APIClass import APICall

from time import perf_counter

def file_setup():
    for value in sports.versions_dic:
        sport = SportClass.Sport(value, sports.versions_dic[value])
        dm = DownloadManager(sport.get_sport(), sport.get_version())
        dm.set_up_sport()

def download_season_data():
    for value in sports.leagues_dic:
        sport = SportsData(value, sports.versions_dic[value])
        dm = DownloadManager(sport.get_sport(), sport.get_version())
        for id in sports.leagues_dic[value]:
            name = sport.get_league_name(id)
            if sport.get_sport() == "afl":
                for year in sport.get_seasons(id):
                    dm.download_games(name,id,year)
                    # dm.download_odds(name,id,year)
            else:
                for i in range(len(sport.get_seasons(id))):
                    year = sport.get_seasons(id)[i]["season"]
                    dm.download_games(name,id,year)
                    # dm.download_odds(name,id,year)

def download_data():
    t1_start = perf_counter()
    print('Downloading data...')
    # file_setup()
    # print('File Set Up Complete')
    download_season_data()
    print('Season Data Download Complete')
    t2_end = perf_counter()
    time_elapsed = round(t2_end - t1_start,2)
    print('Download complete in '+str(time_elapsed)+' seconds')

# download_data()
    
# TESTING
a = APICall('afl','v1')

url = a.API_URL('odds','game=97')

odds = a.call_API(url)

print(odds)