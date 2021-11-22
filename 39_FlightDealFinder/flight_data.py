class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, flightdata):
        self.costs = []
        self.min_price = flightdata[0]['price']
        self.currency = 'EUR'
        for flight in flightdata:
            price = flight['price']
            self.costs.append(price)
            if price < self.min_price:
                self.min_price = price

