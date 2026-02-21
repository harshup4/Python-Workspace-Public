class Flight:
  def __init__(self, flight_no, base_price, total_seats):
    self.flight_no=flight_no
    self.base_price=base_price
    self.total_seats=total_seats

  def display_flight_info(self):
    print(f'{self.flight_no} has total seats: {self.total_seats} and its base price is {self.base_price}')

class DomesticFlight(Flight):
  def __init__(self, flight_no, base_price, total_seats, tax_percent):
    super().__init__(flight_no, base_price, total_seats)
    self.tax_percent=tax_percent
  
  def calculate_price(self):
    final_price = self.base_price + (self.base_price * self.tax_percent / 100)
    return final_price

class BookingFlight(DomesticFlight):
  def __init__(self, flight_no, base_price, total_seats, tax_percent, booked_seats):
    super().__init__(flight_no, base_price, total_seats, tax_percent)
    self.booked_seats=booked_seats
  
  def check_seat_availability(self):
    return self.total_seats>=self.booked_seats

  def book_seats(self):
    if self.check_seat_availability():
      left_over = self.total_seats-self.booked_seats
      print(f"Left over seats after booking is {left_over}")
    else:
      print('Requested no. of seats are not available')
  def get_final_price(self):
    if self.check_seat_availability():
      print(f'Total Price is {self.calculate_price() * self.booked_seats}')

book_flight = BookingFlight("IND-101", 8400, 32, 10, 32)
book_flight.check_seat_availability()
book_flight.book_seats()
book_flight.get_final_price()