from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/escopo")

def index():
    return render_template("Escopo.html")
    
app.run()

