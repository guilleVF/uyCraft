from datos.base_de_datos import BaseDeDatos


def crear_articulo(descripcion, tiempo_entrega, rating, precio,  id_productor, id_categoria):

    crear_articulo_sql = f""" INSERT INTO articulo(descripcion, tiempo_entrega, rating, precio,  id_productor, id_categoria) 
                            VALUES ('{descripcion}','{tiempo_entrega}','{rating}','{precio}','{id_productor}','{id_categoria}')
                        """
    bd = BaseDeDatos()
    bd.ejecutar_sql(crear_articulo_sql)