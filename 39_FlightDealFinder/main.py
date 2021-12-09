#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
# from notification_manager import NotificationManager
import requests

sheety_header = {
    'Content-Type':'application/json',
    "Authorization": "Bearer asdf123percenwcilk55"
}
url = 'https://api.sheety.co/d75e55864dbd2bd91cc468ff28a8f34f/flightDetails/flights'
body = {
  'flight': {
    'Price':'AHHA'
  }
}

edit_req = requests.post(url=url, headers = sheety_header, json=body)

# flight = FlightSearch('JFK')
# print((flight.search()))
# cost_data = FlightData(flight.search())
# print(cost_data.min_price)
# print(cost_data.currency)
# sheet = DataManager()
# sheet.get_iataCode()
# sheet.write_price()
# sheet.get_price()
# sheet.write_price()
# notification = NotificationManager(sheet)
# notification.send_msg()


# data = DataManager()
# data.get_iataCode()

