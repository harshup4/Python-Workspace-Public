class Flight:
    def __init__(self, flight_no,source,destination,base_fare):
        self.flight_no=flight_no
        self.source=source
        self.destination=destination
        self.base_fare=base_fare
    
    def get_flight_info(self):
        return f"Flight No: {self.flight_no}\nSource: {self.source}\nDestination: {self.destination}"

    def calculate_fare(self, count,discount_percentage=0):
        total_fare = self.base_fare * count
        if discount_percentage !=0:
            discount_amount = total_fare*(discount_percentage/100)
            total_fare=total_fare-discount_amount
        return total_fare
    def update_route(self,destination,source=None):
        self.destination=destination
        if source is not None:
            self.source=source


flight = Flight("IND-101", "Pune", "New Delhi", 3000)
print(f"Flight Info: \n{flight.get_flight_info()}")
print(f"Total Fare: {flight.calculate_fare(3)}")
print(f"Total Fare: {flight.calculate_fare(3,10)}")
flight.update_route("Bangalore")
print(f"Flight Info after Destination update: \n{flight.get_flight_info()}")
flight.update_route("Srinagar", "Chennai")
print(f"Flight Info after Source & Destination update \n{flight.get_flight_info()}")