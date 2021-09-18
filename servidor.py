from flask import Flask, request
from servicios.autenticacion import autenticacion
from servicios.articulo import articulo
import json

app = Flask(__name__)

#Creación de Usuario
@app.route('/usuario',methods=['POST'])
def crear_usuario():

    datos_usuario = request.get_json()

    if "nombre" not in datos_usuario:
        return "El nombre es requerido", 412
    if "apellido" not in datos_usuario:
        return "El apellido es requerido", 412
    if "email" not in datos_usuario:
        return "El email es requerido", 412
    if "nombre_usuario" not in datos_usuario:
        return "El email es requerido", 412
    if "clave" not in datos_usuario:
        return "La clave es requerida", 412

    autenticacion.crear_usuario(datos_usuario['nombre'],datos_usuario['apellido'],datos_usuario['nombre_usuario'],datos_usuario['clave'],
                                datos_usuario['email'],datos_usuario['telefono'], datos_usuario['direccion'])
    return 'OK', 200

#Login de usuario
@app.route('/login_usuario',methods=['POST'])
def login_usuario():

    datos_usuario = request.get_json()

    if "nombre_usuario" not in datos_usuario:
        return "El nombre de usuario es requerido", 412
    if "clave" not in datos_usuario:
        return "La clave es requerida", 412

    resultado = autenticacion.login_usuario(datos_usuario['nombre_usuario'],datos_usuario['clave'])
    if resultado:
        return 'OK, bienvenido.', 200
    else:
        return 'Usuario y/o contraseña incorrectos', 404

#Listado de Usuarios
@app.route('/usuario', methods=['GET'])
def listar_usuario():

    resultado = autenticacion.listar_usuarios()
    return json.dumps(resultado)

#Creación de artículo
@app.route('/crear_articulo', methods=['POST'])
def crear_articulo():

    datos_articulo = request.get_json()

    if "titulo" not in datos_articulo:
        return "El título es requerido", 412
    if "precio" not in datos_articulo:
        return "El precio es requerido", 412

    articulo.crear_articulo(datos_articulo['titulo'],datos_articulo['descripcion'],datos_articulo['tiempo_entrega'],datos_articulo['precio'],
                            datos_articulo['id_productor'],datos_articulo['id_categoria'])
    return 'OK', 200

#Obtener artículo
@app.route('/articulo/<id_articulo>', methods=['GET'])
def obtener_articulo(id_articulo):

    resultado = articulo.obtener_articulo(id_articulo)
    return json.dumps(resultado)

#Modificacion de artículo
@app.route('/articulo/<id_articulo>',methods=['PUT'])
def modificar_articulo(id_articulo):

    datos_articulo = request.get_json()
    articulo.modificar_articulo(id_articulo, datos_articulo['titulo'],datos_articulo['descripcion'],datos_articulo['tiempo_entrega'],datos_articulo['precio'],
                            datos_articulo['id_productor'],datos_articulo['id_categoria'])
    return 'OK', 200

#Borrado de articulo
@app.route('/articulo/<id_articulo>', methods=['DELETE'])
def eliminar_articulo(id_articulo):

    articulo.eliminar_articulo(id_articulo)
    return 'OK',200

#Listado de articulos
@app.route('/articulo',methods=['GET'])
def listar_articulos():
    return json.dumps(articulo.listar_articulo())









if __name__ == '__main__':
    app.debug = True
    app.run()