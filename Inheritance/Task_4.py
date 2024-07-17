class Investments:
    def __init__(self, ticker, price, currency, industry):
        self._ticker = ticker
        self._price = price
        self._currency = currency
        self._industry = industry

    def display(self):
        print(f'Ticker: {self._ticker}')
        print(f'Price: {self._price}')
        print(f'Currency: {self._currency}')
        print(f'Industry: {self._industry}')

def buying_securities(func):
    def inside_func(security):
        if security._echelon == 3:
            print('This deal is very risky!')
            return None
        return func(security)
    return inside_func

class Shares(Investments):
    def __init__(self,ticker, price, currency, industry,dividend,echelon,profit):
        super().__init__(ticker, price, currency, industry)
        self._dividend=dividend
        self._echelon=echelon
        self._profit=profit

    @buying_securities
    def buying(self):
        if self._profit > 5:
            q = int(input('Quantity: '))
            print(f'Purchase for is done: {(self._price * q):,.2f}')
        else:
            print('This deal is very risky!')


class Bonds(Investments):
    def __init__(self, ticker, price, currency, industry, coupon, echelon, nominal):
        super().__init__(ticker, price, currency, industry)
        self._coupon = coupon
        self._echelon = echelon
        self._nominal = nominal

    @buying_securities
    def buying(self):
        if self._price <= self._nominal:
            q = int(input('Quantity: '))
            print(f'Purchase for is done: {(self._price * q):,.2f}')
        else:
            print('This deal is very risky!')

