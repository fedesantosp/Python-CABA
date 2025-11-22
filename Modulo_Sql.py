import sqlite3
#Crear Conexión y el archivo que almacenará la base de datos
conexion= sqlite3.connect("inventario.db")
cursor=conexion.cursor()


#Crear Tabla
def crear_tabla():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT NOT NULL
        )
    ''')
    conexion.commit()
    print("Tabla 'productos' creada con éxito")

#Crear Producto
def crear_producto(nombre, descripcion, cantidad, precio, categoria):
    if(buscar_Producto(nombre) is None):
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print("Producto creado con éxito")
    else:
        raise ValueError("El producto ya existe en la base de datos")


#Buscar Producto

#Buscar Categoria


def saliendo():
    conexion.close()
    
conexion.close()