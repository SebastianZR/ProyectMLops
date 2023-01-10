FROM python:3.8.4-slim-buster

#Creamos el directorio 
WORKDIR /app
COPY . /app

#Instalamos las dependencias
COPY  requirements.txt ./

#Instalamos las dependencias
RUN pip install -r requirements.txt


CMD [ "python","main.py"]
