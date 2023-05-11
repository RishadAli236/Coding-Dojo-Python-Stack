from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import dojo
from flask_app.models import ninja

@app.route("/ninjas")
def ninjas():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("ninjas.html", dojos = dojos)

@app.route("/add_ninja", methods = ["POST"])
def add_ninja():
    print(request.form)
    ninja.Ninja.add_ninja(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")