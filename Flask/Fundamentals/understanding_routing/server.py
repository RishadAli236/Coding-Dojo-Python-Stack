from flask import Flask
app = Flask(__name__)

# SENSEI BONUS
@app.errorhandler(404)
def no_response(e):
    return "Sorry! No response. Try again."

@app.route("/")
def index():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<string:name>")
def say_hi(name):
    return f"Hi {name.capitalize()}"

@app.route("/repeat/<int:num>/<string:txt>")
def repeat(num , txt):
    return txt * num


if __name__ == "__main__":
    app.run(debug = True)