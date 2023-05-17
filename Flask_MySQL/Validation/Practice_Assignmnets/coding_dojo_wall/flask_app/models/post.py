from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash

class Post:
    db = "coding_dojo_wall"
    def __init__(self, data):
        self.id = data["id"]
        self.content = data["content"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.creator =  None

    @classmethod
    def add_post(cls, data):
        query = """
                INSERT INTO posts (content, user_id)
                VALUES (%(content)s, %(user_id)s)
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_posts_with_creators(cls):
        query = """
                SELECT *
                FROM posts
                JOIN users
                ON posts.user_id = users.id
                ORDER BY posts.created_at DESC
                """
        results = connectToMySQL(cls.db).query_db(query)
        all_posts = []
        for record in results:
            post = cls(record)
            user_data = {
                "id" : record["users.id"],
                "first_name" : record["first_name"],
                "last_name" : record["last_name"],
                "email" : record["email"],
                "password" : record["password"],
                "created_at" : record["created_at"],
                "updated_at" : record["users.updated_at"]
            }
            post.creator = user.User(user_data)
            all_posts.append(post)
        return all_posts
    
    @classmethod
    def delete_post(cls, data):
        query = """
                DELETE FROM posts
                WHERE id = %(id)s
                """
        #data = {"id" : id}
        return connectToMySQL(cls.db).query_db(query, data)
    
    @staticmethod
    def is_valid(post_content):
        is_valid = True
        if len(post_content["content"]) < 1:
            flash("Post content must not be blank", "post error")
            is_valid = False
        return is_valid
