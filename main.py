# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from collections import defaultdict

players_list = ["Scottie Scheffler", "Justin Thomas", "Mackenzie Hughes,"]


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











# See PyCharm help at https://www.jetbrains.com/help/pycharm/
