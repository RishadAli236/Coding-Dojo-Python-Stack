from flask import Flask, render_template, session, request, redirect
from user import User

app = Flask(__name__)

@app.route("/users")
def display_all_users():
    users = User.get_all()
    return render_template("read_all.html", users = users)

@app.route("/users/new")
def new_user():
    return render_template("create.html")

@app.route("/create", methods = ["POST"])
def create_user():
    User.create(request.form)
    return redirect("/users")

if __name__ == "__main__":
    app.run(debug = True)