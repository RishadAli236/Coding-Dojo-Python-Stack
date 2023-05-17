from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    db = "books_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.authors = []

    @classmethod
    def add_book(cls,data):
        query = """
                INSERT INTO books (title, num_of_pages)
                VALUES (%(title)s, %(num_of_pages)s);
            """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_books(cls):
        query = """
                SELECT * 
                FROM books;
                """
        results = connectToMySQL(cls.db).query_db(query)
        books = []
        for book in results:
            books.append(cls(book))
        return books
    
    @classmethod
    def get_one_book(cls, book_id):
        query = """
                SELECT * 
                FROM books
                WHERE id = %(id)s;
                """
        data = {"id" : book_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def edit_book(cls, data):
        query = """
                UPDATE books
                SET title = %(title)s, num_of_pages = %(num_of_pages)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def delete_book(cls, book_id):
        query = """
                DELETE FROM books
                WHERE id = %(id)s;
                """
        data = {"id" : book_id}
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_book_with_author(cls, book_id):
        query = """
                SELECT *
                FROM books
                LEFT JOIN favorites
                ON books.id = favorites.book_id
                LEFT JOIN authors
                ON favorites.author_id = authors.id
                WHERE books.id = %(id)s
                """
        data = {"id" : book_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        book = cls(results[0])
        for record in results:
            author_data = {
                "id" : record["authors.id"],
                "name" : record["name"],
                "created_at" : record["authors.created_at"],
                "updated_at" : record["authors.updated_at"]
            }
            book.authors.append(author.Author(author_data))
        return book
    
    @classmethod
    def add_author_favorite(cls, data):
        query = """
                INSERT INTO favorites (book_id, author_id)
                VALUES (%(book_id)s, %(author_id)s)
                """
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def authors_not_favorited(cls, book_id):
        query = """
                SELECT *
                FROM authors
                WHERE id
                NOT IN (SELECT author_id FROM favorites WHERE book_id = %(book_id)s)
                """
        data = {"book_id" : book_id}
        results = connectToMySQL(cls.db).query_db(query, data)
        authors = []
        for record in results:
            authors.append(author.Author(record))
        return authors
