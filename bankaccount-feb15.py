class BankAccount:

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    def __str__(self):
        return(f"Your account has a balance of {'balance'} and an interest rate of {'interest_rate'}.")

    def deposit(self, amount):
        self.balance += amount
        return(f"You have deposited {amount}. New account balance is {'balance'}.")

    def withdrawl(self, amount):
        self.balance -= amount
        return(f"You have withdrawn {amount}. New account balance is {'balance'}.")

    def gain_interest(self):
        self.balance *= (self.interest_rate/100) + 1
        return self.balance

account1 = BankAccount
print(account1)

print()
