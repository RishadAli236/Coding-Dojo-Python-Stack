from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    db = "login_and_registration"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {"id" : user_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def get_by_email(cls, user_email):
        query = "SELECT * FROM users WHERE email = %(email)s"
        data = {"email" : user_email}
        result = connectToMySQL(cls.db).query_db(query, data)
        if len(result) < 1:
            return False
        else:
            return cls(result[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def delete(cls, user_id):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id" : user_id}
        connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all_emails(cls):
        query = "SELECT email FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        emails = []
        for record in results:
            emails.append(record["email"])
        print(emails)
        return emails
    
    @staticmethod
    def is_valid(user_info):
        is_valid = True
        if len(user_info["first_name"]) < 3:
            is_valid = False
            flash("First name should have at least 3 characters")
        elif not user_info["first_name"].isalpha():
            is_valid = False
            flash("First name should have letters only")
        if len(user_info["last_name"]) < 3:
            is_valid = False
            flash("Last name should have at least 3 characters")
        elif not user_info["last_name"].isalpha():
            is_valid = False
            flash("Last name should have letters only")
        if not EMAIL_REGEX.match(user_info["email"]):
            is_valid = False
            flash("Invalid email address")
        elif user_info["email"] in User.get_all_emails():
            is_valid = False
            flash("This email already exists")
        if len(user_info["password"]) < 8:
            is_valid = False
            flash("Password should be at least 8 characters")
        # Ninja bonus
        elif user_info["password"].isnumeric() or user_info["password"].isalpha() or user_info["password"].islower():
            is_valid = False
            flash("Password has to have a least 1 number and 1 uppercase letter")
        if user_info["password_confirmation"] != user_info["password"]:
            is_valid = False
            flash("Password must match password confirmation")
        return is_valid
        