import requests
import os
from twilio.rest import Client
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv('../.env')
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
TWILLIO_ACCOUNT_SID = os.getenv('TWILLIO_ACCOUNT_SID')
TWILLIO_AUTH_TOKEN = os.getenv('TWILLIO_AUTH_TOKEN')
NUMBER = os.getenv('NUMBER')

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': os.getenv('STOCK_API_KEY')
}

response = requests.get('https://www.alphavantage.co/query?', params=params)
data = response.json()
stock_data = data['Time Series (Daily)']
date_now = datetime.now().date()
date_minus1 = date_now - timedelta(1)
date_minus2 = date_now - timedelta(2)
day1 = float(stock_data[f'{date_minus1}']['1. open'])
day2 = float(stock_data[f'{date_minus2}']['1. open'])

percentage = 100*(day1 - day2)/day2
percent_number = (abs(round(percentage,2)))
percent_string = ''
if percentage > 0:
    percent_string = f'🔺{percent_number}%'
else:
    percent_string = f'🔻{percent_number}%'
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
params = {
    'q': COMPANY_NAME,
    'from': date_now,
    'sortBy': 'popularity',
    'apiKey': os.getenv('NEWS_API_KEY')
}
response = requests.get('https://newsapi.org/v2/everything?', params=params)
data = response.json()
news_data = data['articles'][:3]
for news_article in news_data:
    print(news_article['title'])
    print(news_article['description'])
    print('000')


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
if percent_number > 2:
    for news_article in news_data:
        account_sid = TWILLIO_ACCOUNT_SID
        auth_token = TWILLIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f'{STOCK}: {percent_string}\nHeadline: {news_article["title"]}\nBrief: {news_article["description"]}',
            from_='+12055393232',
            to=NUMBER
        )


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

