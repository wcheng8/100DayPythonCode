class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, flightdata):
        self.costs = []
        self.min_price = flightdata[0]['price']
        self.currency = 'EUR'
        self.min_price_index = 0
        self.local_departure = ''
        for flight in flightdata:
            price = flight['price']
            self.costs.append(price)
            if price < self.min_price:
                self.min_price = price
                self.local_departure = flight['local_departure']

