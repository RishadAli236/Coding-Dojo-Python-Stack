# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Friend:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.occupation = data["occupation"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL("first_flask").query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append(cls(friend))
        return friends
    
    # Method to add a record to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(occ)s, NOW(), NOW());"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL("first_flask").query_db(query, data)
    
    # Method to retrieve a single record given the id
    @classmethod
    def get_one(cls, friend_id):
        query = "SELECT * FROM friends WHERE id = %(id)s"
        data = {"id" : friend_id}
        result = connectToMySQL("first_flask").query_db(query, data)
        return cls(result[0])
    
    # Method to alter a record
    @classmethod
    def update_info(cls, data): # Pass in the data to update including the id of the record to alter
        query = "UPDATE friends SET first_name = %(fname)s, last_name = %(lname)s, occupation = %(occ)s WHERE id = %(id)s;"
        results = connectToMySQL("first_flask").query_db(query, data)
        return results # Should return None because Update returns nothing 
    
    # Method to delete a record
    @classmethod
    def delete(cls, friend_id):
        query = "DELETE FROM friends WHERE id = %(id)s;"
        data = {"id" : friend_id}
        connectToMySQL("first_flask").query_db(query, data)
        # Since DELETE does not return anything, no need for return statement?


        
    