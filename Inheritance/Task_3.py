class BankAccount:
    def __init__(self, holder, balance, interest_rate):
        self.__holder = holder
        self.balance = balance
        self.interest_rate = interest_rate

    @property
    def holder(self):
        return self.__holder

    @holder.setter
    def holder(self, holder):
        self.__holder = holder

    def __str__(self):
        return f'Holder: {self.__holder}\n' + \
            f'Balance: {self.balance:,.2f}\n' + \
            f'Interest rate: {self.interest_rate}'


class BankOperation(BankAccount):
    def __init__(self, holder, balance, interest_rate):
        super().__init__(holder, balance, interest_rate)
        self.__id = id(self)
        self.dict_of_transactions = list()

    def deposit(self, amount):
        self.balance += amount
        self.dict_of_transactions.append(f'add {amount:,.2f}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Sorry!You can`t withdraw this amount of money.')
        else:
            self.balance -= amount
            self.dict_of_transactions.append(f'withdraw {amount:,.2f}')

    def add_interest(self):
        percents = self.balance * self.interest_rate

        self.balance += percents
        self.dict_of_transactions.append(f'deposit interest add {percents:,.2f}')

    def history(self):
        for item in self.dict_of_transactions:
            print(f'Account {self.__id}: {item}')


