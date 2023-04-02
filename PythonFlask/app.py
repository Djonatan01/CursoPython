from flask import Flask, render_template ,request
#Definição de nme da aplicação
app = Flask (__name__)

recebeFrutas = []
registros = []
Item = []

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
    app.run(debug=True)
    
#set FLASK_ENV=development serve para ativar o modo debug    
#flask run serve para ativar o python flask e rodar o servidor