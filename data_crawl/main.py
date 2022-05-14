from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utils

driver = webdriver.Firefox()

region = "br"
summoner = "joseph joéstar"

url = f"https://{region}.op.gg/summoners/{region}/{summoner}/ingame"
driver.get(url)

blue_team_data = {
    "bluetop": [],
    "bluejungle": [],
    "bluemid": [],
    "blueadc": [],
    "bluesupport": []
}

red_team_data = {
    "redtop": [],
    "redjungle": [],
    "redmid": [],
    "redadc": [],
    "redsupport": []
}

try:
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    
    teams = driver.find_elements(By.TAG_NAME, "table")

    blue_team = teams[0].find_element(By.TAG_NAME, "tbody")
    red_team  = teams[1].find_element(By.TAG_NAME, "tbody")

    blue_team_players = blue_team.find_elements(By.TAG_NAME, "tr")
    red_team_players  = red_team.find_elements(By.TAG_NAME, "tr")

    blue_team_data = utils.parse_team_data(blue_team_players, blue_team_data)
    red_team_data = utils.parse_team_data(red_team_players, red_team_data)

    utils.save_results(blue_team_data, red_team_data)

    driver.close()

except Exception as e:
    print(e)
    driver.quit()



