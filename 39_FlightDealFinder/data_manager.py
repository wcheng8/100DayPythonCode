import os
import requests
from dotenv import load_dotenv
from flight_data import FlightData
from flight_search import FlightSearch
from datetime import datetime
load_dotenv('../.env')

SHEETY_AUTH_TOKEN2 = os.getenv('SHEETY_AUTH_TOKEN2')
SHEETY_URL = 'https://api.sheety.co/d75e55864dbd2bd91cc468ff28a8f34f/flightDetails/flights'
FLIGHT_API = os.getenv('FLIGHTTEQ_API_KEY')

class DataManager:
    def __init__(self):
        self.locations_dict = []
        self.headers = {
            'Authorization': 'Bearer asdf123percenwcilk55'
        }

    def get_iataCode(self):
        req = requests.get(url=f'{SHEETY_URL}',headers=self.headers)
        country_data = req.json()['flights']
        print(country_data)
        country_list = []
        row_ids = []
        for country in country_data:
            country_list.append(country['city'])
            row_ids.append(country['id'])
        print(country_list)

        iaTa_list = []
        for country in country_list:
            params = {
                'term': f'{country}'
            }
            search_req = requests.get(
                url='https://tequila-api.kiwi.com/locations/query',
                params=params,
                headers={'apikey': FLIGHT_API}
            )
            search_req.raise_for_status()

            iaTa_list.append(search_req.json()['locations'][0]['code'])

        print(iaTa_list)

        for index in range(len(country_list)):
            flight_details = {'country': country_list[index], 'iaTaCode': iaTa_list[index], 'id': row_ids[index]}
            self.locations_dict.append(flight_details)

        print(self.locations_dict)

        for country in self.locations_dict:
            edit_row = {
                'flight':{
                    'iaTaCode': f'{country["iaTaCode"]}'
                }
            }
            edit_req = requests.put(url = f'{SHEETY_URL}/{country["id"]}', headers=self.headers, json=edit_row)
            print(edit_req.json())

    def get_country(self):
        req = requests.get(url=f'{SHEETY_URL}',headers=self.headers)
        country_data = req.json()['sheet1']
        print(req.json())
        for country in country_data:
            self.locations_code['ids'].append(country['id'])
            self.locations_code['countries_index'].append(country['iataCode'])
            self.locations_code['country'][country['iataCode']] = 0
        print(self.locations_code)
    #This class is responsible for talking to the Google Sheet.

    def get_price(self):
        for country_number in range(len(self.locations_code['ids'])):
            iaTaCode = self.locations_code['countries_index'][country_number]
            new_flight = FlightSearch(iaTaCode)
            flight_object = FlightData(new_flight.search())
            self.locations_code['country'][iaTaCode] = flight_object.min_price
            self.locations_code['country'][iaTaCode] = flight_object.local_departure
        print(self.locations_code)

    def write_price(self):
        for country_number in range(len(self.locations_code['ids'])):
            iaTaCode = self.locations_code['countries_index'][country_number]
            min_price = self.locations_code['country'][iaTaCode]
            id = self.locations_code['ids'][country_number]
            edit_row = {
                'sheet1':{
                    'Price': f'{min_price}'
                }
            }
            edit_req = requests.put(url = f'{SHEETY_URL}/{id}', headers=self.headers, json=edit_row)
            print(edit_req.json())