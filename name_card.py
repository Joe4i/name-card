from flask import Flask
from flask import render_template
import random
app = Flask(__name__)

@app.route("/")
def mySite():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=random.randint(5000, 9999))
