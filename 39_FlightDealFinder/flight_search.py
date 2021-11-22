import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
load_dotenv('../.env')

FLIGHT_API = os.getenv('FLIGHTTEQ_API_KEY')

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self,flight_to):
        today = datetime.now()
        future_day = today + timedelta(days=183)
        self.params = {
            'fly_from': 'HK',
            'fly_to': flight_to,
            'dateFrom': today.strftime("%d/%m/%Y"),
            'dateTo': future_day.strftime("%d/%m/%Y"),
            'price_to': 500,
            # Buggy currency
            # 'curr': 'USD'
        }
        self.headers = FLIGHT_API

    def search(self):
        search_req = requests.get(
            url='https://tequila-api.kiwi.com/v2/search?',
            params=self.params,
            headers={'apikey': FLIGHT_API}
        )
        search_req.raise_for_status()
        return search_req.json()['data']
