"""The Python file to set up files and download historic data"""

from time import perf_counter

from Tools.Sports import sport_class, sports_dicts
from Archive.HistoricDataDownload.download_class import DownloadManager
from Tools.DataAccess.sports_data_class import SportsData


def file_setup():
    """
    Works through the dictionary in 'sports' to establish which sports to download.
    Then downloads league, seasons and API status data.
    """
    for data in sports_dicts.leagues_dict:
        sport = sport_class.Sport(data["sport"], data["version"])
        dm = DownloadManager(sport.get_sport(), sport.get_version())
        dm.set_up_sport()


def download_season_data():
    """
    Works through the leagues specified in the leagues dictionary and downloads all season data
    """
    for data in sports_dicts.leagues_dict:
        sport = SportsData(data["sport"], data["version"])
        dm = DownloadManager(sport.get_sport(), sport.get_version())
        for i in data["leagues"]:
            league_id = i["league_id"]
            name = sport.get_league_name_by_api(league_id)
            if sport.get_sport() == "afl":
                for year in sport.get_seasons(league_id):
                    dm.download_games(name, league_id, year)
                    # dm.download_odds(name,league_id,year)
            else:
                seasons = sport.get_seasons(league_id)
                for i in range(len(seasons)):
                    year = sport.get_seasons(league_id)[i]["season"]
                    dm.download_games(name, league_id, year)
                    # dm.download_odds(name,league_id,year)


def download_data():
    """
    Sets up files and downloads season data. Also returns the time taken to do so.
    """
    t1_start = perf_counter()
    print("Downloading data...")
    file_setup()
    print("File Set Up Complete")
    download_season_data()
    print("Season Data Download Complete")
    t2_end = perf_counter()
    time_elapsed = round(t2_end - t1_start, 2)
    print(f"Download complete in {time_elapsed} seconds")


download_data()
