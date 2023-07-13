from flask import Flask, render_template ,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

#Definição de nme da aplicação
app = Flask (__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cursos.sqlite3"
#Crição do banco de dados SQLAlchemy
db = SQLAlchemy(app)

recebeFrutas = []
registros = []
Item = []

class tb_cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    ch = db.Column(db.Integer)

    def __init__(self,nome,descricao,ch):
        self.nome = nome
        self.descricao = descricao
        self.ch = ch

@app.route('/', methods=["GET" , "POST"])
def principal():
    if request.method == "POST":
        if request.form.get("fruta"):
            recebeFrutas.append(request.form.get("fruta")) #método append serve para inserir dados ao fim de uma lista;
    return render_template("index.html" , recebeFrutas = recebeFrutas)

@app.route('/itens',methods = ["GET" ,"POST"])
def itens():
    if request.method=="POST":
        if request.form.get("Item"):
            Item.append(request.form.get("Item"))
    return render_template("itens.html", Item = Item)

@app.route('/sobre', methods = ["GET","POST"])
def sobre():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
         registros.append({"aluno": request.form.get("aluno"),"nota": request.form.get("nota")})
    return render_template("sobre.html",registros=registros)

@app.route('/cursos')
def lista_cursos():
    return render_template("cursos.html",cursos=tb_cursos.query.all())

@app.route('/cadastro_curso',methods=["GET","POST"])
def cadastar_cursos():
    nome = request.form.get('nome')
    des = request.form.get('desc_curso')
    ch_curso = request.form.get('ch_curso')

    if request.method == 'POST':
        curso = tb_cursos(nome ,des,ch_curso)
        db.session.add(curso)
        db.session.commit()
        return redirect(url_for('lista_cursos'))
    return render_template("cadastroCurso.html")

if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(debug=True)
