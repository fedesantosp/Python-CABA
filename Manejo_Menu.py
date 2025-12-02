from colorama import init, Fore, Back, Style
import Modulo_Sql as sql
init()


#Métodos Genericos:
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
            actualizar_productos()
        case 5:
            eliminar_producto()
        case 6:
            informe_stock()

#Crear Producto:
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
        print("Producto creado con éxito")
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
    cantOpciones=len(opciones_categoria)
    if(cantOpciones>0):
        mostrar_lista("Categorias:",opciones_categoria)
    cantOpciones+=1
    print(f"{Fore.YELLOW}{Style.BRIGHT}{cantOpciones}.{Style.RESET_ALL} {Fore.WHITE}Agregar Nueva Categoria{Style.RESET_ALL}")
    categoria=pedir_opcion(cantOpciones)
    if(categoria!=cantOpciones):
        
        return opciones_categoria[categoria-1]
    else:
        categoria = agregar_categoria()
        return(categoria)

"""Creacion y validacion de una Categoria"""
def agregar_categoria():
    categoria= input("Ingrese la nueva categoria: ").capitalize()
    while (not (len(categoria)>4 and categoria.isalpha)):
            categoria= input("Ingrese la nueva categoria: ").capitalize()
    return categoria
   

#Mostrar:
"""Funcion que muestra una lista de opciones y su nombre"""
def mostrar_lista (nombre_lista,lista):
   
    i=1
    print(f"\n{Back.BLUE}{Fore.WHITE}{Style.BRIGHT} {nombre_lista} {Style.RESET_ALL}") 
    for opcion in lista:
        print(f"{Fore.YELLOW}{Style.BRIGHT}{i}.{Style.RESET_ALL} {Fore.WHITE}{opcion}")
        i+=1
       
"""Muestra todos los productos registrados en la BD"""
def mostrar_productos():
    
    print("Lista de Productos:")
    productos = sql.mostrar_productos()
    for producto in productos:
        mostrar_objeto(producto)
        

"""Muestra un producto de la Base de Datos 
id[0] nombre[1], descripcion[2], cantidad[3], precio[4], categoria[5]"""
def mostrar_objeto(objeto):

    print(f"{Fore.WHITE}{Style.BRIGHT}Id:{objeto[0]}{Style.RESET_ALL}")

    print(f"{Fore.WHITE}{Style.BRIGHT}{objeto[1]}{Style.RESET_ALL}")
    
    print(f"{Fore.LIGHTBLACK_EX}Descripcion: {objeto[2]}{Style.RESET_ALL}")
    
    print(f"{Fore.YELLOW}Categoría: {Fore.WHITE}{objeto[5]}")
    
    print(f"{Fore.GREEN}Precio: ${objeto[4]:<10} {Fore.BLUE}Stock: {objeto[3]} u.")
    
    print(f"{Fore.CYAN}{'-'*40}{Style.RESET_ALL}")

"""Informe productos bajo Stock"""
def informe_stock():
    stock_minimo= pedir_opcion(10000,0,"Seleccione el stock maximo para generar el informe: ")
    productos_bajo_stock=sql.generar_informe_stock(stock_minimo)
    if(len(productos_bajo_stock)==0):
        print("No hay productos con ese stock o menos")
    else:
        print(f"Productos con stock menor a {stock_minimo}:")
        for producto in productos_bajo_stock:
            mostrar_objeto(producto) 

#Buscar:
"""Pide al usuario que determine el método de Busqueda y llama a dicho metodo"""
def buscar_producto():
    opciones=("Busqueda por ID: ","Busqueda por Nombre: ","Busqueda por Categoria: ")
    mostrar_lista("Métodos de Busqueda",opciones)
    opcion=pedir_opcion(3,1,"Eliga el método de busqueda deseado: ")
    match opcion:
        case 1:
            buscar_producto_id()
        case 2:
            buscar_producto_nombre()
        case 3:
            buscar_producto_categoria()

"""Pide un id para mostrar ese producto"""
def buscar_producto_id():
    try:
        id=int(input("Ingrese el ID que desea buscar:"))
        producto_buscado=sql.buscar_producto(id)
        if(producto_buscado is None):
            print("No existe un producto con ese Id")
        else:
            mostrar_objeto(producto_buscado)
    except ValueError:
        print("Error: Debe ingresar un número entero.")

"""Pide  un nombre de producto y lo busca en la BD"""
def buscar_producto_nombre():
    nombre=input("Ingrese el nombre del producto que desea buscar:").capitalize()
    producto_buscado=sql.buscar_producto_nombre(nombre)
    if(producto_buscado is None):
        print("No existe un producto con ese nombre")
    else:
        mostrar_objeto(producto_buscado)

"""Pide que se ingrese una categoria y trae todos los productos con esa categoria de la BD"""
def buscar_producto_categoria():
    categoria=input("Ingrese el nombre de la categoria que desea buscar:").capitalize()
    productos_buscado=sql.buscar_producto_categoria(categoria)
    if(len(productos_buscado)==0):
        print("No existe un producto con esa categoria")
    else:
        print(f"Productos con la categoria pedida: {categoria}")
        for producto in productos_buscado:
            mostrar_objeto(producto) 


#Actualizacion Registros:
"""Pide un ID de un producto para modificarlo"""
def actualizar_productos():
    campos=("Nombre","Descripcion","Cantidad","Precio","Categoria")
    try:
        id=int(input("Ingrese el ID del producto que desea modificar: "))
        producto_buscado=sql.buscar_producto(id)
        if(producto_buscado is None):
            print("No existe un producto con ese Id")
        else:
            print("Desea Modificar este producto?")
            mostrar_objeto(producto_buscado)
            eleccion=input("Si/No: ").capitalize()
            if(eleccion=="Si"):
                mostrar_lista("Campos Actualizables",campos)
                opcion=pedir_opcion(len(campos))
                match opcion:
                    case 1:
                        nombre=pedir_nombre()
                        sql.actualizar_nombre_producto(id,nombre)
                        print("Nombre Actualizado")
                    case 2:
                        descripcion=pedir_descripcion()
                        sql.actualizar_descripcion_producto(id,descripcion)
                        print("Descripcion Actualizada")
                    case 3:
                        cantidad=pedir_cantidad()
                        sql.actualizar_cantidad_producto(id,cantidad)
                        print("Cantidad Actualizada")
                    case 4:
                        precio=elegir_precio()
                        sql.actualizar_precio_producto(id,precio)
                        print("Precio Actualizado")
                    case 5:
                        categoria=elegir_categoria()
                        sql.actualizar_categoria_producto(id,categoria)
                        print("Categoria Actualizada")
            else:
                print(f"{Fore.RED}Actualizacion Cancelada{Style.RESET_ALL}")

    except ValueError:
        print("Error: Debe ingresar un número entero.")

"""Pide un Id y borra el producto asociado"""
def eliminar_producto():
    try:
        mostrar_productos()
        id=int(input("Ingrese el ID del producto que desea eliminar: "))
        producto_buscado=sql.buscar_producto(id)
        if(producto_buscado is None):
            print("No existe un producto con ese Id")
        else:
            sql.eliminar_producto(id)
            print(f"Producto {producto_buscado[1]} eliminado correctamente")
    except ValueError:
        print("Error: Debe ingresar un número entero.")