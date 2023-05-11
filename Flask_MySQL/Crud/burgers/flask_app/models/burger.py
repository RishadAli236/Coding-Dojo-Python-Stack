from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import topping

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

