from selenium.webdriver.common.by import By

import json
import csv
import utils
import re


def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range") 


def parse_team_data(team_players, team_data):
    # blue team parse
    count = 0
    for player in team_players:

        player_data = player.find_elements(By.CLASS_NAME, "champion-info")
        key = utils.get_nth_key(team_data, count)

        if (player_data[0].get_attribute("innerHTML") != "-"):
            wr_games = player_data[0].find_elements(By.TAG_NAME, "div")

            win_ratio = float(wr_games[0].text.rstrip("%"))/100
            games_played = int(re.search("\d+" ,wr_games[1].text).group())
            kda = float(player_data[1].find_element(By.TAG_NAME, "div").text.replace("KDA", ""))

            team_data[key] = [win_ratio, games_played, kda]
        else:
            team_data[key] = [0.5, 0, 1]
        
        count += 1
    
    return team_data


def save_results(blue_team_data, red_team_data):

    data = {}

    for key, value in blue_team_data.items():
        data[f"{key}wr"] = value[0]
        data[f"{key}gp"] = value[1]
        data[f"{key}kda"] = value[2]

    
    for key, value in red_team_data.items():
        data[f"{key}wr"] = value[0]
        data[f"{key}gp"] = value[1]
        data[f"{key}kda"] = value[2]

    with open("match_data.csv", "w") as f:
        writer = csv.DictWriter(f, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)