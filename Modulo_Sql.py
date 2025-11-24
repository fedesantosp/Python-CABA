import sqlite3
#Crear Conexión y el archivo que almacenará la base de datos
conexion= sqlite3.connect("inventario.db")
cursor=conexion.cursor()


"""Crea la  Tabla de productos, si no se creo previamente"""
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
    if(buscar_producto(nombre) is None):
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print("Producto creado con éxito")
    else:
        raise ValueError("El producto ya existe en la base de datos")


"""Busca en la BD un prodcuto basado en el nombre, devuelve el primero que encuentra"""
def buscar_producto(nombre_buscado):
    cursor.execute('''
    SELECT * FROM productos
    WHERE nombre = ?
    ''',(nombre_buscado))

    producto_encontrado= cursor.fetchone
    return producto_encontrado

"""Busca y devuelve la lista de ecategorias"""
def buscar_categorias():
    cursor.execute("""SELECT categoria FROM productos""")

    categorias_encontrado= cursor.fetchall
    return categorias_encontrado

"""Traer todos los objetos cargados para mostrarlos"""
def mostrar_productos():
    cursor.execute('''
    SELECT * 
    FROM productos
    ''')
    return cursor.fetchall()

def saliendo():
    conexion.close()
    
conexion.close()