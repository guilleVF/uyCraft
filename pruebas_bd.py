from datos.base_de_datos import BaseDeDatos

bd = BaseDeDatos()


# bd.ejecutar_sql('DELETE FROM usuario')
# bd.ejecutar_sql('DELETE FROM articulo')

print(bd.ejecutar_sql('SELECT * FROM articulo'))
print(bd.ejecutar_sql('SELECT * FROM usuario'))

