import os

import time
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
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

# Facebook login
fb_login = driver.find_element(By.XPATH, '//*[@id="s-1866641101"]/div/div/div[1]/div/div[3]/span/div[2]/button')
fb_login.click()

main_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
print(fb_login_window)

driver.switch_to.window(fb_login_window)
print(driver.title)

email = driver.find_element(By.ID, 'email')
password = driver.find_element(By.ID, 'pass')
fb_login_btn = driver.find_element(By.ID, 'loginbutton')
email.send_keys(TINDER_USER)
password.send_keys(TINDER_PASS)
fb_login_btn.click()

#Allow popups
time.sleep(2)

driver.switch_to.window(main_window)
print(driver.title)

allow_btn = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
allow_btn.click()

time.sleep(1)
enable_btn = driver.find_element(By.XPATH, '//*[@id="s-1866641101"]/div/div/div/div/div[3]/button[1]/span')
accept_btn = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div/div[1]/button')

enable_btn.click()
accept_btn.click()

# Swipe
time.sleep(8)

for i in range(100):
    time.sleep(1)

    try:
        like_btn = driver.find_element(By.XPATH, '//*[@id="s-138260025"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span')
        like_btn.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, '.itsAMatch a')
            match_popup.click()

        except NoSuchElementException:
            time.sleep(2)

    except NoSuchElementException:
        time.sleep(1)

