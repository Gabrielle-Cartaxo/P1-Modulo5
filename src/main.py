from modules import funcoes
from flask import Flask, render_template, jsonify, request, redirect, url_for
from yaspin import yaspin
from tinydb import TinyDB
import inquirer

db = TinyDB("posts.json")
app = Flask(__name__)

site = funcoes()

@app.route("/", methods=["GET", "POST"])
def principal(funcao=None):
    if request.method == "POST":
        funcao = request.form.get("funcao")
        if funcao == "adicionar":
            return url_for 
        elif funcao == "pegar-caminho":
            return render_template("pegar-caminho.html")
        elif funcao == "lista":
            return render_template("lista-caminhos.html")
        elif funcao == "atualizar":
            return render_template("atualizar.html")
        elif funcao == "deletar":
            return render_template("deletar.html")
    return render_template("index.html")


@app.route("/novo", methods=["GET", "POST"])
def new():
    site.novo(x={{"x"}}, y={{"y"}}, z={{"z"}}, r={{"r"}})


@app.route("pegar-caminho")
def id_for_paths():
    site.pegar_caminho(id={{"id"}})


@app.route("listas-caminhos")
def all_paths():
    site.listas_caminhos()

@app.route("atualizar")
def refresh():
    site.atualizar(id={{"id"}}, x={{"x"}}, y={{"y"}}, z={{"z"}}, r={{"r"}})

@app.route("deletar")
def delete():
    site.delete()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 3000)