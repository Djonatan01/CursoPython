from flask import Flask, render_template ,request
#Definição de nme da aplicação
app = Flask (__name__)

frutas = []
registros = []

@app.route('/', methods=["GET" , "POST"])
def principal():
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta")) #metodo append serve para inserir dados ao fim de uma lista; 
    return render_template("index.html" , frutas = frutas)

@app.route('/sobre', methods = ["GET","POST"])
def sobre():
    #notas = {"Fulano":5.0,"Beltrano":6.0,"Aluno":7.0}
    
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
         registros.append({"aluno": request.form.get("aluno"),"nota": request.form.get("nota")})
    return render_template("sobre.html",registros=registros)

if __name__ == "__main__":
    app.run(debug=False)