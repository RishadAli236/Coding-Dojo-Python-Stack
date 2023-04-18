from my_modules import user

user_rishad = user.User("Rishad", "email")
user_yasin = user.User("Yasin", "email")

user_rishad.make_deposit("Checking", 1000).display_user_balance("Checking").make_withdrawal("Checking", 500).display_user_balance("Checking")
user_rishad.make_deposit("Savings", 2000).display_user_balance("Savings").make_withdrawal("Savings", 700).display_user_balance("Savings")

user_rishad.transfer_money(200, user_yasin).display_user_balance("Checking")
user_yasin.display_user_balance("Checking")
