from flask import Flask, render_template, jsonify, request, redirect, url_for
from yaspin import yaspin
from tinydb import TinyDB
import inquirer
db = TinyDB("posts.json")



class funcoes:
    def __init__(self) -> None:
        pass
    
    def novo(x=int, y=int, z=int, r=int):
        if request.method =="POST":
         db.insert({"x":x, "y":y, "z":z, "r":r})
        return render_template("novo.html", x=x, y=y, z=z, r=r)

    def pegar_caminho(id):
        if request.method =="POST":
            db.search(id=={{id}})
            return render_template("pegar-caminho.html", id= {{"id"}})


    def listas_caminhos(Self):
        db.all()

    def atualizar(id= int, x=int, y=int, z=int, r=int):
        db.update({'id': <id>, 'x':<x>, 'y':<y>, 'z':<z>, 'r'=<r>})
        return render_template ("atualizar.html")

    def deletar(Self):
        db.remove('id'== id)
        return render_template("../../static/remover.html")