from datos.modelos import usuario as modelo_usuario
from datos.modelos import productor as modelo_productor

def crear_usuario(nombre, apellido, nombre_usuario, clave, email, telefono, direccion):
    modelo_usuario.crear_usuario(nombre, apellido, nombre_usuario, clave, email, telefono, direccion)

def login_usuario(nombre_usuario, clave):
    resultado = modelo_usuario.login_usuario(nombre_usuario, clave)
    return resultado

def listar_usuarios():
    return modelo_usuario.listar_usuarios()

def crear_productor(nombre, apellido, nombre_usuario, clave, email, telefono, direccion):
    modelo_productor.crear_productor(nombre, apellido, nombre_usuario, clave, email, telefono, direccion)
