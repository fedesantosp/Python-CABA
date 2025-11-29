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

"""Recibe los datos ya validados para crear un producto. Comprueba que el nombre no exista ya en la BD"""
def crear_producto(nombre, descripcion, cantidad, precio, categoria):
    if(buscar_producto_nombre(nombre) is None):
        cursor.execute('''
            INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
            VALUES (?, ?, ?, ?, ?)
        ''', (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print("Producto creado con éxito")
    else:
        raise ValueError("El producto ya existe en la base de datos")

"""Busca en la BD un prodcuto basado en el nombre, devuelve el primero que encuentra"""
def buscar_producto_nombre(nombre_buscado):
    cursor.execute('''
    SELECT * FROM productos
    WHERE nombre = ?
    ''',(nombre_buscado,))

    producto_encontrado= cursor.fetchone()
    return producto_encontrado

"""Busca en la BD un prodcuto basado en el ID, devuelve el primero que encuentra"""
def buscar_producto(id):
    cursor.execute('SELECT * FROM productos WHERE id=?',(id,))
    producto_encontrado= cursor.fetchone()
    return producto_encontrado

def buscar_producto_categoria(categoria):
    cursor.execute('SELECT * FROM productos WHERE categoria=?',(categoria,))
    productos_encontrados= cursor.fetchall()
    return productos_encontrados

"""Busca y devuelve la lista de categorias"""
def buscar_categorias():
    cursor.execute("""SELECT categoria FROM productos""")

    categorias_encontrado= cursor.fetchall()
    return categorias_encontrado

"""Traer todos los objetos cargados para mostrarlos"""
def mostrar_productos():
    cursor.execute('''
    SELECT * 
    FROM productos
    ''')
    return cursor.fetchall()

def contar_productos():
    cursor.execute("SELECT COUNT(*) FROM productos")
    resultado = cursor.fetchone()     
    
    return resultado[0]

def saliendo():
    conexion.close()
    
