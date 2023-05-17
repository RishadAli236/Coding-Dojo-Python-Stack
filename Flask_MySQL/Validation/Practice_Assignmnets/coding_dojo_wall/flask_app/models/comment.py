from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Comment:
    db = "coding_dojo_wall"
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.post_id = data["post_id"]
        self.creator = None

    @classmethod
    def add_comment(cls,data):
        query = """
                INSERT INTO comments (content, user_id, post_id)
                VALUES (%(content)s, %(user_id)s, %(post_id)s)
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_comments_with_creators(cls):
        query = """
                SELECT *
                FROM comments
                JOIN users
                ON comments.user_id = users.id
                """
        results = connectToMySQL(cls.db).query_db(query)
        all_comments = []
        for record in results:
            comment = cls(record)
            user_data = {
                "id" : record["users.id"],
                "first_name" : record["first_name"],
                "last_name" : record["last_name"],
                "email" : record["email"],
                "password" : record["password"],
                "created_at" : record["created_at"],
                "updated_at" : record["users.updated_at"]
            }
            comment.creator = user.User(user_data)
            all_comments.append(comment)
        return all_comments
    
    @staticmethod
    def is_valid(comment):
        is_valid = True
        if len(comment["content"]) < 1:
            is_valid = False
            flash("Comment must not be blank", "comment error")
        return is_valid