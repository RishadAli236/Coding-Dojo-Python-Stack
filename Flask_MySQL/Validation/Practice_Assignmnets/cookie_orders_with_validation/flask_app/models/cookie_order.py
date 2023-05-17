from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class CookieOrder:
    db = "cookie_orders"
    def __init__(self, data):
        self.id = data["id"]
        self.customer_name = data["customer_name"]
        self.cookie_type = data["cookie_type"]
        self.number_of_boxes = data["number_of_boxes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def add_order(cls, data):
        query = """
                INSERT INTO cookie_orders (customer_name, cookie_type, number_of_boxes)
                VALUES (%(customer_name)s, %(cookie_type)s, %(number_of_boxes)s);
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_orders(cls):
        query = """
                SELECT *
                FROM cookie_orders;
                """
        results = connectToMySQL(cls.db).query_db(query)
        orders = []
        for order in results:
            orders.append(cls(order))
        return orders
    
    @classmethod
    def get_one_order(cls, order_id):
        query = """
                SELECT *
                FROM cookie_orders
                WHERE id = %(id)s;
                """
        data = {"id" : order_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def edit_order(cls, data):
        query = """
                UPDATE cookie_orders
                SET customer_name = %(customer_name)s, cookie_type = %(cookie_type)s, number_of_boxes = %(number_of_boxes)s
                WHERE id = %(id)s;
            """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @staticmethod
    def is_valid(order_info):
        is_valid = True
        if order_info["customer_name"] == "":
            is_valid = False
            flash("Name is required")
        elif len(order_info["customer_name"]) < 2:
            is_valid = False
            flash("Name must be at least 2 characters")
        if order_info["cookie_type"] == "":
            is_valid = False
            flash("Cookie type is required")
        elif len(order_info["cookie_type"]) < 2:
            is_valid = False
            flash("Cookie type must be at least 2 characters")
        if order_info["number_of_boxes"] == "":
            is_valid = False
            flash("Number of boxes is required")
        elif int(order_info["number_of_boxes"]) < 0:
            is_valid = False
            flash("Number of boxes cannot be negative")
        return is_valid