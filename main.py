from flask import Flask, render_template , request 
import pickle
import numpy as np

with open('./modelo.pkl' , 'rb') as modelo:
    clf = pickle.load(modelo)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("formulario.html")

@app.route('/predecir' , methods =['POST'])
def predecir():
    sl = float(request.form.get("SL"))
    sw = float(request.form.get("SW"))
    pl = float(request.form.get("PL"))
    pw = float(request.form.get("PW"))
    prediccion = clf.predict(np.array([[sl , sw , pl , pw]]))
    if prediccion == 0:
        return render_template("mostrar.html",  prediccion=" Setosa")
    elif prediccion == 1:
        return render_template("mostrar.html",  prediccion=" Versicolor")
    elif prediccion == 2:
        return render_template("mostrar.html",  prediccion=" Virginica")
    else:
        return render_template("mostrar.html", prediccion=" Error")


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
