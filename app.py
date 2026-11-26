from flask import Flask,  request, jsonify
import sqlite3
import database

app = Flask (__name__)


@app.route("/" , methods=["GET"])
def hw():
        return jsonify({"mensagem": "API funcionando"}), 200

@app.route("/usuarios", methods=["GET"])
def users():
      usuarios = database.listar_usuarios()
      return jsonify(usuarios), 200

@app.route("/usuarios", methods=["POST"])
def criar_user():
      dados = request.get_json()
      nome = dados.get("nome")
      email = dados.get("email")
      idade = dados.get("idade")

      if not nome or not email:
        return jsonify({
            "erro": "Nome e email são obrigatórios"
        }), 400

      try:
           usuario_id = database.criar_usuario(nome, email, idade)

           return jsonify({
                "mensagem":"Usuário cadastrado",
                "id":usuario_id
           }), 200
      
      except sqlite3.IntegrityError:
        return jsonify({
            "erro": "Email já cadastrado"
        }), 409
           
          
@app.route("/usuarios/<int:id>", methods=["GET"])
def buscar(id):
     usuario=database.buscar_user_por_id(id)
     if usuario is None:
          return jsonify({
               "erro":"Usuário não encontrado"
          }), 404
     return jsonify(usuario), 200

@app.route("/usuarios/<int:id>", methods=["PUT"]) #parametro de rota
def atualizar(id):
    dados = request.get_json()
    nome = dados.get("nome")
    email = dados.get("email")
    idade = dados.get("idade")

    if not nome or not email:
        return jsonify({
            "erro": "Nome e email são obrigatórios"
        }), 400
    try:
         atualizado = database.atualizar_usuario(id, nome, email, idade)
         if not atualizado:
              return jsonify({
                   "erro": "Usuário não encontrado"
              }),404
         return jsonify({
              "mensagem":"Usuário atualizado"
         }), 200
    except sqlite3.IntegrityError:
        return jsonify({
            "erro": "Email já cadastrado"
        }), 409

@app.route("/usuarios/<int:id>", methods=["DELETE"])
def deletar(id):
     deletado = database.deletar_usuario(id)
     if not deletado:
        return jsonify({
                   "erro": "Usuário não encontrado"
              }),404
     return jsonify({
              "mensagem":"Usuário deletado"
         }), 200
    


if __name__ == "__main__":
    database.criar_tabela()
    app.run(debug=True)

