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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.savings_account = BankAccount(int_rate = 0.02, balance = 0)
        self.checking_account = BankAccount(int_rate = 0, balance = 0)

    def make_deposit(self, account_type, amount):
        if account_type == "Savings":
            self.savings_account.deposit(amount)
            print(f"${amount} has been deposited to {self.name}'s {account_type} account")
        elif account_type == "Checking":
            self.checking_account.deposit(amount)
            print(f"${amount} has been deposited to {self.name}'s {account_type} account")
        return self

    def make_withdrawal(self, account_type, amount):
        if account_type == "Savings":
            self.savings_account.withdraw(amount)
            print(f"${amount} has been withdrawn from {self.name}'s {account_type} account")
        elif account_type == "Checking":
            self.checking_account.withdraw(amount)
            print(f"${amount} has been withdrawn from {self.name}'s {account_type} account")
        return self

    def display_user_balance(self, account_type):
        if account_type == "Savings":
            print(f"User: {self.name}, {account_type} balance: {self.savings_account.balance}")
        elif account_type == "Checking":
            print(f"User: {self.name}, {account_type} balance: {self.checking_account.balance}")
        return self
    
    def transfer_money(self, amount, other_user):
        self.checking_account.balance -= amount
        other_user.checking_account.deposit(amount)
        print(f"${amount} has been transferred from {self.name} to {other_user.name}'s Checking account")
        return self

user_rishad = User("Rishad", "email")
user_yasin = User("Yasin", "email")

user_rishad.make_deposit("Checking", 1000).display_user_balance("Checking").make_withdrawal("Checking", 500).display_user_balance("Checking")
user_rishad.make_deposit("Savings", 2000).display_user_balance("Savings").make_withdrawal("Savings", 700).display_user_balance("Savings")

user_rishad.transfer_money(200, user_yasin).display_user_balance("Checking")
user_yasin.display_user_balance("Checking")
