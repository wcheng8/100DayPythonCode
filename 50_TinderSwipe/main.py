import os

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
load_dotenv('../.env')
TINDER_USER = os.getenv('TINDER_USER')
TINDER_PASS = os.getenv('TINDER_PASS')

# Selnium setup
chrome_driver_path = Service('/Users/wilkinscheng/Desktop/PythonCourse/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get('https://tinder.com')

time.sleep(1)

login_btn = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_btn.click()

time.sleep(1)

fb_login = driver.find_element(By.XPATH, '//*[@id="s-1866641101"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

fb_login_window = driver.window_handles[1]
print(fb_login_window)

## Start here cant switch window
driver.switch_to_window(fb_login_window)
print(driver.title)

