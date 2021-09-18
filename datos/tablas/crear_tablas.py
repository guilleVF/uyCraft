import sqlite3

#Creamos y nos conectamos a la base de datos
con = sqlite3.connect('/home/guillermo/PycharmProjects/uyCraft/datos/uyCraft.db')

#Creamos un objeto de tipo cursor
c = con.cursor()

try:
    con.execute("""CREATE TABLE usuario(
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono INTEGER NOT NULL,
                email TEXT NOT NULL UNIQUE,
                foto_perfil BLOB,
                nombre_usuario TEXT NOT NULL UNIQUE,
                clave TEXT NOT NULL 
                )""")

    con.execute("""CREATE TABLE productor(
                id_productor INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono INTEGER NOT NULL,
                email TEXT NOT NULL UNIQUE,
                nombre_usuario TEXT NOT NULL UNIQUE,
                clave TEXT NOT NULL
                )""")

    con.execute("""CREATE TABLE articulo(
                id_articulo INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                tiempo_entrega TEXT,
                rating REAL DEFAULT 1,
                precio REAL NOT NULL,
                id_productor INTEGER NOT NULL,
                id_categoria INTEGER NOT NULL,
                FOREIGN KEY(id_productor) REFERENCES productor(id_productor),
                FOREIGN KEY(id_categoria) REFERENCES categoria(id_categoria)
                )""")

    con.execute("""CREATE TABLE categoria(
                id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_categoria TEXT NOT NULL
                )""")

    con.execute("""CREATE TABLE favorito(
                id_favorito INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                id_articulo INTEGER NOT NULL,
                FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
                FOREIGN KEY(id_articulo) REFERENCES item(id_articulo)
                )""")

    con.execute("""CREATE TABLE orden(
                id_orden INTEGER PRIMARY KEY AUTOINCREMENT,
                cantidad INTEGER NOT NULL DEFAULT 1,
                id_productor INTEGER NOT NULL,
                id_usuario INTEGER NOT NULL,
                precio REAL NOT NULL,
                id_articulo INTEGER NOT NULL,
                FOREIGN KEY(id_productor) REFERENCES productor(id_productor),
                FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
                FOREIGN KEY(precio) REFERENCES item(precio),
                FOREIGN KEY(id_articulo) REFERENCES item(id_articulo)
                )""")

    con.execute("""CREATE TABLE curso(
                id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_curso TEXT NOT NULL,
                texto TEXT NOT NULL
                )""")

    con.execute("""CREATE TABLE curso_productor(
                id_curso_productor INTEGER PRIMARY KEY AUTOINCREMENT,
                id_curso INTEGER NOT NULL,
                id_productor INTEGER NOT NULL,
                FOREIGN KEY(id_curso) REFERENCES curso(id_curso),
                FOREIGN KEY(id_productor) REFERENCES productor(id_productor)
                )""")

    print('Tablas creadas correctamente.')

except Exception as e:
    print(f'Error al crear tablas: {e}', e)

con.close()

