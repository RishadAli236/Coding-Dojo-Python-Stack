from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    db = "books_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.books = []

    @classmethod
    def add_author(cls, data):
        query = """
                INSERT INTO authors (name)
                VALUES (%(name)s);
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_authors(cls):
        query = """
                SELECT *
                FROM authors;
                """
        results = connectToMySQL(cls.db).query_db(query)
        authors = []
        for author in results:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def get_one_author(cls, author_id):
        query = """
                SELECT *
                FROM authors
                WHERE id = %(id)s
                """
        data = {"id" : author_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def edit_author(cls, data):
        query = """
                UPDATE authors
                SET name = %(name)s
                WHERE id = %(id)s
                """
        return connectToMySQL(cls.db).query_db(query, data)
        
    @classmethod
    def delete_author(cls, author_id):
        query = """
                DELETE FROM authors
                WHERE id = %(id)s
                """
        data = {"id" : author_id}
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_author_with_books(cls, author_id):
        query = """
                SELECT *
                FROM authors
                LEFT JOIN favorites
                ON authors.id = favorites.author_id
                LEFT JOIN books
                ON favorites.book_id = books.id
                WHERE authors.id = %(id)s
                """
        data = {"id" : author_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        author = cls(results[0])
        for record in results:
            book_data = {
                "id" : record["books.id"],
                "title" : record["title"],
                "num_of_pages" : record["num_of_pages"],
                "created_at" : record["books.created_at"],
                "updated_at" : record["books.updated_at"]
            }
            author.books.append(book.Book(book_data))
        return author
    
    @classmethod
    def add_favorite_book(cls, data):
        query = """
                INSERT INTO favorites (author_id, book_id)
                VALUES (%(author_id)s, %(book_id)s)
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def unfavorited_books(cls, author_id):
        query = """
                SELECT *
                FROM books
                WHERE id 
                NOT IN (SELECT book_id FROM favorites WHERE author_id = %(author_id)s)
                """
        data = {"author_id" : author_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        books = []
        for record in results:
            books.append(book.Book(record))
        return books
        

