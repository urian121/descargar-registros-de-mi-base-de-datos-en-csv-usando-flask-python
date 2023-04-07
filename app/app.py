from flask import Flask, render_template, make_response
import csv  # Libreria para Exportar datos en formato CSV
from connBD import *
app = Flask(__name__)


# Mi decorador Home
@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/downloader-csv', methods=['GET', 'POST'])
def procesarDescarga():
    conexion_MySQLdb = connectionBD()  # Hago instancia a mi conexion desde la funcion
    mycursor = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = ("SELECT * FROM personas")
    mycursor.execute(querySQL)
    listaRegistros = mycursor.fetchall()
    mycursor.close()  # cerrrando conexion SQL
    conexion_MySQLdb.close()  # cerrando conexion de la BD

    '''  
     En este ejemplo, he usado la variable csv_data += para agregar cada registro de la lista
     a una cadena de texto en formato CSV. 
    '''
    # Crear una cadena de texto en formato CSV el cual será el encabezado
    csv_data = 'Id,Usuario,Nombre,Sexo,Nivel,Email,Telefono,Marca,Compañia,Saldo,Activo\n'
    for persona in listaRegistros:
        csv_data += f"{persona['id_persona']}\,"
        f"{persona['usuario']},{persona['nombre']},\,"
        f"{persona['sexo']},\,"
        f"{persona['nivel']},\,"
        f"{persona['email']},\,"
        f"{persona['telefono']},\,"
        f"{persona['marca']},\,"
        f"{persona['company']},\,"
        f"{persona['saldo']},\,"
        f"{persona['activo']}\n"

    # Crear una respuesta y establecer encabezados
    response = make_response(csv_data)
    response.headers['Content-Disposition'] = 'attachment; filename=my_data.csv'
    response.headers['Content-Type'] = 'text/csv'

    return response


# Corriendo la aplicación
if __name__ == "__main__":
    app.run(debug=True, port=8050)
