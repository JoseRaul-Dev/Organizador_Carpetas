# Organizador automático de carpetas
Organizador automático de carpetas desarrollado en Python utilizando la librería **Rich** para mejorar la presentación de la aplicación en consola.

## Descripción
Este programa permite al usuario introducir una carpeta de origen y otra de destino para clasificar automáticamente los archivos según su extensión, incluyendo los archivos que se encuentran en subcarpetas.
Al finalizar, se muestran dos informes:
- El primero muestra los archivos movidos, el tamaño total y los archivos que quedan en el origen y en el destino.
- El segundo muestra los movimientos realizados entre la carpeta de origen y la carpeta de destino.

## Funcionalidades
- Solicitud de las rutas de origen y destino.
- Validación de las rutas introducidas.
- Comprobación de que las carpetas no sean iguales ni estén una dentro de otra.
- Comprobación de que la carpeta de origen no esté vacía.
- Recorrido de carpetas y subcarpetas mediante recursividad.
- Clasificación de archivos según su extensión.
- Creación automática de carpetas para cada extensión (si un archivo no tiene extensión, se crea la carpeta `sin extension`).
- Evita sobrescribir archivos con el mismo nombre.
- Cálculo del tamaño total de los archivos movidos.
- Recuento de archivos en el origen y en el destino.
- Informe final mediante tablas de Rich.
- Control de errores mediante excepciones.

## Autor
**Realizado por José Raúl Álvarez**