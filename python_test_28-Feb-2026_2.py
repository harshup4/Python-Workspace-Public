flight_no = "AI203"
base_fare = "4500.75"
tax_percent = "5"
seat_numbers = "12A,12B,14C,15D"
is_international = "True"

final_fare = float(base_fare)+(float(base_fare) *int(tax_percent)/100)
print(final_fare)

list_of_seats = seat_numbers.split(",")
print(list_of_seats)

print(set(list_of_seats))

print(bool(is_international))

flight_summary = {"Flight No": flight_no, "Final Fare":int(final_fare), "Seat Numbers": tuple(list_of_seats)}
print(flight_summary)