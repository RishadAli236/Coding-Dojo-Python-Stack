from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import author, book

@app.route("/")
def index():
    return redirect ("/authors")

@app.route("/authors")
def display_authors():
    authors = author.Author.get_all_authors()
    return render_template("authors.html", authors = authors)

@app.route("/create_author", methods = ["POST"])
def create_author():
    author.Author.add_author(request.form)
    return redirect("/authors")

@app.route("/authors/<int:author_id>")
def show_author(author_id):
    author_with_books = author.Author.get_author_with_books(author_id)
    # NINJA Bonus Personal attempt: `Author Show` page, only display the books in the drop down that have not already been added to the authors favorites
    # books = book.Book.get_all_books()
    # for favorited_book in author_with_books.books:
    #     for one_book in books:
    #         if favorited_book.title == one_book.title:
    #             books.remove(one_book)
    #             break

    # Ninja Bonus: Solution
    unfavorited_books = author.Author.unfavorited_books(author_id)
    return render_template("author_show.html", author = author_with_books, unfavorited_books = unfavorited_books)

@app.route("/add_favorite_book", methods = ["POST"])
def add_favorite_book():
    author.Author.add_favorite_book(request.form)
    return redirect(f"/authors/{request.form['author_id']}")