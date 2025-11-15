import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import oauth,scope_token,client_id


BROADCASTER_ID = ""                      # ID of the channel where the clip will be shown
NEW_TITLE = ""                     # the name for the clip
SELENIUM_GRID_URL = ""  # URL Selenium Grid
auth_cookies={[
    
    {
        "domain": ".twitch.tv",
        "expirationDate": 1797260632,
        "hostOnly": false,
        "httpOnly": false,
        "name": "auth-token",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": oauth
    },


    {
        "domain": ".twitch.tv",
        "expirationDate": 1797260632,
        "hostOnly": false,
        "httpOnly": false,
        "name": "twilight-user",
        "path": "/",
        "sameSite": "no_restriction",
        "secure": true,
        "session": false,
        "storeId": null,
        "value": "{%22authToken%22:%22"+oauth+"%22displayName%22:%22%sample_nick22%2C%22id%22:%221333738697%22%2C%22login%22:%22sample_nick22%22%2C%22roles%22:{%22isStaff%22:false}%2C%22version%22:2}"
    }]
    }

def create_clip(broadcaster_id):
    url = "https://api.twitch.tv/helix/clips"
    headers = {
        "Authorization": f"Bearer {scope_token}",
        "Client-Id": client_id
    }
    params = {"broadcaster_id": broadcaster_id}
    response = requests.post(url, headers=headers, params=params)
    if response.status_code == 202:
        data = response.json()
        clip_id = data["data"][0]["id"]
        edit_url = data["data"][0]["edit_url"]
        print(f"The clip was created successfully! clip_id: {clip_id}")
        print(f"edit_url: {edit_url}")
        return edit_url
    else:
        print(f"Clip creation error: {response.status_code}")
        print(response.text)
        return None


def edit_clip_title(edit_url, new_title):
    global auth_cookies
    cookies = json.load(auth_cookies)
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-infobars")
    options.add_argument("--no-sandbox")
    driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, options=options)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": open("stealth.min.js").read()
})
    driver.get("https://www.twitch.tv/")
    time.sleep(3)
    for cookie in cookies:
        cookie.pop("sameSite", None)
        cookie.pop("storeId", None)
        cookie.pop("hostOnly", None)
        if "expirationDate" in cookie:
            cookie["expires"] = int(cookie["expirationDate"])
            cookie.pop("expirationDate", None)
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print("Cookie error:", cookie["name"], e)
    driver.refresh()
    time.sleep(3)
    driver.get(edit_url)
    time.sleep(5)
    title_input = driver.find_element(By.ID, "cmgr-title-input")
    title_input.clear()
    title_input.send_keys(new_title)
    save_btn = driver.find_element(By.XPATH, "//button[.//div[text()='Save Clip']]")
    driver.execute_script("arguments[0].scrollIntoView(true);", save_btn)
    time.sleep(0.5)
    driver.execute_script("arguments[0].click();", save_btn)
    time.sleep(3)
    driver.quit()
    print("The name of the clip has been updated!")


if __name__ == "__main__":
    edit_url = create_clip(BROADCASTER_ID)
    if edit_url:
        print("We wait 10 seconds for the clip to appear in the database....")
        time.sleep(10)
        edit_clip_title(edit_url, NEW_TITLE)
