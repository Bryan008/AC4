from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.rout("/Times")
def Times():
    return render_template("lista_cursos.html")
app.run()