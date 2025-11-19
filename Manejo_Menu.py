from colorama import init, Fore, Back, Style

init()

#Funcion que muestra una lista de opciones y su nombre
def mostrar_lista (nombre_lista,lista):
    i=1
    print(nombre_lista,":")
    for opcion in lista:
        print(f"{Fore.RED}{i}-{Fore.GREEN+opcion}")
        i+=1