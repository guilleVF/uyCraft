from datos.modelos import articulo as modelo_articulo

def crear_articulo(titulo, descripcion, tiempo_entrega, precio, id_productor, id_categoria):
    modelo_articulo.crear_articulo(titulo, descripcion, tiempo_entrega, precio, id_productor, id_categoria)

def obtener_articulo(id_articulo):
    return modelo_articulo.obtener_articulo(id_articulo)

def eliminar_articulo(id_articulo):
    modelo_articulo.eliminar_artiulo(id_articulo)

def modificar_articulo(id_articulo, titulo, descripcion, tiempo_entrega, precio, id_productor, id_categoria):
    modelo_articulo.modificar_articulo(id_articulo, titulo, descripcion, tiempo_entrega, precio, id_productor, id_categoria)

def listar_articulo():
    return modelo_articulo.listar_articulos()