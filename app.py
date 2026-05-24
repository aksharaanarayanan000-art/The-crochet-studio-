from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# HEART
@app.route("/pattern1")
def pattern1():
    return render_template("pattern1.html")

# DINOSAUR
@app.route("/dino")
def dino():
    return render_template("pattern_dino.html")

# PENGUIN
@app.route("/penguin")
def penguin():
    return render_template("pattern_penguin.html")

# TOTE BAG
@app.route("/tote")
def tote():
    return render_template("pattern_tote.html")

# OCTOPUS
@app.route("/octopus")
def octopus():
    return render_template("pattern_octopus.html")

# CHERRY
@app.route("/cherry")
def cherry():
    return render_template("pattern_cherry.html")

# WHALE
@app.route("/whale")
def whale():
    return render_template("pattern_whale.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
