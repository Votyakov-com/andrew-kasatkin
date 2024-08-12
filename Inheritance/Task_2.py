class Pastry:
    def __init__(self, name, price, manufacturing_date, term):
        self._name = name
        self._price = price
        self._manufacturing_date = manufacturing_date
        self._term = term

    def display(self):
        print(f'Name: {self._name}')
        print(f'Price: {self._price}')
        print(f'Manufacturing date: {self._manufacturing_date}')
        print(f'Term: {self._term}')

    def valid_until(self):
        print(f'Product was manufactured on: {self._manufacturing_date}')
        date = list(map(int, self._manufacturing_date.split('/')))
        if date[0] + self._term > 30:
            day = (date[0] + self._term - 30)
            month = date[1] + 1
        else:
            day = date[0] + self._term
            month = date[1]
        print(f'Product is suitable to ead till: {'/'.join(map(str, [day, month, date[2]]))}')


class Cake(Pastry):
    def __init__(self, name, price, manufacturing_date, term, filling):
        super().__init__(name, price, manufacturing_date, term)
        self._filling = filling

    def order(self):
        super().display()
        print(f'Filling: {self._filling}\n')
        super().valid_until()


class BentoCake(Pastry):
    def __init__(self, name, price, manufacturing_date, term, celebration):
        super().__init__(name, price, manufacturing_date, term)
        self._celebration = celebration

    def order(self):
        super().display()
        print(f'Celebration: {self._celebration}\n')
        super().valid_until()


cake1 = Cake('Торт', 1300, '25/7/2023', 13, 'strawberry')
cake2 = BentoCake('Тортик', 900, '13/6/2023', 10, 'Thanksgiving day')

cake1.order()
print('------------')
cake2.order()
