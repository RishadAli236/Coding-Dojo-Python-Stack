from flask import Flask, render_template, request, session, redirect
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
app.secret_key = "warzone"

bootstrap = Bootstrap5(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods = ["POST"])
def process():
    for key in request.form.keys():
        session[key] = request.form[key]
    return redirect("/results")

@app.route("/results")
def results():
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug = True)