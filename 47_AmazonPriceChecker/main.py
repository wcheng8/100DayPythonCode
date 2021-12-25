import os
import smtplib
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv('../.env')

my_email = 'medemo760@gmail.com'
password = 'AAAaaa111pass'
to_addrs = os.getenv('MY_EMAIL')
item = 'poo'

# Send email
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=to_addrs,
        msg=f'Subject:Price drop for item {item}!\n\n {message_str}\n\n{motivation}'
    )