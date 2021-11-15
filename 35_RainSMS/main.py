import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv('../.env')
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
TWILLIO_ACCOUNT_SID = os.getenv('TWILLIO_ACCOUNT_SID')
TWILLIO_AUTH_TOKEN = os.getenv('TWILLIO_AUTH_TOKEN')
NUMBER = os.getenv('NUMBER')
MY_LAT = -33.800770 # Your latitude
MY_LONG = 151.179596 # Your longitude

parameters = {
    'lat' : MY_LAT,
    'lon':  MY_LONG,
    'appid': WEATHER_API_KEY,
    'exclude': 'current,minutely,daily'
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()
will_rain = False

hour_weather_data = weather_data['hourly'][:12]

for hour in hour_weather_data:
    id = hour['weather'][0]['id']
    if id < 700:
        will_rain = True
    # print(id)

if will_rain:
    account_sid = TWILLIO_ACCOUNT_SID
    auth_token = TWILLIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Hello there',
        from_='+12055393232',
        to=NUMBER
    )
    # print(message.sid)