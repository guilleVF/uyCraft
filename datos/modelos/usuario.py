from datos.base_de_datos import BaseDeDatos


def crear_usuario(nombre, apellido, nombre_usuario, clave, email, telefono, direccion):

    crear_usuario_sql = f""" INSERT INTO usuario(nombre, apellido, nombre_usuario, clave, email, telefono, direccion) 
                            VALUES ('{nombre}','{apellido}','{nombre_usuario}','{clave}','{email}','{telefono}','{direccion}')
                        """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_usuario_sql)

def login_usuario(nombre_usuario, clave):

    login_usuario_sql = f""" SELECT * FROM usuario WHERE nombre_usuario = '{nombre_usuario}' AND clave = '{clave}' 
                        """

    bd = BaseDeDatos()
    resultado = bd.ejecutar_sql(login_usuario_sql)
    return resultado



