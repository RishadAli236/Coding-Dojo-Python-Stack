from my_modules.bank_account import BankAccount

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