#SISTEMA DE GESTIÓN DE INVENTARIO - ENTREGA FINAL PYTHON

AUTOR: Federico Santos Piacente
CURSO: Talento Tech - Inicialización a la Programación con Python

DESCRIPCIÓN:
Este proyecto es una aplicación de consola para la gestión de inventario de productos. 
Utiliza una base de datos SQLite para la persistencia de la información y permite 
realizar todas las operaciones CRUD (Crear, Leer, Actualizar, Eliminar), además de 
búsquedas avanzadas y reportes de stock.

CARACTERÍSTICAS PRINCIPALES:
---------------------------
1. Base de Datos Relacional:
   - Uso de SQLite3.
   - Tabla 'productos' con campos validados (ID, nombre, descripción, cantidad, precio, categoría).

2. Funcionalidades (CRUD):
   - Registro de nuevos productos con validación de datos.
   - Visualización del listado completo.
   - Actualización de campos específicos de un producto.
   - Eliminación segura de productos por ID.

3. Consultas Avanzadas:
   - Búsqueda por ID, Nombre y Categoría.
   - REPORTE DE BAJO STOCK: Filtra productos con cantidad igual o menor a un límite ingresado.

4. Seguridad y Buenas Prácticas:
   - Prevención de Inyección SQL mediante el uso de consultas parametrizadas (?).
   - Manejo de errores con bloques try-except para evitar cierres inesperados.
   - Modularización del código (Separación en Main, Menú y Módulo SQL).

REQUISITOS DEL SISTEMA:
-----------------------
- Python 3.x
- Librería externa: colorama

INSTALACIÓN Y EJECUCIÓN:
------------------------
1. Asegúrese de tener Python instalado.
2. Instale las dependencias necesarias ejecutando:
   pip install colorama
3. Ejecute el archivo principal:
   python main.py

ESTRUCTURA DE ARCHIVOS:
-----------------------
* main.py         -> Punto de entrada del programa. Controla el flujo principal.
* Manejo_Menu.py  -> Contiene la lógica de interacción con el usuario y validaciones de input.
* Modulo_Sql.py   -> Maneja la conexión a la BD y todas las consultas SQL.
* inventario.db   -> Archivo de base de datos (se crea automáticamente al iniciar).

NOTAS ADICIONALES:
------------------
El sistema valida que los precios no sean negativos y que los nombres de productos 
tengan una longitud mínima para asegurar la consistencia de los datos.