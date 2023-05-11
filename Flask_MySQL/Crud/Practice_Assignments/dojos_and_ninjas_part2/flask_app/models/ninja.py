from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    db ="dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]

    @classmethod
    def add_ninja(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_ninja(cls, ninja_id):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        data = {"id" : ninja_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def delete(cls, ninja_id):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        data = {"id" : ninja_id}
        connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def edit(cls, data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s WHERE id = %(id)s;"
        connectToMySQL(cls.db).query_db(query, data)

    
    # Can use a Ninja class method to retrieve all ninjas that belong to a particular dojo using dojo id
    # @classmethod
    # def get_ninjas_by_dojo(cls, dojo_id):
    #     query = "SELECT * FROM ninjas WHERE dojo_id = %(dojo_id)s"
    #     data = {"dojo_id" : dojo_id}
    #     results = connectToMySQL(cls.db).query_db(query, data)
    #     ninjas = []
    #     for record in results:
    #         ninjas.append(cls(record))
    #     return ninjas