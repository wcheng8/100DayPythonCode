import os
import smtplib
import lxml
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv('../.env')

item = 'Joshua-Weissman-Unapologetic-Cookbook'
my_email = 'medemo760@gmail.com'
password = 'AAAaaa111pass'
to_addrs = os.getenv('MY_EMAIL')

ITEM_URL = 'https://www.amazon.com/Joshua-Weissman-Unapologetic-Cookbook/dp/1615649980/ref=sr_1_1?crid=2JYB6N50YHWAA&keywords=cook+book&qid=1640499280&sprefix=cook+boo%2Caps%2C295&sr=8-1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}
req = requests.get(ITEM_URL, headers=headers)

data = req.content

soup = BeautifulSoup(data, 'lxml')
# print(soup.prettify())

price = soup.findAll('span', class_ = 'a-color-base')[3]
price = price.getText()
price_split = price.split("$")
price = float(price_split[1])
print(price)

# Send email
if price < 20:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_addrs,
            msg=f'Subject:Price drop for item {item}. Price: {price}!\n\n Price Drop to {price}! Click here to buy now on amazon! {ITEM_URL}\n\n'
        )