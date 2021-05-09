from flask import Flask, render_template, abort
import json
import os
app = Flask (__name__)

with open("books.json") as fichero:
    datos=json.load(fichero)

@app.route('/')
def inicio():
    return render_template("inicio.html",libros=datos)

@app.route('/libro/<isbn>')
def libro(isbn):
    for i in datos:
        if "isbn" in i.keys() and isbn == i["isbn"]:
            return render_template("libros.html",libro=i)
    abort(404)

@app.route('/categoria/<categoria>')
def categoria(categoria):
    for i in datos:
        if "categories" in i.keys() and categoria in i["categories"]:
            return render_template("categoria.html",libros=datos,categoria=categoria)
    abort(404)

port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)