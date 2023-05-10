from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.restaurant import Restaurant

@app.route("/restaurant")
def restaurant():
    Restaurant.get_restaurant_with_burgers({"id": 1})
