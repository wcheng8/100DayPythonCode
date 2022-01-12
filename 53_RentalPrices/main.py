import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

RENT_URL = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.46834792089844%2C%22east%22%3A-122.24244154882813%2C%22south%22%3A37.72724355489126%2C%22north%22%3A37.83171463696806%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

req = requests.get(RENT_URL, headers = headers)
data = req.content
soup = BeautifulSoup(data,'html.parser')
# print(soup.prettify())

price_list = soup.findAll('div', class_ = 'list-card-price')
address_list = soup.findAll('address', class_='list-card-addr')
url_list = soup.findAll('a', class_ = "list-card-link")

address_list = [address.getText() for address in address_list]
price_list = [price.getText() for price in price_list]
url_list = [url['href'] for url in url_list]
# print(address_list)
# print(len(address_list))
# print(price_list)
# print(len(price_list))
# print(url_list)
# print(len(url_list))

# Selenium setup
chrome_driver_path = Service('/Users/wilkinscheng/Desktop/PythonCourse/chromedriver')
driver = webdriver.Chrome(service=chrome_driver_path)

for i in range(len(address_list)):
    driver.get('https://forms.gle/JYiA72fZJ4EMw4cD7')
    time.sleep(3)
    q_address_entry = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q_price_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q_url_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    q_submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    q_address_entry.send_keys(address_list[i])
    q_price_entry.send_keys(price_list[i])
    q_url_entry.send_keys(url_list[2*i])
    q_submit.click()

driver.quit()




