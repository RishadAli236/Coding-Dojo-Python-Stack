from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import dojo, ninja

@app.route("/ninjas")
def ninjas():
    dojos = dojo.Dojo.get_all_dojos()
    return render_template("ninjas.html", dojos = dojos)

# Alternative method of deleting ninja and redirecting --> seems more effiecient
@app.route("/add_ninja", methods = ["POST"])
def add_ninja():
    print(request.form)
    ninja.Ninja.add_ninja(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")

# @app.route("/ninja/delete/<int:ninja_id>")
# def delete_ninja(ninja_id):
#     ninja_info = ninja.Ninja.get_ninja(ninja_id)
#     ninja.Ninja.delete(ninja_id)
#     return redirect(f"/dojos/{ninja_info.dojo_id}")

@app.route("/ninja/delete/<int:ninja_id>/<int:dojo_id>")
def delete_ninja(ninja_id, dojo_id):
    ninja.Ninja.delete(ninja_id)
    return redirect(f"/dojos/{dojo_id}")

@app.route("/ninjas/edit/<int:ninja_id>")
def show_edit_ninja(ninja_id):
    ninja_info = ninja.Ninja.get_ninja(ninja_id)
    return render_template("edit.html", ninja = ninja_info)

@app.route("/ninja/edit", methods = ["POST"])
def edit_ninja():
    ninja.Ninja.edit(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")