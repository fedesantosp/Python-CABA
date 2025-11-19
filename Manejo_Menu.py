from colorama import init, Fore, Back, Style
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

        print(f"{color}{fondo}{i}-{opcion}{Style.RESET_ALL}")
        i+=1
        fondo=Back.RESET
        color=Fore.WHITE

"""Funcion que pide un valor al usuario, asumiendo que es un numero.
Lo valida dentro de las opciones de min y max recibidas por parametro.
En caso contrario lo pide nuevamente.
"""
def pedir_opcion(max,min=1,mensaje="Seleccione la opcion deseada para continuar: "):
    import Pre_Entrega as entrega   # import tardío para evitar import circular
    while True:
        opcion_elejida = input(f"\n{mensaje}")
        print()
        try:
            opcion = int(opcion_elejida)
        except ValueError:
            print("Ingrese un número válido.")
            continue

        if entrega.valor_fuera_rango(opcion, min, max):
           print(f"Ingrese un valor entre {min} y {max}.")
           continue

        return opcion

"""Activa la funcionalidad del menú  en base al número recibido por parametro.
Llamando a su respectiva funcion 
"""
def activar_opcion(opcion):
    import Pre_Entrega as entrega   # import tardío para evitar import circular
    match opcion:
        case 1:
            entrega.agregar_producto()
        case 2:
            entrega.mostrar_productos()
        case 3:
            producto = input("Ingrese el nombre del Producto: ").capitalize()
            if entrega.ya_existe(producto):
                entrega.mostrar_productos(entrega.buscar_producto(producto))
            else:
                print("No existe ese producto")
        case 4:
            entrega.eliminar_producto()