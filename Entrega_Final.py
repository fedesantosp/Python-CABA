import Manejo_Menu as menu
import Modulo_Sql as sql
from colorama import init, Fore, Back, Style
init()


opcion=0
menu_inicio=("Agregar Producto","Mostrar Productos","Buscar producto","Actualizar Producto","Eliminar Producto","Reporte Bajo Stock","Salir")
sql.crear_tabla()

try:
        while opcion!=7:
                menu.mostrar_lista("\nMenu de Opciones",menu_inicio)
                opcion=menu.pedir_opcion(len(menu_inicio))   
                menu.activar_opcion(opcion)
except Exception as e:
        print(f"{Fore.RED}Ocurrió un error: {e}")
finally:
        print(f"{Fore.RED}Saliendo del Programa...")
        sql.saliendo()

        