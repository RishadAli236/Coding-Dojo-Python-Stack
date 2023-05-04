from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "warzone"

@app.route("/")
def index():
    # Check if session keys exist
    # if keys exist increament accordingly
    if "counter" in session:
        session["visit_count"] += 1
        session["counter"] += int(session["increament"])
    # if keys don't exist create and initialize them
    else:
        session["increament"] = 1 # Make the default increament value 1
        session["counter"] = 1 
        session["visit_count"] = 1 # SENSEI BONUS: Track how many times the page has actually been visited
    return render_template("index.html")

@app.route("/destroy_session")
def destroy_session():
    # Clear session and redirect to root route
    session.clear()
    return redirect("/")

# NINJA BONUS: Add a +2 button underneath the counter and a new route that will increment the counter by 2
@app.route("/add_two")
def add_two():
    session["counter"] += 2
    return redirect("/")

@app.route("/process", methods=["POST"])
def process():
    # Check if button was clicked without specifying increament
    if request.form["increament"] == "":
        pass
    else:
        session["increament"] = request.form["increament"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug = True)