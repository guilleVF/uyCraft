from flask import Flask, request
from servicios.autenticacion import autenticacion

app = Flask(__name__)


@app.route('/usuarios',methods=['POST'])
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

@app.route('/login_usuario',methods=['POST'])
def login_usuario():

    datos_usuario = request.get_json()

    if "nombre_usuario" not in datos_usuario:
        return "El nombre de usuario es requerido", 412
    if "clave" not in datos_usuario:
        return "La clave es requerida", 412

    resultado = autenticacion.login_usuario(datos_usuario['nombre_usuario'],datos_usuario['clave'])
    if resultado:
        return 'OK', 200
    else:
        return 'Wrong Credentials', 412




if __name__ == '__main__':
    app.debug = True
    app.run()