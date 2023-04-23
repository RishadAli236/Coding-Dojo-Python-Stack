from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<int:rows>")
@app.route("/<int:rows>/<int:columns>")
@app.route("/<int:rows>/<int:columns>/<color1>")
@app.route("/<int:rows>/<int:columns>/<color1>/<color2>")
def index(rows = 8, columns = 8, color1 = "red", color2 = "black"):
    return render_template("index.html", num_of_rows = rows, num_of_columns = columns, light_color = color1, dark_color = color2)

if __name__ == "__main__":
    app.run(debug = True)
