from abc import ABC,abstractmethod

class Discount(ABC):
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price
    @abstractmethod
    def give_discount(self):
        pass

class PriceForFavouriteCustomer(Discount):
    def give_discount(self):
        return self.price*0.2

class PriceForVIPCustomer(Discount):
    def give_discount(self):
        return self.price*0.4


customer=PriceForVIPCustomer('Dima',1000)
print(customer.give_discount())