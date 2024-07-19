class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if isinstance(amount, int):
            self.balance += amount

    def withdraw(self, amount):
        if isinstance(amount, int):
            if self.balance - amount >= 0:
                self.balance -= amount
            else:
                raise ValueError('Low balance alert!')

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return f'Your interest: {self.balance + (self.balance * self.interest_rate / 100)}'

    def get_interest_rate(self):
        return f'Your interest rate: {self.interest_rate}%'


class CheckingAccount(Account):
    def __init__(self, account_number, balance, fee_percentage):
        super().__init__(account_number, balance)
        self.fee_percentage = fee_percentage

    def deduct_fees(self):
        return f'Your deducted fees: {self.balance - (self.balance * self.fee_percentage / 100)}'

    def get_fee_percentage(self):
        return f'Your fee percentage: {self.fee_percentage}%'


class Bank:
    def __init__(self):
        self.accounts = dict()

    def add_account(self, obj):
        if obj.account_number not in self.accounts:
            self.accounts[obj.account_number] = obj
        else:
            print('Sorry! This account is already in our data base.')

    def delete_account(self, obj):
        if obj.account_number in self.accounts:
            del self.accounts[obj.account_number]
        else:
            print('Sorry! There is no that account in our data base.')

    def find_account(self, obj):
        if obj.account_number in self.accounts:
            print('We have this account in our data base!')
        else:
            print('Sorry! There is no that account in our data base.')

    def transfer_funds(self, source_account_number, destination_account_number, amount):
        if source_account_number and destination_account_number in self.accounts:
            if self.accounts[source_account_number].balance - amount >= 0:
                self.accounts[source_account_number].balance -= amount
                self.accounts[destination_account_number].balance += amount
            else:
                print('Transaction failed')
                print(f'Balance of source account: {self.accounts[source_account_number].balance}')
        else:
            print('We can`t find one of accounts!')



savings_account = SavingsAccount(account_number="SAV-001", balance=400, interest_rate=5)
checking_account = CheckingAccount(account_number="CHK-001", balance=500, fee_percentage=2)
bank = Bank()
bank.add_account(savings_account)
bank.add_account(checking_account)
print("Savings Account Balance:", savings_account.get_balance())
print("Checking Account Balance:", checking_account.get_balance())
print('------------------------------')
bank.transfer_funds(source_account_number="SAV-001", destination_account_number="CHK-001", amount=500)
print('------------------------------')
print("Savings Account Balance:", savings_account.get_balance())
print("Checking Account Balance:", checking_account.get_balance())