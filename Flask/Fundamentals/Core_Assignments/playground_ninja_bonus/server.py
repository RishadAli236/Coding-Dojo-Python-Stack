from flask import Flask, render_template

app = Flask(__name__)


@app.route("/play")
@app.route("/play/<x>") 
@app.route("/play/<x>/<color>")
def index(x = 3, color = "aqua"): # Assign default values to x and color
    return render_template("index.html", num = int(x), box_color = color)


if __name__ == "__main__":
    app.run(debug = True)