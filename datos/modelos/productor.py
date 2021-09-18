from datos.base_de_datos import BaseDeDatos


def crear_productor(nombre, apellido, nombre_usuario, clave, email, telefono, direccion):

    crear_productor_sql = f""" INSERT INTO productor(nombre, apellido, nombre_usuario, clave, email, telefono, direccion) 
                            VALUES ('{nombre}','{apellido}','{nombre_usuario}','{clave}','{email}','{telefono}','{direccion}')
                        """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_productor_sql)

