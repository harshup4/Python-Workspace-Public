discount = 0.10
def display_details(id, name, price, quantity):
  global discount
  disc_price = price - price * discount
  print(f"Product ID: {id}, Product Name: {name}, Price after discount: {disc_price}")

  def total_price(q):
    total=disc_price*q
    return total
  
  print(f'Total Price for {quantity} {name} is : {total_price(quantity)}')
  
display_details(1, "Laptop", 20000, 3)