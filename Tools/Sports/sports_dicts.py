from datetime import datetime

year = datetime.today().year
lastyear = datetime.today().year - 1
nextyear = datetime.today().year + 1
year_next = str(year) + " - " + str(nextyear)
year_last = str(lastyear) + " - " + str(year)

if datetime.now().month > 6:
    nbl_current_season = nba_current_season = year_next
    football_current_season = year
else:
    nbl_current_season = nba_current_season = year_last
    football_current_season = lastyear

afl_current_season = mlb_current_season = nbaw_current_season = year

leagues_dict = [
    {
        "sport": "afl",
        "version": "v1",
        "leagues": [
            {
                "league_id": 1,
                "league_name": "AFL Premiership",
                "current_season": afl_current_season,
            }
        ],
    },
    {
        "sport": "baseball",
        "version": "v1",
        "leagues": [
            {
                "league_id": 1,
                "league_name": "MLB",
                "current_season": mlb_current_season,
            }
        ],
    },
    {
        "sport": "basketball",
        "version": "v1",
        "leagues": [
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
    },
    {
        "sport": "football",
        "version": "v3",
        "leagues": [
            {
                "league_id": 4,
                "league_name": "Euros Championship",
                "current_season": 2024,
            },
            {
                "league_id": 39,
                "league_name": "Premier League",
                "current_season": football_current_season,
            },
            {
                "league_id": 140,
                "league_name": "La Liga",
                "current_season": football_current_season,
            },
            {
                "league_id": 61,
                "league_name": "Ligue 1",
                "current_season": football_current_season,
            },
            {
                "league_id": 135,
                "league_name": "Serie A",
                "current_season": football_current_season,
            },
            {
                "league_id": 78,
                "league_name": "Bundesliga",
                "current_season": football_current_season,
            },
            {
                "league_id": 188,
                "league_name": "A-League",
                "current_season": football_current_season,
            },
        ],
    },
]

holding_dict = [
    {
        "sport": "afl",
        "version": "v1",
        "leagues": [
            {
                "league_id": 1,
                "league_name": "AFL Premiership",
                "current_season": afl_current_season,
            }
        ],
    },
    {
        "sport": "baseball",
        "version": "v1",
        "leagues": [
            {
                "league_id": 1,
                "league_name": "MLB",
                "current_season": mlb_current_season,
            }
        ],
    },
    {
        "sport": "basketball",
        "version": "v1",
        "leagues": [
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
    },
]

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
