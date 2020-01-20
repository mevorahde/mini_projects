import random
import sys
import time

nfl_teams = {
    1: 'Arizona Cardinals',
    2: 'Chicago Bears',
    3: 'Green Bay Packers',
    4: 'New York Giants',
    5: 'Detroit Lions',
    6: 'Washington Redskins',
    7: 'Philadelphia Eagles',
    8: 'Pittsburgh Steelers',
    9: 'Los Angeles Rams',
    10: 'San Francisco 49ers',
    11: 'Cleveland Browns',
    12: 'Indianapolis Colts',
    13: 'Dallas Cowboys',
    14: 'Kansas City Chiefs',
    15: 'Los Angeles Chargers',
    16: 'Denver Broncos',
    17: 'New York Jets',
    18: 'New England Patriots',
    19: 'Oakland Raiders',
    20: 'Tennessee Titans',
    21: 'Buffalo Bills',
    22: 'Minnesota Vikings',
    23: 'Atlanta Falcons',
    24: 'Miami Dolphins',
    25: 'New Orleans Saints',
    26: 'Cincinnati Bengals',
    27: 'Seattle Seahawks',
    28: 'Tampa Bay Buccaneers',
    29: 'Carolina Panthers',
    30: 'Jacksonville Jaguars',
    31: 'Baltimore Ravens',
    32: 'Houston Texans'
}


def nfl_fan_generator():
    print("What NFL team most represents you?" + '\n' "Let's find out!" + '\n\n' + "Press any key to begin:")
    key = input()
    user_num = random.randint(1,32)
    for n, team_name in nfl_teams.items():
        if n == user_num:
            print("You are a fan of the: {}!".format(team_name))
            time.sleep(60)
            sys.exit(0)


nfl_fan_generator()
