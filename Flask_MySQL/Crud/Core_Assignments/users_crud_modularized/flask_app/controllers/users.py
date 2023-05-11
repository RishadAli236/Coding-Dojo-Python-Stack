from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.user import User 

@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def display_all_users():
    users = User.get_all()
    return render_template("read_all.html", users = users)

@app.route("/users/new")
def new_user():
    return render_template("create.html")

@app.route("/create", methods = ["POST"])
def create_user():
    user_id = User.create(request.form)
    return redirect(f"/users/{user_id}")

@app.route("/users/<int:user_id>")
def display_user(user_id):
    user = User.get_one(user_id)
    # print(type(user.created_at))
    # print(user.created_at.strftime("%B %d, %Y"))
    return render_template("read_one.html", user = user)

@app.route("/users/<int:user_id>/edit")
def edit(user_id):
    user = User.get_one(user_id)
    return render_template("edit.html", user = user)

@app.route("/edit", methods = ["POST"])
def update_user():
    User.update(request.form)
    return redirect(f"/users/{request.form['id']}")

@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    User.delete(user_id)
    return redirect("/users")
