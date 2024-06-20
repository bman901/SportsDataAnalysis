from datetime import datetime

year = datetime.today().year
lastyear = datetime.today().year - 1
nextyear = datetime.today().year + 1
year_next = str(year) + " - " + str(nextyear)
year_last = str(lastyear) + " - " + str(year)

if datetime.now().month > 6:
    two_years = year_next
    one_year = year
else:
    two_years = year_last
    one_year = lastyear

calendar_year = year

leagues_dict = [
    {
        "sport": "afl",
        "version": "v1",
        "leagues": [
            {
                "league_id": 1,
                "league_name": "AFL Premiership",
                "current_season": calendar_year,
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
                "current_season": calendar_year,
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
                "current_season": two_years,
            },
            {
                "league_id": 12,
                "league_name": "NBA",
                "current_season": two_years,
            },
            {
                "league_id": 13,
                "league_name": "NBA W",
                "current_season": calendar_year,
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
                "current_season": calendar_year,
            },
            {
                "league_id": 1,
                "league_name": "World Cup",
                "current_season": calendar_year,
            },
            {
                "league_id": 5,
                "league_name": "UEFA Nations League",
                "current_season": one_year,
            },
            {
                "league_id": 39,
                "league_name": "Premier League",
                "current_season": one_year,
            },
            {
                "league_id": 140,
                "league_name": "La Liga",
                "current_season": one_year,
            },
            {
                "league_id": 61,
                "league_name": "Ligue 1",
                "current_season": one_year,
            },
            {
                "league_id": 135,
                "league_name": "Serie A",
                "current_season": one_year,
            },
            {
                "league_id": 78,
                "league_name": "Bundesliga",
                "current_season": one_year,
            },
            {
                "league_id": 188,
                "league_name": "A-League",
                "current_season": one_year,
            },
        ],
    },
    {
        "sport": "handball",
        "version": "v1",
        "leagues": [
            {
                "league_id": 131,
                "league_name": "Champions League",
                "current_season": one_year,
            },
        ],
    },
    {
        "sport": "hockey",
        "version": "v1",
        "leagues": [
            {
                "league_id": 31,
                "league_name": "NHL",
                "current_season": one_year,
            },
            {
                "league_id": 56,
                "league_name": "UK Challenge Cup",
                "current_season": one_year,
            },
        ],
    },
    {
        "sport": "american-football",
        "version": "v1",
        "leagues": [
            {
                "league_id": 1,
                "league_name": "NFL",
                "current_season": one_year,
            },
            {
                "league_id": 2,
                "league_name": "NCAA",
                "current_season": one_year,
            },
        ],
    },
    {
        "sport": "rugby",
        "version": "v1",
        "leagues": [
            {
                "league_id": 25,
                "league_name": "Six Nations",
                "current_season": calendar_year,
            },
            {
                "league_id": 85,
                "league_name": "Rugby Championship",
                "current_season": calendar_year,
            },
            {
                "league_id": 71,
                "league_name": "Super Rugby",
                "current_season": calendar_year,
            },
            {
                "league_id": 69,
                "league_name": "World Cup",
                "current_season": calendar_year,
            },
        ],
    },
    {
        "sport": "volleyball",
        "version": "v1",
        "leagues": [
            {
                "league_id": 118,
                "league_name": "Poland - I. Liga",
                "current_season": one_year,
            },
            {
                "league_id": 97,
                "league_name": "Italy - SuperLega",
                "current_season": one_year,
            },
            {
                "league_id": 63,
                "league_name": "France - Ligue A",
                "current_season": one_year,
            },
            {
                "league_id": 132,
                "league_name": "Russia - SuperLeague",
                "current_season": one_year,
            },
        ],
    },
]
