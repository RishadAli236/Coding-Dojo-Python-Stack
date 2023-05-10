from flask_app.config.mysqlconnection import connectToMySQL

class Restaurant:
    db = "burgers_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # We create a list so that later we can add in all the burgers that are associated with a restaurant.
        self.burgers = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO restaurants ( name , created_at , updated_at, restaurant_id ) VALUES (%(name)s,NOW(),NOW());"
        results = connectToMySQL(cls.db).query_db(query, data)
        return results
    
    @classmethod
    def get_restaurant_with_burgers(cls, data):
        query = "SELECT * FROM restaurants LEFT JOIN burgers ON restaurants.id = burgers.restaurant_id WHERE restaurants.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        print(results)
        restaurant = cls(results[0])
        return restaurant