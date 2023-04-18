class BankAccount:
    all_accounts = []

    def __init__(self, int_rate, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        print(f"Interest rate: ${self.int_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
            return self
        else:
            print("Negative balance")
            return self
        
    @classmethod
    def display_all_account_info(cls):
        for account in BankAccount.all_accounts:
            account.display_account_info()

rishad_account = BankAccount(0.5)
yasin_account = BankAccount(0.1, 1000)

rishad_account.deposit(100).deposit(50).deposit(500).withdraw(200).yield_interest().display_account_info()
yasin_account.deposit(1000).deposit(300).withdraw(10).withdraw(50).withdraw(2000).withdraw(500).yield_interest().display_account_info()

BankAccount.display_all_account_info()
