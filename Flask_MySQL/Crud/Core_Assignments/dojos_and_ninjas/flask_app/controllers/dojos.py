from flask_app import app 
from flask import render_template, request, redirect
from flask_app.models import dojo
#from flask_app.models.ninja import Ninja

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def dojos():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("dojos.html", dojos = dojos)

@app.route("/add_dojo", methods = ["POST"])
def add_dojo():
    dojo.Dojo.add_dojo(request.form)
    return redirect("/dojos")

@app.route("/dojos/<int:dojo_id>")
def show_dojo(dojo_id):
    dojo_with_ninjas = dojo.Dojo.get_dojo_with_ninjas(dojo_id)
    return render_template("show_dojo.html", dojo = dojo_with_ninjas, ninjas = dojo_with_ninjas.ninjas)


# noticed that queries still run successfuly even if I don't change the id's to integers before passing them into the methods
# noticed that I could also use a Ninja method (get_ninjas_by_dojo) in order to get the ninjas that belong 
# to a particular dojo as long as I have the dojo id, this way I don't need to query a join in the dojo model

# @app.route("/dojos/<dojo_id>")
# def show_dojo(dojo_id):
#     dojo = Dojo.get_dojo(dojo_id)
#     ninjas = Ninja.get_ninjas_by_dojo(dojo_id)
#     return render_template("show_dojo.html", dojo = dojo, ninjas = ninjas)