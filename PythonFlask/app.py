from flask import Flask, render_template ,request
from flask_sqlalchemy import SQLAlchemy


#Definição de nme da aplicação
app = Flask (__name__)
# create the extension
db = SQLAlchemy(app)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cursos.db"

recebeFrutas = []
registros = []
Item = []

class cursos(db.Model):
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



if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    