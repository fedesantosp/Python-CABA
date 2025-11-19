
#Funcion que muestra una lista de opciones y su nombre
def mostrar_lista (nombre_lista,lista):
    i=1
    print(nombre_lista,":")
    for opcion in lista:
        print(f"{i}- {opcion}")
        i+=1

#Funcion que pide un valor al usuario, asumiendo que es un numero.
#Lo valida dentro de las opciones de min y max recibidas por parametro.
# En caso contrario lo pide nuevamente.
def pedir_opcion(max,min=1,mensaje="Seleccione la opcion deseada para continuar: "):
    opcion_elejida=  input(f"\n{mensaje}")
    print()
    opcion= int(opcion_elejida)

    if valor_fuera_rango(opcion,min,max):
       return pedir_opcion(max,min)      

    return opcion
       
#Valida el número recibido por parametro y sus rangos, y devuelve si esta o no en rango 
def valor_fuera_rango(opcion,min=0,max=1000000):
    invalido=False
    if(opcion>max or opcion<min):
        invalido=True
    return invalido

#Activa la funcionalidad del menú  en base al número recibido por parametro.
#Llamando a su respectiva funcion
def activar_opcion(opcion):
    
     match opcion:
        case 1:
            agregar_producto()
        case 2:
            mostrar_productos()
        case 3:
            producto= input("Ingrese el nombre del Producto: ").capitalize()
            if ya_existe(producto):
                mostrar_objeto(buscar_producto(producto))
            else:
                print("No existe ese producto")
        case 4:
            eliminar_producto()

#Permite agregar un producto, pidiendo nombre, categoria y precio validando cada uno
def agregar_producto():
    nombre=pedir_nombre()
    categoria=elegir_categoria()
    precio=elegir_precio()

    lista_productos.append([nombre,categoria,precio])

#Pide un nombre al usuario y lo valida
def pedir_nombre():
    nombre=input("Ingrese el nombre del producto: ").capitalize()

    if ya_existe(nombre): 
        print("El producto ya se encuentra en la lista")
        return pedir_nombre()
        
    return nombre

#Pide al usuario que elija una categoria con un menu y sus numeros
def elegir_categoria():
    opciones_categoria= ("Bebida","Fruta","Verdura","Carne","Lácteo","Panadería","Congelado")
    mostrar_lista("Categorias:",opciones_categoria)
    categoria=pedir_opcion(len(opciones_categoria))-1
    return opciones_categoria[categoria]

#Pide al usuario que ingrese el precio y lo valida
def elegir_precio():
    precio_max=1000000
    precio= pedir_opcion(precio_max,1,"Seleccione el precio del producto: ")

    return precio

#comprueba si ya se agrego un producto con ese nombre
def ya_existe(nombre):
    ya_existe=False
    producto_buscado= buscar_producto(nombre)
    if   producto_buscado:
        ya_existe=True
    
    return ya_existe

#Itera toda la lista de productos y la muestra
def mostrar_productos():
    i=1
    print("Lista de Productos:")
    for producto in lista_productos:
        print(i,end="- ")
        mostrar_objeto(producto)
        i+=1

#Muestra un objeto de la lista con formato
def mostrar_objeto(objeto):
    print(f"Producto {objeto[0]} de la categoria {objeto[1]} tiene un precio de\t${objeto[2]}")

#Busca un producto usando el nombre
def buscar_producto(nombre):
    i=0
    producto_buscado=[]
    while i<len(lista_productos) and not producto_buscado:
        producto=lista_productos[i]
        nombre_producto=producto[0]
        if nombre_producto.capitalize() ==nombre:
            producto_buscado=lista_productos[i]
        i+=1

    return producto_buscado

def eliminar_producto():
    nombre= input("Ingrese el nombre del Producto a eliminar: ").capitalize()
    if ya_existe(nombre):
        print(f"Se elimino el producto {nombre} de la lista")
        producto_eliminado=buscar_producto(nombre)
        lista_productos.remove(producto_eliminado)
    else:
        print("No existe ese producto")

    

lista_productos=[["Manzana","Fruta",100],["Naranja","Fruta",230],["Brócoli","Verdura",50]
                 ,["Agua","Bebida",500],["Pollo","Carne",75]]

opcion=0
menu_inicio=("Agregar Producto","Mostrar Productos","Buscar producto","Eliminar Producto","Salir")

while opcion!=5:
    mostrar_lista("\nMenu de Opciones",menu_inicio)
    opcion=pedir_opcion(len(menu_inicio))   
    activar_opcion(opcion)
print("Saliendo del Programa...")


#Hay que probar el push