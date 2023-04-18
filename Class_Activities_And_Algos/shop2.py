# Worldy wacky shop of wonders!!!!

# Together as a group, come up with an idea for a shop that sells anything you want. 
# Think about what a shop might have as attributes, maybe a name, address, list of items etc
# Associate that Shop with another class called Inventory 
# Give the inventory a name and a price.

# Create the items first and then create the Shop and add the items to the shops inventory
# Make a method to loop through the inventory and display the info of each item - think about how you can simplify that code in the class

# Bonus: create a staticmethod to check and make sure in the Item class: the name is not an empty string and the price is greater than 0
# Bonus: Validate the values before creating the Item and print "Not valid" if it fails
# Bonus: Add some more methods together and embrace your creativity!

class Shop:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(Item(item))

    def add_items(self, item_data_list):
        for item_data in item_data_list:
            self.inventory.append(Item(item_data))

    def display_item_info(self):
        for item in self.inventory:
            print(f"{item.name} : ${item.price}")
        print("\n")

class Item: 
    def __init__(self, item):
        self.name = item["name"]
        self.price = item["price"]

car_data_list = [
    {
        "name" : "Nissan",
        "price" : 27000
    },
    {
        "name" : "Mazda",
        "price" : 26000
    },
    {
        "name" : "Mustang",
        "price" : 30000
    },
    {
        "name" : "Tesla",
        "price" : 40000
    }
]

new_item = {"name" : "Volvo", "price" : 50000}

car_shop = Shop("Ninja cars", "123 Maple st")
print(car_shop.inventory)
car_shop.add_items(car_data_list)
print(car_shop.inventory)
car_shop.display_item_info()
car_shop.add_item(new_item)
car_shop.display_item_info()




