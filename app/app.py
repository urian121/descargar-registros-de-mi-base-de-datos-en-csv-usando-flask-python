from flask import Flask, request, render_template, make_response
import csv  # Libreria para Exportar datos en formato CSV
from connBD import *  # Conexion a BD

app = Flask(__name__)


# Mi decorador Home
@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/downloader-csv', methods=['GET'])
def procesarDescarga():
    if request.method == 'GET':
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
        csv_data = 'Id,Usuario,Nombre,Sexo,Nivel,Email,Telefono,Marca,Compañia,Saldo,Estatus\n'
        for persona in listaRegistros:
            csv_data += f"{persona['id_persona']},"
            csv_data += f"{persona['usuario']},"
            csv_data += f"{persona['nombre']},"
            csv_data += f"{persona['sexo']},"
            csv_data += f"{persona['nivel']},"
            csv_data += f"{persona['email']},"
            csv_data += f"{persona['telefono']},"
            csv_data += f"{persona['marca']},"
            csv_data += f"{persona['company']},"
            csv_data += f"{persona['saldo']},"
            csv_data += f"{persona['activo']}\n"

        # Crear una respuesta y establecer encabezados
        response = make_response(csv_data)
        response.headers['Content-Disposition'] = 'attachment; filename=my_data.csv'
        response.headers['Content-Type'] = 'text/csv'

        return response
    else:
        return 'Método HTTP incorrecto'


# Corriendo la aplicación
if __name__ == "__main__":
    app.run(debug=True, port=8050)
