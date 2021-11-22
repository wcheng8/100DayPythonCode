#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager

# flight = FlightSearch('JFK')
# print((flight.search()))
# cost_data = FlightData(flight.search())
# print(cost_data.min_price)
# print(cost_data.currency)
# sheet = DataManager()
# sheet.get_country()
# sheet.write_price()
# sheet.get_price()
# sheet.write_price()

data = DataManager()
data.get_iataCode()

