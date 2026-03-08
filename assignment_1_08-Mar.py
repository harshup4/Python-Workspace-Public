import logging
logging.basicConfig(filename="assignment_08-Mar.log",filemode="a",level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
def discount_decorator(func):
    def wrapper(price):
        if price <0:
            logging.error("Invalid negative amount")
            return 
        if price<=500:
            return func(price)
        else:
            price = func(price)
            discounted_price = price-(price*10/100)
            return discounted_price
    return wrapper

def tax_decorator(func):
    def wrapper(price):
        if price <0:
            logging.error("Invalid negative amount")
            return 
        if price <=1000:
            return func(price)
        else:
            price = func(price)
            final_price = price+(price*18/100)
            return final_price
    return wrapper

@discount_decorator
@tax_decorator
def cal_price(base_price):
    return base_price
print(cal_price(500))
print(cal_price(600))
print(cal_price(1000))
print(cal_price(1001))
print(cal_price(-1))