from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("Escopo.html")

@app.route("/tabajara.html")
def Tabajara():
    return render_template("tabajara.html")

@app.route("/boiadeiros.html")
def boiadeiros():
    return render_template("boiadeiros.html")

@app.route("/timedocopo.html")
def Time_Do_Copo():
    return render_template("timedocopo.html")

@app.route("/cornos.html")
def Os_Cornos():
    return render_template("cornos.html")

@app.route("/cupins.html")
def Os_Cupins():
    return render_template("cupins.html")

@app.route("/latao.html")
def Latao_Da_Melhor():
    return render_template("latao.html")

@app.route("/Resultados.html")
def Resultados():
    return render_template("Resultados.html")

@app.route("/Escopo.html")
def Escopo():
    return render_template("Escopo.html")


app.run()