"""The dictionary of available sports"""

from datetime import datetime

"""Setting up the current seasons"""
year = datetime.today().year  # Current year
lastyear = datetime.today().year - 1  # Previous year
nextyear = datetime.today().year + 1  # Next year
year_next = str(year) + " - " + str(nextyear)  # Current year - Next year
year_last = str(lastyear) + " - " + str(year)  # Previous year - Current year

# For seasons which start midway through the year, this calculates the current season
if datetime.now().month > 6:
    two_years = year_next
    one_year = year
else:
    two_years = year_last
    one_year = lastyear

calendar_year = year

"""Setting up previous seasons"""
# For calendar year seasons
previous_seasons_calendar = []

for i in range(2021, year):  # TEMP to test; change back to 2024 when done
    previous_seasons_calendar.append(i)

# For seasons every 4 years
euros_seasons = []
football_wc_seasons = []
rugby_wc_seasons = []

for i in range(2024, year, 4):
    euros_seasons.append(i)

for i in range(2026, year, 4):
    football_wc_seasons.append(i)

for i in range(2023, year, 4):
    rugby_wc_seasons.append(i)

# For seasons which begin mid-year
one_year_previous = []
two_years_previous = []

if datetime.now().month > 6:
    for i in range(2024, year):
        one_year_previous.append(i - 1)
        two_years_previous.append(str(i - 1) + " - " + str(i))
else:
    for i in range(2024, year):
        one_year_previous.append(i - 1)
        two_years_previous.append(str(i - 1) + " - " + str(i))

"""A list of available sports, API version, current season & previous seasons"""
leagues_dict = [
    {
        "sport": "afl",
        "version": "v1",
        "leagues": [
            {
                "league_id": 1,
                "league_name": "AFL Premiership",
                "current_season": calendar_year,
                "previous_seasons": previous_seasons_calendar,
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
                "previous_seasons": previous_seasons_calendar,
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
                "previous_seasons": two_years_previous,
            },
            {
                "league_id": 12,
                "league_name": "NBA",
                "current_season": two_years,
                "previous_seasons": two_years_previous,
            },
            {
                "league_id": 13,
                "league_name": "NBA W",
                "current_season": calendar_year,
                "previous_seasons": previous_seasons_calendar,
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
                "previous_seasons": euros_seasons,
            },
            {
                "league_id": 1,
                "league_name": "World Cup",
                "current_season": calendar_year,
                "previous_seasons": football_wc_seasons,
            },
            {
                "league_id": 5,
                "league_name": "UEFA Nations League",
                "current_season": one_year,
                "previous_seasons": one_year_previous,
            },
            {
                "league_id": 39,
                "league_name": "Premier League",
                "current_season": one_year,
                "previous_seasons": one_year_previous,
            },
            {
                "league_id": 140,
                "league_name": "La Liga",
                "current_season": one_year,
                "previous_seasons": one_year_previous,
            },
            {
                "league_id": 61,
                "league_name": "Ligue 1",
                "current_season": one_year,
                "previous_seasons": one_year_previous,
            },
            {
                "league_id": 135,
                "league_name": "Serie A",
                "current_season": one_year,
                "previous_seasons": one_year_previous,
            },
            {
                "league_id": 78,
                "league_name": "Bundesliga",
                "current_season": one_year,
                "previous_seasons": one_year_previous,
            },
            {
                "league_id": 188,
                "league_name": "A-League",
                "current_season": one_year,
                "previous_seasons": one_year_previous,
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
                "previous_seasons": one_year_previous,
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
                "previous_seasons": one_year_previous,
            },
            {
                "league_id": 56,
                "league_name": "UK Challenge Cup",
                "current_season": one_year,
                "previous_seasons": one_year_previous,
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
                "previous_seasons": one_year_previous,
            },
            {
                "league_id": 2,
                "league_name": "NCAA",
                "current_season": one_year,
                "previous_seasons": one_year_previous,
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
                "previous_seasons": previous_seasons_calendar,
            },
            {
                "league_id": 85,
                "league_name": "Rugby Championship",
                "current_season": calendar_year,
                "previous_seasons": previous_seasons_calendar,
            },
            {
                "league_id": 71,
                "league_name": "Super Rugby",
                "current_season": calendar_year,
                "previous_seasons": previous_seasons_calendar,
            },
            {
                "league_id": 69,
                "league_name": "World Cup",
                "current_season": calendar_year,
                "previous_seasons": rugby_wc_seasons,
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
                "previous_seasons": one_year_previous,
            },
            {
                "league_id": 97,
                "league_name": "Italy - SuperLega",
                "current_season": one_year,
                "previous_seasons": one_year_previous,
            },
            {
                "league_id": 63,
                "league_name": "France - Ligue A",
                "current_season": one_year,
                "previous_seasons": one_year_previous,
            },
            {
                "league_id": 132,
                "league_name": "Russia - SuperLeague",
                "current_season": one_year,
                "previous_seasons": one_year_previous,
            },
        ],
    },
]
