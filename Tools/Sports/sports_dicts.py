from datetime import datetime, timedelta

versions_dict = {
    "afl": "v1",
    "basketball": "v1",
    "football": "v3",
    "baseball": "v1",
    "formula-1": "v1",
    "handball": "v1",
    "hockey": "v1",
    "mma": "v1",
    "american-football": "v1",
    "rugby": "v1",
    "volleyball": "v1",
}

year = datetime.today().year
lastyear = datetime.today().year - 1
nextyear = datetime.today().year + 1
year_next = str(year) + " - " + str(nextyear)
year_last = str(lastyear) + " - " + str(year)

if datetime.now().month > 6:
    nbl_current_season = year_next
    nba_current_season = year_next
else:
    nbl_current_season = year_last
    nba_current_season = year_last

afl_current_season = year
mlb_current_season = year
nbaw_current_season = year

leagues_dict = {
    "afl": [
        {
            "league_id": 1,
            "league_name": "AFL Premiership",
            "current_season": afl_current_season,
        }
    ],
}

holding_dict = {
    "afl": [
        {
            "league_id": 1,
            "league_name": "AFL Premiership",
            "current_season": afl_current_season,
        }
    ],
    "baseball": [
        {
            "league_id": 1,
            "league_name": "MLB",
            "current_season": mlb_current_season,
        }
    ],
    "basketball": [
        {
            "league_id": 1,
            "league_name": "NBL",
            "current_season": nbl_current_season,
        },
        {
            "league_id": 12,
            "league_name": "NBA",
            "current_season": nba_current_season,
        },
        {
            "league_id": 13,
            "league_name": "NBA W",
            "current_season": nbaw_current_season,
        },
    ],
}
