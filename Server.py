from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    return render_template("home.html")

@app.route("/aboutUs", methods=["POST","GET"])
def aboutUs():
    return render_template("aboutus.html")

@app.route("/sponsors", methods=["POST","GET"])
def sponsors():
    return render_template("sponsors.html")

@app.route("/divisions", methods=["POST","GET"])
def divisions():
    return render_template("divisions.html")
    

if __name__ == "__main__":
    app.run(debug=True)
