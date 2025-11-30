import sqlite3

"""Conecta/Crea la BD y genera la conexion"""
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

"""Busca y devuelve una lista de los productos con la Categoria recibida por parametro"""
def buscar_producto_categoria(categoria):
    cursor.execute('SELECT * FROM productos WHERE categoria=?',(categoria,))
    productos_encontrados= cursor.fetchall()
    return  productos_encontrados

"""Busca y devuelve la lista de categorias"""
def buscar_categorias():
    cursor.execute("""SELECT DISTINCT categoria FROM productos""")

    categorias_encontrado= cursor.fetchall()
    return [x[0] for x in categorias_encontrado]

"""Traer todos los objetos cargados para mostrarlos"""
def mostrar_productos():
    cursor.execute('''
    SELECT * 
    FROM productos
    ''')
    return cursor.fetchall()

"""Cuenta todos los registros en la BD, para determinar la cantidad de productos"""
def contar_productos():
    cursor.execute("SELECT COUNT(*) FROM productos")
    resultado = cursor.fetchone()     
    
    return resultado[0]

"""Recibe un ID y lo elimina de la BD"""
def eliminar_producto(id):
    producto_eliminado=buscar_producto(id)
    cursor.execute('DELETE FROM productos WHERE id=?',(id,))
    conexion.commit()

"""Recibe un ID y modifica el nombre"""
def actualizar_nombre_producto(id,nombre):
    cursor.execute('UPDATE productos SET nombre=? WHERE id=?',(nombre,id,))
    conexion.commit()

"""Recibe un ID y modifica la descripción"""
def actualizar_descripcion_producto(id,descripcion):
    cursor.execute('UPDATE productos SET descripcion=? WHERE id=?',(descripcion,id,))
    conexion.commit()

"""Recibe un ID y modifica la cantidad"""
def actualizar_cantidad_producto(id,cantidad):
    cursor.execute('UPDATE productos SET cantidad=? WHERE id=?',(cantidad,id,))
    conexion.commit()
    

"""Recibe un ID y modifica el precio"""
def actualizar_precio_producto(id,precio):
    cursor.execute('UPDATE productos SET precio=? WHERE id=?',(precio,id,))
    conexion.commit()
    

"""Recibe un ID y modifica la categoria"""
def actualizar_categoria_producto(id,categoria):
    cursor.execute('UPDATE productos SET categoria=? WHERE id=?',(categoria,id,))
    conexion.commit()
    

"""Genera una lista de productos segun el stock máximo recibido"""
def generar_informe_stock(stock):
    cursor.execute('SELECT * FROM productos WHERE cantidad<=?',(stock,))
    productos_bajo_stock=cursor.fetchall()
    return productos_bajo_stock

"""Cierra la conexion con la BD al cerrar el programa"""
def saliendo():
    conexion.close()
    
