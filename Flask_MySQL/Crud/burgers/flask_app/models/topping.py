from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import burger

class Topping:
    db = "burgers_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        # we need have a list in case we want to show which burgers are related to the topping.
        self.burgers = []

    @classmethod
    def save(cls, data):
        pass

    @classmethod
    def get_topping_with_burgers(cls, topping_id):
        query = """ SELECT * FROM toppings
                    LEFT JOIN add_ons
                    ON toppings.id = add_ons.topping_id
                    LEFT JOIN burgers
                    ON add_ons.burger_id = burgers.id
                    WHERE toppings.id = %(id)s
                """
        data = {"id" : topping_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        topping = cls(results[0])
        for record in results:
            burger_data = {
                "id" : record["burgers.id"],
                "name" : record["burgers.name"],
                "bun" : record["bun"],
                "meat" : record["meat"],
                "calories" : record["calories"],
                "created_at" : record["burgers.created_at"],
                "updated_at" : record["burgers.updated_at"],
                "restaurant_id" : record["restaurant_id"]
            }
            topping.burgers.append(burger.Burger(burger_data))
        return topping