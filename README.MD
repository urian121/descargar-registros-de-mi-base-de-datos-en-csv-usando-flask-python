### Crear un Sistema de Login de Usuario usando Sesiones con PHP y MySQL

#####  PASO 1, Crear mi entorno virtual
	python -m venv env 

##### PASO 2, Activar el entorno virtual ejecutando;
	. env/Scripts/activate

##### PASO 3, Ya dentro del entorno virtual instalar flask
	pip install flask

##### PASO 4, Instalar Python MySQL Connector, es una bibliote (Driver) para conectar Python con MySQL
	pip install mysql-connector-python

##### Crear/Actualizar el fichero requirements.txt:
	pip freeze > requirements.txt

(env)$ deactivate Para desactivar nuestro entono virtual

 IMPORTANTE, para correr el proyecto solo debes ejecutar el archivo

 requirements.txt con el comando;

pip install -r requirements.txt

en el mismo se encuentran todas las dependecias del proyecto.

 Nota: cuando vallas hacer una actualizacion del archivo requirements.txt
 debes estar dentro del entorno virtual pero no dentro de la carpera app solo en mi entorno.

##### corrar el proyecto luego de instalar todas las dependencias del mismo con:
python app.py

visitar la url: http://127.0.0.1:8050/



![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/descargar-registros-de-BD-en-CSV-con-Flask-Python.png)

