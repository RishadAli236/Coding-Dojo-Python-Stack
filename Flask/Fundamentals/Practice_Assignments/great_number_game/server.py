from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)
app.secret_key = "warzone"

@app.route("/")
def index():
    if "random_number" in session:
        pass
    else:
        session["random_number"] = random.randint(1,10)
        print(session["random_number"])
    return render_template("index.html")

@app.route("/guess", methods = ["POST"])
def guess():
    if int(request.form["player_guess"]) > session["random_number"]:
        session["results"] = "Too High"
    elif int(request.form["player_guess"]) < session["random_number"]:
        session["results"] = "Too Low"
    else:
        session["results"] = f"You guessed it! The number was {request.form['player_guess']}"
    return redirect("/")


if __name__ == "__main__":
    app.run(debug = True)