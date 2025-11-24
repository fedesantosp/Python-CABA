from colorama import init, Fore, Back, Style
import Modulo_Sql as sql
init()

"""Funcion que muestra una lista de opciones y su nombre"""
def mostrar_lista (nombre_lista,lista):
    fondo=Back.YELLOW
    color=Fore.BLACK
    i=1
    print(f"{fondo}{color}{nombre_lista} :{Style.RESET_ALL}")
    for opcion in lista:
        fondo=Back.RESET
        color=Fore.WHITE
        if(i==5):
            fondo=Back.RED
            color=Fore.BLACK

        print(f"{color}{fondo}{i}-{opcion[0]}{Style.RESET_ALL}")
        i+=1
        fondo=Back.RESET
        color=Fore.WHITE

"""Funcion que pide un valor al usuario, asumiendo que es un numero.
Lo valida dentro de las opciones de min y max recibidas por parametro.
En caso contrario lo pide nuevamente.
"""
def pedir_opcion(max,min=1,mensaje="Seleccione la opcion deseada para continuar: "):
    
    while True:
        opcion_elejida = input(f"\n{mensaje}\n")
        
        try:
            opcion = int(opcion_elejida)
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if valor_fuera_rango(opcion, min, max):
           print(f"Ingrese un valor entre {min} y {max}.")
           continue

        return opcion

"""Valida el número recibido por parametro y sus rangos, y devuelve si esta o no en rango """
def valor_fuera_rango(opcion,min=0,max=1000000):
    invalido=False
    if(opcion>max or opcion<min):
        invalido=True
    return invalido





"""Activa la funcionalidad del menú  en base al número recibido por parametro.
Llamando a su respectiva funcion 
"""
def activar_opcion(opcion):
    match opcion:
        case 1:
            agregar_producto()
        case 2:
            mostrar_productos()
        case 3:
           buscar_producto()
        case 4:
            eliminar_producto()




"""Permite agregar un producto, pidiendo nombre, descripcion, cantidad, precio, categoria, validando que ninguno sea
nulo o incorrecto.
Luego llama a otro metodo para agregar el producto a la BD, donde previamente se comprueba que no este ya agregado.
"""
def agregar_producto():
    try:
        nombre=pedir_nombre()
        descripcion=pedir_descripcion()
        cantidad=pedir_cantidad()
        precio=elegir_precio()
        categoria=elegir_categoria()
        sql.crear_producto(nombre, descripcion, cantidad, precio, categoria)
    except ValueError as e:
        print(e)
   

"""Pide un nombre al usuario y lo valida para que no sea nulo.
    nombre=String"""
def pedir_nombre():
    nombre=input("Ingrese el nombre del producto: ").capitalize()

    if not(len(nombre) > 3):
        raise ValueError("El nombre del producto debe tener más de 3 letras y solo contener letras.")        
        
    return nombre

"""Pide al usuario que ingrese una descripcion y la valida para que no sea nula.
    descripcion=String"""
def pedir_descripcion():
    descripcion=input("Ingrese la descripcion del producto: ")

    if not(len(descripcion) > 5):
        raise ValueError("La descripcion del producto debe tener más de 5 caracteres.")        
        
    return descripcion

"""Pide al usuario que ingrese una cantidad y la valida usando otro metodo (pedir_opcion).
    cantidad=Integer"""
def pedir_cantidad():
    cantidad_max=3000
    cantidad= pedir_opcion(cantidad_max,1,"Seleccione la cantidad de stock del producto: ")

    return cantidad

"""Pide al usuario que ingrese un precio y lo valida usando otro metodo (pedir_opcion).
    precio=Float"""
def elegir_precio():
    precio_max=10000
    precio= pedir_opcion(precio_max,1,"Seleccione el precio del producto: ")

    return precio

"""Muestra todas las categorias previamente cargadas y la opcion de craer una nueva."""
def elegir_categoria():
    opciones_categoria= sql.buscar_categorias()
    categoria
    cantOpciones=len(opciones_categoria)
    if(cantOpciones>0):
        mostrar_lista("Categorias:",opciones_categoria)
    cantOpciones+=1
    print(f"{len(cantOpciones)} -Agregar Nueva Categoria")
    categoria=pedir_opcion(cantOpciones)
    if(categoria!=cantOpciones):
        
        return opciones_categoria[categoria-1]
    else:
        categoria = agregar_categoria()
        return(categoria)

"""Creacion y validacion de una Categoria"""
def agregar_categoria():
    categoria= input("Ingrese la nueva categoria: ").capitalize
    while (not (len(categoria)>4 and categoria.isalpha)):
            categoria= input("Ingrese la nueva categoria: ").capitalize
    return categoria
   



#Itera toda la lista de productos y la muestra
def mostrar_productos():
    i=1
    print("Lista de Productos:")
    productos = sql.mostrar_productos()
    for producto in productos:
        print(i,end="- ")
        mostrar_objeto(producto)
        i+=1



"""Muestra un producto de la Base de Datos 
nombre[0], descripcion[1], cantidad[2], precio[3], categoria[4]"""
def mostrar_objeto(objeto):
    print(f"Producto: {objeto[0]} de la categoria {objeto[4]}tiene un precio de\t${objeto[3]} y cuenta con un stock de {objeto[2]}")
    print(f"Descripcion: {objeto[1]}")

#Busca un producto usando el nombre
def buscar_producto_nombre(nombre):
  

    return producto_buscado

#Busca un producto usando el Id
def buscar_producto_id():
  

    return producto_buscado

#Busca un producto usando la categoria
def buscar_producto_categoria(categoria):
  

    return producto_buscado


def eliminar_producto():
    nombre= input("Ingrese el nombre del Producto a eliminar: ").capitalize()
    if ya_existe(nombre):
        print(f"Se elimino el producto {nombre} de la lista")
        producto_eliminado=buscar_producto(nombre)
        lista_productos.remove(producto_eliminado)
    else:
        print("No existe ese producto")