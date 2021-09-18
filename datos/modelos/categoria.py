from datos.base_de_datos import BaseDeDatos

bd = BaseDeDatos()

bd.ejecutar_sql("INSERT INTO categoria ('nombre_categoria') VALUES ('ceramica')")