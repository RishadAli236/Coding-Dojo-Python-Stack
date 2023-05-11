from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name= data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def add_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for record in results:
            dojos.append(cls(record))
        return dojos
    
    @classmethod
    def get_dojo(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {"id" : dojo_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_dojo_with_ninjas(cls, dojo_id):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s;"
        data = {"dojo_id" : dojo_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        dojo = cls(results[0])
        for record in results:
            ninja_data = {
                "id" : record["ninjas.id"],
                "first_name" : record["first_name"],
                "last_name" : record["last_name"],
                "age" : record["age"],
                "created_at" : record["ninjas.created_at"],
                "updated_at" : record["ninjas.updated_at"],
                "dojo_id" : record["dojo_id"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo
