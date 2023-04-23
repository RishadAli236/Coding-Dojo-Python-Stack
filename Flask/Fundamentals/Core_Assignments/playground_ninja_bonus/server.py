from flask import Flask, render_template

app = Flask(__name__)


@app.route("/play")
def play(x = 3, color = "aqua"): # Assign default values to x and color
    return render_template("index.html", num = x, box_color = color)

@app.route("/play/<x>") 
def play_x(x = 3, color = "aqua"):
    return render_template("index.html", num = int(x), box_color = color)

@app.route("/play/<x>/<color>")
def play_x_color(x = 3, color = "aqua"):
    return render_template("index.html", num = int(x), box_color = color)

if __name__ == "__main__":
    app.run(debug = True)