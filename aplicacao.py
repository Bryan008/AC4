from flask import Flask
from flask import render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://Bryan:0210@localhost/cadastro'
db = SQLAlchemy(app)


class cadastro(db.Model):
    __tablename__="cadastrar"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.String(20))
    membro = db.Column(db.String(20))
    
    def __init__(self,time,membro):
        self.time = time
        self.membro = membro
    

db.create_all()

@app.route("/")
@app.route("/home")
def index():
    return render_template("Escopo.html")

@app.route("/tabajara")
def Tabajara():
    return render_template("tabajara.html")

@app.route("/boiadeiros")
def boiadeiros():
    return render_template("boiadeiros.html")

@app.route("/timedocopo")
def Time_Do_Copo():
    return render_template("timedocopo.html")

@app.route("/cornos")
def Os_Cornos():
    return render_template("cornos.html")

@app.route("/cupins")
def Os_Cupins():
    return render_template("cupins.html")

@app.route("/latao")
def Latao_Da_Melhor():
    return render_template("latao.html")

@app.route("/Resultados")
def Resultados():
    return render_template("Resultados.html")

@app.route("/Escopo")
def Escopo():
    return render_template("Escopo.html")
    
@app.route("/mensagem")
def mensagem():
    return render_template("mensagem.html")
    
@app.route("/Cadastro")
def Cadastro():
    return render_template("cadastrar.html")

@app.route("/cadastrar",methods=['GET', 'POST'])
def cadastrar():
    if request.method =="POST":
        time = (request.form.get("time"))
        membro = (request.form.get("membro"))
        if time:
            f = cadastro(time,membro)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("listar"))

@app.route("/listar")
def listar():
    cadastros = cadastro.query.all()
    return render_template("listar.html", cadastro=cadastros)


if __name__ == "__main__":
    app.run(debug=True)




app.run()
