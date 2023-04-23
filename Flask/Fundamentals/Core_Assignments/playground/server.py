from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play")
def play():
    return render_template("play.html")

@app.route("/play/<x>")
def play_x(x):
    return render_template("play_x.html", num = int(x))

@app.route("/play/<x>/<color>")
def play_x_color(x, color):
    return render_template("play_x_color.html", num = int(x), box_color = color)

if __name__ == "__main__":
    app.run(debug = True)
