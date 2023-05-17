from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods = ["POST"])
def register():
    if not User.is_valid(request.form):
        return redirect("/")
    else:
        password_hash = bcrypt.generate_password_hash(request.form["password"])
        print(password_hash)
        data = {
            "first_name" : request.form["first_name"],
            "last_name" : request.form["last_name"],
            "email" : request.form["email"],
            "password" : password_hash
        }
        user_id = User.create(data)
        session["user_id"] = user_id
        return redirect("/success")
    
@app.route("/success")
def success():
    if "user_id" not in session:
        flash("Please log in", "login error")
        return redirect("/")
    else:
        user = User.get_by_id(session["user_id"])
        return render_template("success.html", user = user)

@app.route("/login", methods = ["POST"])
def login():
    # see if the email provided exists in the database
    user = User.get_by_email(request.form["email"])
    # if user is not registered in the db
    if not user:
        flash("Invalid Email/Password", "login error")
        return redirect("/")
    else:
        if not bcrypt.check_password_hash(user.password, request.form["password"]):
            # if we get False after checking the password
            flash("Invalid Email/Password", "login error")
            return redirect("/")
        else:
            # if the passwords matched, we set the user_id into session
            session["user_id"] = user.id
            return redirect("/success")
        
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

