class CoffeeMachine:
    def __init__(self, water_level, coffee_level, milk_level, sugar_level=0, cups=0):
        self.__water_level = water_level
        self.__coffee_level = coffee_level
        self.__milk_level = milk_level
        self.__sugar_level = sugar_level
        self.__cups = cups

    def add_water(self,amount):
        self.__water_level+=amount
    def add_coffee(self,amount):
        self.__coffee_level+=amount
    def add_milk(self,amount):
        self.__milk_level+=amount
    def add_sugar(self,amount):
        self.__sugar_level+=amount
    def add_cups(self,number):
        self.__cups+=number

    def __check_resources(self,water,coffee,milk,sugar,cups):
        if self.__water_level-water>=0 and self.__coffee_level-coffee>=0 and \
           self.__milk_level-milk>=0 and self.__sugar_level-sugar>=0 and self.__cups-cups>=0:
            return True
        else:
            return False


    def make_coffee(self,water,coffee,milk,sugar,cups):
        result=CoffeeMachine.__check_resources(self,water,coffee,milk,sugar,cups)
        if result is True:
            print('Your order is done!')
        else:
            print('Sorry the Coffe Machine is empty for some resources.')