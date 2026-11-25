from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from contextlib import closing

def conectar():
    return  sqlite3.connect("database_flask.db")


def criar_tabela():
    try:
        with closing(conectar()) as conexao:
            with conexao:
                cursor = conexao.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    idade INTEGER
                    )
                """)
        return True
    except sqlite3.IntegrityError as erro:
        print(f"Erro de integridade: {erro}")

    except sqlite3.OperationalError as erro:
        print(f"Erro operacional: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")




#C - CREATE
def criar_usuario(nome,email,idade):
    try:
        with closing(conectar()) as conexao:
            with conexao:
                cursor = conexao.cursor()
                cursor.execute("""
                    INSERT INTO usuarios (nome,email,idade)
                    VALUES(?,?,?)
            """, (nome,email,idade))
        return True
                
    except sqlite3.IntegrityError as erro:
        print(f"Erro de integridade: {erro}")

    except sqlite3.OperationalError as erro:
        print(f"Erro operacional: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")

# R - READ
def listar_usuarios():
    try:
        with closing(conectar()) as conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT * FROM usuarios")
            usuarios = cursor.fetchall() #fetchall retorna todos os registros encontrados
            list=[]
            for user in usuarios:
                dict={
                    "id": user[0],
                    "nome": user[1],
                    "email": user[2],
                    "idade": user[3],
                }
                list.append(dict)
            print(f"lista: {list}")
            json = jsonify(list)
            print(f"usuarios fetchall {usuarios}")
            return usuarios
  
    except sqlite3.IntegrityError as erro:
        print(f"Erro de integridade: {erro}")

    except sqlite3.OperationalError as erro:
        print(f"Erro operacional: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")


# R - READ
def buscar_user_por_id(id):
    try:
        with closing(conectar()) as conexao:
            with conexao:
                cursor=conexao.cursor()
                cursor.execute("SELECT * FROM usuarios WHERE id = ?",(id,))
                usuario= cursor.fetchone() #fetchone retorna somente um registro
        return usuario
    except sqlite3.IntegrityError as erro:
        print(f"Erro de integridade: {erro}")

    except sqlite3.OperationalError as erro:
        print(f"Erro operacional: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")
    
# U - UPDATE
def atualizar_usuario(id,nome,email,idade):
    try:
        with closing(conectar()) as conexao:
            with conexao:
                cursor= conexao.cursor()
                cursor.execute("""
                    UPDATE usuarios
                    SET nome = ?, email = ?, idade = ?
                    WHERE id = ?
            """, (nome,email,idade,id))
        return True
    except sqlite3.IntegrityError as erro:
        print(f"Erro de integridade: {erro}")

    except sqlite3.OperationalError as erro:
        print(f"Erro operacional: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")



# D - Delete
def deletar_usuario(id):
    try:
        with closing(conectar()) as conexao:
            with conexao:
                cursor = conexao.cursor()
                cursor.execute("DELETE FROM usuarios WHERE id = ?",(id,))
        return True
    except sqlite3.IntegrityError as erro:
        print(f"Erro de integridade: {erro}")

    except sqlite3.OperationalError as erro:
        print(f"Erro operacional: {erro}")

    except sqlite3.Error as erro:
        print(f"Erro no banco de dados: {erro}")




criar_tabela() 
# criar_usuario("Elo","elolinda@gmail.com",20)
# criar_usuario("Daniel","daniel@gmail.com",20)
# criar_usuario("Viviane","vivi@gmail.com",47)
app = Flask (__name__)


@app.route("/")
def hw():
        return "salve salve"

@app.route("/usuarios")
def users():
      usuarios = listar_usuarios()
      return f"<p>{usuarios}</p>"
          


@app.route("/sobre")
def about():
      return "about us"



