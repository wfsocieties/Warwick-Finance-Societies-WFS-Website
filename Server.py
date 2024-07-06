from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def homePage():
    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True)
