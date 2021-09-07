import sqlite3

#Creamos y nos conectamos a la base de datos
con = sqlite3.connect('uyCraft.db')

#Creamos un objeto de tipo cursor
c = con.cursor()


con.execute("""CREATE TABLE usuario(
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            direccion TEXT NOT NULL,
            telefono INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE,
            foto_perfil BLOB,
            nombre_usuario TEXT NOT NULL UNIQUE,
            contraseña TEXT NOT NULL 
            )""")

con.execute("""CREATE TABLE productor(
            id_productor INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            direccion TEXT NOT NULL,
            telefono INTEGER NOT NULL,
            email TEXT NOT NULL UNIQUE,
            nombre_usuario TEXT NOT NULL UNIQUE,
            contraseña TEXT NOT NULL
            )""")

con.execute("""CREATE TABLE item(
            id_item INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT,
            tiempo_entrega TEXT,
            imagenes BLOB,
            comentarios TEXT,
            rating REAL DEFAULT 1,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            id_productor INTEGER NOT NULL,
            FOREIGN KEY(id_productor) REFERENCES productor(id_productor)
            )""")


con.execute("""CREATE TABLE favorito(
            id_favorito INTEGER PRIMARY KEY AUTOINCREMENT,
            id_usuario INTEGER NOT NULL,
            id_item INTEGER NOT NULL,
            FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
            FOREIGN KEY(id_item) REFERENCES item(id_item)
            )""")

con.execute("""CREATE TABLE orden(
            id_orden INTEGER PRIMARY KEY AUTOINCREMENT,
            cantidad INTEGER NOT NULL DEFAULT 1,
            id_productor INTEGER NOT NULL,
            id_usuario INTEGER NOT NULL,
            precio REAL NOT NULL,
            id_item INTEGER NOT NULL,
            FOREIGN KEY(id_productor) REFERENCES productor(id_productor),
            FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
            FOREIGN KEY(precio) REFERENCES item(precio),
            FOREIGN KEY(id_item) REFERENCES item(id_item)
            )""")

con.execute("""CREATE TABLE chat(
            id_chat INTEGER PRIMARY KEY AUTOINCREMENT,
            contenido TEXT NOT NULL,
            id_item INTEGER NOT NULL,
            id_usuario INTEGER NOT NULL,
            id_productor INTEGER NOT NULL,
            FOREIGN KEY(id_item) REFERENCES item(id_item),
            FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
            FOREIGN KEY(id_productor) REFERENCES productor(id_productor)
            )""")

con.execute("""CREATE TABLE curso(
            id_curso INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_curso TEXT NOT NULL,
            texto TEXT NOT NULL,
            imagenes BLOB,
            videos BLOB
            )""")

#Puedo poner imagenes y videos en la base de datos?
#Puedo usar una FK externa como PK?
#Necesito una tabla intermedia para definir relacion entre 2 entidades?
#Como hago una consulta con relacion a una FK? Los datos se copian de una tabla a otra?