class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def display_account_info(self):
        print(f"Balance: {self.balance}")

    def yield_interest(self):
        self.balance += self.balance * self.int_rate

#Create first account
account1 = BankAccount()

# Make deposits and withdrawal for the first account
account1.deposit(100)
account1.deposit(69)
account1.deposit(420)
account1.deposit(75)
account1.withdraw(20)

# Create secound account
account2 = BankAccount()

#Make deposits and withdrawals for the second account
account2.deposit(1000)
account2.deposit(2000)
account2.deposit(1300)
account2.withdraw(50)

#calculate interest and display account info for the second account
account2.yield_interest()
account2.display_account_info()

account1.yield_interest()
account1.display_account_info()

