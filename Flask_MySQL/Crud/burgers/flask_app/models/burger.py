from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import topping
from flask import flash

class Burger:
    db = "burgers_schema" #name of database
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.restaurant_id = data['restaurant_id']
        self.toppings = []

    @classmethod
    def save(cls,data):
        # When creating a burger we will need to pass the restaurant id as well
        query = "INSERT INTO burgers (name,bun,meat,calories,created_at,updated_at, restaurant_id) VALUES (%(name)s,%(bun)s,%(meat)s,%(calories)s,NOW(),NOW(), %(restaurant_id)s);"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM burgers;"
        burgers_from_db =  connectToMySQL(cls.db).query_db(query)
        burgers =[]
        for b in burgers_from_db:
            burgers.append(cls(b))
        return burgers

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM burgers WHERE burgers.id = %(id)s;"
        burger_from_db = connectToMySQL(cls.db).query_db(query,data)

        return cls(burger_from_db[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE burgers SET name=%(name)s, bun=%(bun)s, meat=%(meat)s, calories=%(calories)s,updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM burgers WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def get_burger_with_toppings(cls, burger_id):
        query = """ SELECT * FROM burgers
                    LEFT JOIN add_ons
                    ON burgers.id = add_ons.burger_id
                    LEFT JOIN toppings
                    ON add_ons.topping_id = toppings.id
                    WHERE burgers.id = %(id)s
                """
        data = {"id" : burger_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        burger = cls(results[0])
        for record in results:
            topping_data = {
                "id" : record["toppings.id"],
                "name" : record["toppings.name"],
                "created_at" : record["toppings.created_at"],
                "updated_at" : record["toppings.updated_at"]
            }
            burger.toppings.append(topping.Topping(topping_data))
        return burger
    
    @staticmethod
    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    # The method takes in a parameter which will be the data that needs to be validated
    # The data will be assumed to be in form of a dictionary
    def validate_burger(burger):
        is_valid = True # assume this is true
        if len(burger["name"]) < 3:
            flash("Name must be at least 3 characters", "name")
            is_valid = False
        if len(burger["bun"]) < 3:
            flash("Bun must be at least 3 characters", "bun")
            is_valid = False
        if len(burger["meat"]) < 3:
            flash("Meat must be at least 3 characters", "meat")
            is_valid = False
        if len(burger["calories"]) < 1 or (len(burger["calories"]) > 1 and int(burger["calories"]) < 200):
            flash("Calories must be 200 or greater", "calories")
            is_valid = False
        return is_valid


