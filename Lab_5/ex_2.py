# Design a bank account system with a base class Account and subclasses SavingsAccount and CheckingAccount. 
# Implement methods for deposit, withdrawal, and interest calculation.

class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def calculate_interest(self):
        return 0

class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, interest_rate=0.02):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Calculated interest: ${interest}")
        return interest

class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, balance=0, overdraft_limit=100):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self.balance + self.overdraft_limit):
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid withdrawal amount or overdraft limit reached.")

print("\n")
savings_account = SavingsAccount(account_number="SA123", holder_name="John Doe", balance=1000)
savings_account.deposit(500)
savings_account.calculate_interest()
savings_account.withdraw(200)

print("\n")

checking_account = CheckingAccount(account_number="CA456", holder_name="Jane Doe", balance=500, overdraft_limit=200)
checking_account.deposit(300)
checking_account.withdraw(700)
checking_account.withdraw(100)
