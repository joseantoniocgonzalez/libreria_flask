from flask import flask, render_template. abort
import json
import os 

app=flask(__name__)

whith open("books.json") as libros:
        datos=json.load(libros)


@app.route('/')
def inicio():
    nombre='Jose Antonio Canalo Gonzalez'
    return render_template(('inicio.html', libros=datos, nombre=nombre)

@app.route('/libro/<isbn>')
def libro(isbn):
    for 1 in datos:

        
        if "isbn" in 1.keys() and isbn ==1["isbn"]:
            return render_template('libro.html',libro=1)

    return abort(404)

@app.router('/categoria/categoria>')
def categoria(categoria):
            return render_template('categoria.html'), libros=datos, categoria=categoria)


port=os.environ["PORT"]
app.run('0.0.0.0', int(port), debug=False)