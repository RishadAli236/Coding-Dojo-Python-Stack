from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import book, author

@app.route("/books")
def display_books():
    books = book.Book.get_all_books()
    return render_template("books.html", books = books)

@app.route("/create_book", methods = ["POST"])
def create_book():
    book.Book.add_book(request.form)
    return redirect("/books")

@app.route("/books/<int:book_id>")
def show_book(book_id):
    book_with_authors = book.Book.get_book_with_author(book_id)
    # NINJA Bonus Personal attempt: `Book Show` page, only display the authors in the drop down that have not already been added to the list of books favorite authors
    # authors = author.Author.get_all_authors()
    # for author_favorite in book_with_authors.authors:
    #     for one_author in authors:
    #         if author_favorite.name == one_author.name:
    #             authors.remove(one_author)
    #             break

    # Ninja Bonus: Solution
    authors_not_favorited = book.Book.authors_not_favorited(book_id)
    return render_template("book_show.html", book = book_with_authors, authors_not_favorited = authors_not_favorited)

@app.route("/add_author_favorite", methods = ["POST"])
def add_author_favorite():
    book.Book.add_author_favorite(request.form)
    return redirect(f"/books/{request.form['book_id']}")
