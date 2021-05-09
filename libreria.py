from flask import Flask, render_template, abort
import json
import os
app = Flask (__name__)

with open("books.json") as libros:
        datos=json.load(libros)


@app.route('/')
def inicio():
    nombre='Jose Antonio Canalo Gonzalez'
    return render_template('inicio.html', libros=datos, nombre=nombre)

@app.route('/libro/<isbn>')
def libro(isbn):
    for l in datos:

        
        if "isbn" in l.keys() and isbn == l["isbn"]:
            return render_template('libro.html',libro=1)

    return abort(404)

@app.route('/categoria/<categoria>')
def categoria(categoria):
            return render_template('categoria.html', libros=datos, categoria=categoria)
          

app.run(debug=True)