from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.cookie_order import CookieOrder

@app.route("/")
def index():
    return redirect("/cookies")

@app.route("/cookies")
def dashboard():
    all_orders = CookieOrder.get_all_orders()
    return render_template("cookies.html", all_orders = all_orders)

@app.route("/cookies/new")
def new_order():
    return render_template("new_order.html")

@app.route("/log_new_order", methods = ["POST"])
def log_new_order():
    if not CookieOrder.is_valid(request.form):
        for key in request.form.keys():
            session[key] = request.form[key]
        return redirect("/cookies/new")
    else:
        CookieOrder.add_order(request.form)
        session.clear()
        return redirect("/cookies")

@app.route("/cookies/<order_id>")
def edit(order_id):
    order = CookieOrder.get_one_order(order_id)
    return render_template("edit.html", order = order)

@app.route("/edit_order", methods = ["POST"])
def update_order():
    if not CookieOrder.is_valid(request.form):
        return redirect(f"/cookies/{request.form['id']}")
    else:
        CookieOrder.edit_order(request.form)
        return redirect("/cookies")
