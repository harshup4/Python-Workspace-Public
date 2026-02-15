class Product:
    def __init__(self, name, price,brand,warranty):
        self.name=name
        self.price=price
        self.brand=brand
        self.warranty=warranty
    def display(self):
        print(f'Name: {self.name}, Price: {self.price}, Brand: {self.brand}')
    def cal_price(self):
        total_price = self.price*self.count
        return total_price

class Electronics(Product):
    type = "Electronics"
    def __init__(self, name, price,brand,warranty,count):
        super().__init__(name, price,brand,warranty)
        self.count=count
    
    def displayAlldetails(self): 
        print(f'Name: {self.name}, Price: {self.price}, Brand: {self.brand}, Type: {self.type}, Warranty: {self.warranty}, Count: {self.count}'), 

e = Electronics("Laptop", 1000, "Lenovo", 2, 5)
print('Display Method:')
e.display()
print('\n')
print('Display All Details Method: ')
e.displayAlldetails()
print('\n')
print(f'Total Price: {e.cal_price()}')