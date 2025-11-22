import Manejo_Menu as menu
import Modulo_Sql as sql
from colorama import init, Fore, Back, Style
init()
opcion=0
menu_inicio=("Agregar Producto","Mostrar Productos","Buscar producto","Eliminar Producto","Salir")


while opcion!=5:
        menu.mostrar_lista("\nMenu de Opciones",menu_inicio)
        opcion=menu.pedir_opcion(len(menu_inicio))   
        menu.activar_opcion(opcion)

print(f"{Fore.RED}Saliendo del Programa...")
sql.saliendo()
