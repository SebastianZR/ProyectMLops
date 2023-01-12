
# Proyecto MLOps DevF
## Introudccion
Este proyecto es parte de el modulo de Machine Learning en produccion del masterclass en Ciencia de Datos, este proyeecto nos ayudara a unir los conceptos de Apredizaje Automatico y empezar a ponerlo en produccion con conocimientos en linux , redes , servidores y con herramientas como Airflow para poder crear todo el proceso desde la recoleccion de datos , el entrenamiento , poner el modelo en produccion ya sea una api o una aplicacion web o de otros tipos.

# Proceso 
## Dataset
El primer paso en todo proyecto de programacion es definir un problema , ya que tenemos definido el problema lo que sigue es encontrar el dataset adecuado para poder entrenar el modelo, en este caso para hacerlo mas practico y dedicarnos solo a proceso como tal de el area de MLOps usamos el dataset por defecto de scikit-learn de Iris.
## Modelo
Para el modelo igual para hacer este ejercicio mas enfocado en el area de MLOps elegimos una regresion logistica la cual nos dio una Score de aprox 90% de efectividad, ya que entrenamos el modelo lo guardamos con la ayuda de la libreria joblib en un archivo con formato pickle para poder usarlo en un futuro.
## Implementacion
Para la aplicacion del modelo decidi desplegarlo en una oplicacion web con la ayuda del Framework de Flask que me permite desplegar un servidor web,para esto decidi informarme mas sobre este Framework y gracias a esto pude programar un formulario y apartir de este recopilar los datos para hacer la prediccion, igual podria agregarle estilos en un futuro y una mejor presentacion.
## Alojamiento Web
Para alojar mi aplicacion web Me decidio por Amazon Web Services ya que me parece muy amigable y ya eh trabajado previamente con este , para iniciar accedi al panel de EC2 y lance una una nueva instancia con un sistema operativo Ubuntu 22.04 y elegi una maquina t2 micro ya que me brinda mas memoria RAM y es apto para la capa gratuita, escogi 10gb de memoria la instancia y abri el puerto 5000 de tcp que es por el cual Flask trabaja por defecto , descarge mi clave ssh para poderme conectar desde mi maquina para poder empezar a configurar el servidor y poder subir mi aplicacion web.
## Configuracion
Primero para poder acceder ala instancia de AWS tenemos que conectarnos por ssh para eso ocupe el comando en consola de:
```bash
$ ssh -i "serverMLops.pem" ubuntu@ec2-54-226-236-135.compute-1.amazonaws.com
```
ahora vamos a verificar que tenemos instalado python y si no lo instalaremos para verificar solo tenemos que hacerlo con el siguiente comando en consola :
```bash
$ python --version
```
si la consola no nos dice que no conoce el comando o tenemos una version de python inferior a python 3 lo que haremos es instalar python3 con el siguiente comando como estamos trabajando con ubuntu usaremos aptitude y para eso escribiremos esto en la consola:
```bash 
$ sudo apt install python3
```
una ves instalado python hay que actualizar pip3 que es el instalador de paquetes de python
para poder instalar bien todos los paquetes de python que necesitamos para correr el proyecto para eso usaremos el siguiente comando:
```bash
$ pip3 install --upgrade pip
```
ahora como tengo el proyecto guardado en github lo unico que hare es clonar el repositorio en una carpeta de la instancia con el comando:
```bash
$ git clone https://github.com/SebastianZR/ProyectMLops.git
```
bajara una copia de mi repositorio en la maquina solo ingresamos a esa carpeta y activamos el entorno virtual que viene ya en el proyecto y tiene todo lo necesario para poder correr la aplicacion con el siguiente comando 
```bash
$ source env/bin/activate
```
## Correr aplicacion
El comando visto anteriormente ya deja lista nuestro entorno para ejecutar la aplicacion , y hay dos formas de desplegar la aplicacion la primera es correrla directa con python con el siguiente comando:
```bash
python main.py
```
una ves echo esto ya estara arriba nuestra aplicacion en el servidor solo tenemos que compartir el link de nuestro servidor y ingresar por el puerto 5000 y si queremos que solo al ingresar veamos la app podemos configurar en Flask por el puerto 80 para que sea por default.
  
La segunda forma de correrlo es usando docker ya que tenemos dockerfile para poder crear la imagen y correra lo unico que tenemos que hacer es instalar docker donde lo quedramos correr , abrir la carpeta del proyecto y correr el siguiente comando para crear la imagen en nuestro equipo: 
```bash 
$ docker build -t mlops-ml .
```
lo que hicimos con este comando es crear la imagen apartir del dockerfile de la carpeta y la llamamos mlips-ml y el punto es para usar todo lo que esta en la carpeta, lo que falta ahora es correr la imagen y lo haremos con el siguiente comando:
```bash
$ docker run -it -p 5000:5000 -d mlops-ml
```
lo que hace este comandoe es correr la imagen mlops-ml y hacerlo por el puerto 5000 tanto del sistema operativo como el de la maquina local , despues de esto podemos abrir el navegador y ya estara correindo la app.
## Vista de la aplicacion y uso

![](./images/vista-app.png)   
  
    
Para utilizar la app solo tenemos que introducir con numero la longitud y anchura del sepalo y del petalo y apretar el boton de predecir una ves echo lanzara una prediccion del modelo. Anexo un gif con un ejemplo de como se usa:

![](./images/explicacion.gif)
