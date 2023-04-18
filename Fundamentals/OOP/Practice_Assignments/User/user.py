class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}", f"Last Name: {self.last_name}", f"Email: {self.email}", f"Age: {self.age}", f"Member Status: {self.is_rewards_member}", f"Point: {self.gold_card_points}", sep="\n")

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member.")
            return False
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
            return True

    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("Not enough points")
        else:
            self.gold_card_points -= amount

user_rishad = User("Rishad", "Yasin", "rishad236@gmail.com", 26)
user_rishad.display_info()
user_rishad.enroll()

user_sharif = User("Sharif", "Muyanja", "smuyanja@codingdojo.com", 33)
user_yaaseen = User("Yaaseen", "Martin", "ymartin@codingdojo.com", 26)

user_rishad.spend_points(50)
user_sharif.enroll()
user_yaaseen.spend_points(80)


user_rishad.display_info()
user_sharif.display_info()
user_yaaseen.display_info()

user_rishad.enroll()
user_yaaseen.spend_points(40)






