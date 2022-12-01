
from collections import defaultdict


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def reset_players(plist):
    players = defaultdict(int)
    for i in players_list:
        players[i] = 2500
    print(players)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Welcome to Golf Elo')


    num_players = len(players_list)

    reset_players(players_list)




# Get Leaderboard
# Add all new players and assign base score (2400 for pga, 2300 for kft etc)
# Calculate points gained/lost for each matchup and sum for each player. Adjust player rating.
# Re-sort and publish standings







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
