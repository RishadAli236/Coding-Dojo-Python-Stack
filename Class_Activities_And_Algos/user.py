class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def greeting(self):
        print(f"Hi my name is {self.first_name} {self.last_name}")

user_ada = User("Ada", "Lovelace", 42)
print(type(user_ada.greeting()))
