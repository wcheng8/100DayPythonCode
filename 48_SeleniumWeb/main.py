import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

# Selenium setup
chrome_driver_path = Service('/Users/wilkinscheng/Desktop/PythonCourse/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)
driver.get('http://orteil.dashnet.org/experiments/cookie/')

# Get cookie
cookie = driver.find_element(By.ID, 'cookie')

# Get store upgrade ids
store = driver.find_elements(By.CSS_SELECTOR, '#store div')
item_ids = [item.get_attribute("id") for item in store]

print(item_ids)

five_min = time.time() + 60*5

while True:
    cookie.click()

    # Get price tags of the store and convert to integer price
    store_price = driver.find_elements(By.CSS_SELECTOR, '#store div b')
    store_prices = [int(store_price.text.split('-')[1][1:].replace(',','')) for store_price in store_price if store_price.text != '']

    # Create list of cookie upgrades and prices dictionary
    cookie_upg_dict = {}
    for x in range(len(store_prices)):
        cookie_upg_dict[item_ids[x]] = store_prices[x]

    print(cookie_upg_dict)

    # Get money count (cookie)
    money = driver.find_element(By.ID, 'money').text
    if ',' in money:
        money = int(money.replace(',',''))
    else:
        money = int(money)
    print(money)
    # Find upgrades that you are able to afford
    afford_upg = []
    for price in store_prices:
        if money >= price:
            afford_upg.append(price)
            break

    print(afford_upg)

    # Check if array is not empty
    if len(afford_upg) != 0:
        most_exp_upg_price = max(afford_upg)
        print(most_exp_upg_price)

        most_exp_upg = ''
        for upgrade in cookie_upg_dict:
            if cookie_upg_dict[upgrade] == most_exp_upg_price:
                most_exp_upg = upgrade
                break

        print(most_exp_upg)
        # Select most expensive affordable upgrade and click
        driver.find_element(By.ID, most_exp_upg).click()
        print(f'Upgrade {most_exp_upg} bought!')
    else:
        print('Array is empty. No upgrades available.')

    # Stop bot in five minutes and check
    if time.time() >= five_min:
        cps = driver.find_element(By.ID,'cps')
        print(f'5 min is up. Your {cps.text}')
        break

    sleep(0.25)


driver.quit()
