from datos.base_de_datos import BaseDeDatos


def crear_articulo(descripcion, titulo, tiempo_entrega, precio, id_productor, id_categoria):

    crear_articulo_sql = f""" INSERT INTO articulo(descripcion, titulo, tiempo_entrega, precio,  id_productor, id_categoria) 
                            VALUES ('{descripcion}','{titulo}','{tiempo_entrega}','{precio}','{id_productor}','{id_categoria}')
                        """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_articulo_sql)


def obtener_articulo(id_articulo):

    obtener_articulo_sql = f""" SELECT * FROM articulo WHERE id_articulo = {id_articulo}
                            """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(obtener_articulo_sql)


def modificar_articulo(id_articulo, titulo, descripcion, tiempo_entrega, precio, id_productor, id_categoria):

    modificar_articulo_sql = f""" UPDATE articulo SET titulo = '{titulo}', descripcion = '{descripcion}', tiempo_entrega = '{tiempo_entrega}', 
                                    precio = '{precio}', id_productor = '{id_productor}', id_categoria = '{id_categoria}'
                             """
    bd = BaseDeDatos()
    bd.ejecutar_sql(modificar_articulo_sql)


def eliminar_artiulo(id_articulo):

    eliminar_articulo_sql = f""" DELETE FROM articulo WHERE id_articulo = '{id_articulo}'
                            """

    bd = BaseDeDatos()
    bd.ejecutar_sql(eliminar_articulo_sql)

def listar_articulos():

    listar_articulos_sql = """ SELECT * FROM articulo
                            """
    bd = BaseDeDatos()
    return bd.ejecutar_sql(listar_articulos_sql)