Consignas Entrega Final:

Requerimientos

-Base de datos: Crear una base de datos llamada 'inventario.db' para almacenar los datos de los productos.

La tabla 'productos' debe contener las siguientes columnas:✅ Hecho
-'id': Identificador único del producto (clave primaria, autoincremental).
-'nombre': Nombre del producto (texto, no nulo).
-'descripcion': Breve descripción del producto (texto).
-'cantidad': Cantidad disponible del producto (entero, no nulo).
-'precio': Precio del producto (real, no nulo).
-'categoria': Categoría a la que pertenece el producto (texto).

Funcionalidades de la aplicación:

-Registrar nuevos productos.  ✅ Hecho
-Visualizar datos de los productos registrados. ✅ Hecho
-Actualizar datos de productos, mediante su ID. ✅ Hecho
-Eliminación de productos, mediante su ID. ✅ Hecho
-Búsqueda de productos:
    Por el ID ✅ Hecho
    Por los campos nombre ✅ Hecho
    Por los campos categoría.✅ Hecho
-Reporte de productos que tengan una cantidad igual o inferior a un límite especificado por el usuario o usuaria. ❌ Falta

Interfaz de usuario: ✅ Hecho

Implementar una interfaz de usuario básica, para interactuar con la base de datos a través de la terminal.
La interfaz debe incluir un menú principal con las opciones necesarias para acceder a cada funcionalidad descrita anteriormente.
Opcional: Utilizar el módulo 'colorama' para mejorar la legibilidad y experiencia de usuario en la terminal, añadiendo colores a los mensajes y opciones
