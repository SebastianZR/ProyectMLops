from flask import Flask, render_template , request  # framework para renderizar los formularios 
import pickle # frameworks para poder usar el modelo previamente entrenado 
import numpy as np # ocuparemos numpy para poder meter las predicciones en una matriz

with open('./modelo.pkl' , 'rb') as modelo:#Con estas lineas abrimos el pickle y lo guardamos como "clf"
    clf = pickle.load(modelo)

app = Flask(__name__)#Inicializamos una aplicacion Flask llamada app

@app.route('/')# con esto definimos lo que aparecera en la ruta raiz de la pagina web
def index():
    return render_template("formulario.html") # retornaremos un formulario previamente echo en html 

@app.route('/predecir' , methods =['POST']) # Con esto lo que hacemos es mandar la prediccion cuando apretemos el boton de predecir 
def predecir():#esa es la funcion que usaremos
    sl = float(request.form.get("SL")) # tomamos los datos del formulario y los metemos en una variable cada uno
    sw = float(request.form.get("SW"))
    pl = float(request.form.get("PL"))
    pw = float(request.form.get("PW"))
    prediccion = clf.predict(np.array([[sl , sw , pl , pw]]))# creamos una array con los datos que ingreso el usuario para predecir
    if prediccion == 0:# Lo que hacen estos ifs es mandar una prediccion mas accesible ya que el modelo manda como prediccion numeros y apartir de esto convertimos los numeros a la flor que corresponda el numero de la prediccion
        return render_template("mostrar.html",  prediccion=" Setosa")
    elif prediccion == 1:
        return render_template("mostrar.html",  prediccion=" Versicolor")
    elif prediccion == 2:
        return render_template("mostrar.html",  prediccion=" Virginica")
    else:
        return render_template("mostrar.html", prediccion=" Error")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0") # Ajustes para que pueda verse en el servidor
