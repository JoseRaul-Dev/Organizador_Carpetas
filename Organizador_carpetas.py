"""
Organizador automático de carpetas.
Este programa se encarga de clasificar los archivos de una carpeta y subcarpetas según su extensión.
"""

import os
import shutil
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

consola=Console()

def main():    
    """
    Este es el método principal de nuestro programa en el que llamaremos a las funciones.
    """
       
    # Creamos la lista en la que guardaremos los movimientos del historial
    historial = []

def mostrar_Cabecera(consola):
    """
    Este método se encarga de tener la cabecera de nuestra aplicación.
    """

    consola.print(Panel("[bold blue]Clasificación de archivos[/bold blue]",title="[bold blue]Organizador de carpetas[/bold blue]",border_style="bold blue"))
    

def obtener_extension(nombre_archivo):
    """
    Este método obtiene la extensión de un archivo y la devuelve en minúsculas. 
    En el caso de que el archivo no tenga extensión, devuelve "sin extension".
    """
    
    # Separamos el nombre del archivo y su extensión.
    _, extension = os.path.splitext(nombre_archivo)
    
    # Comprobamos si el archivo tiene extensión, si no la tiene devolvemos sin extension.
    if extension:
        return extension [1:].lower()
    return "sin extension"

def tamano_legible(tamano_bytes): 
    """
    Este método se encarga de convertir el tamaño recibido en la unidad más adecuada.
    """
    
    unidades = ["bytes", "KB", "MB", "GB"]
    tamaño = float(tamano_bytes)
    indice = 0
    
    # Dividimos el tamaño  recibido entre 1024 hasta que encontremos la unidad adecuada.
    while tamaño >= 1024 and indice < len(unidades) - 1:
        tamaño /= 1024
        indice += 1
    
    # Devolvemos el tamaño del archivo y su unidad.
    if indice == 0:
        return f"{int(tamaño)} {unidades[indice]}"
    return f"{tamaño :.2f} {unidades[indice]}"

def una_dentro_de_otra(ruta_1,ruta_2):
    
    """
    Este método comprueba si dos rutas son iguales o si una está dentro de otra.
    """
    
    # Convertimos las dos rutas en rutas absolutas y normalizamos su formato.
    ruta_1 = os.path.normcase(os.path.abspath (ruta_1))
    ruta_2 = os.path.normcase(os.path.abspath (ruta_2))
    
    # Comprobamos si las dos rutas son iguales.
    if ruta_1 == ruta_2:
        return True
    
    # Comprobamos si la primera ruta está dentro de la segunda.
    if ruta_1.startswith(ruta_2 + os.sep):
        return True
    
    # Comprobamos si la segunda ruta está dentro de la primera.
    if ruta_2.startswith(ruta_1 + os.sep):
        return True
    
    return False

def pedir_rutas(consola):  
    """
    Este método se encarga de solicitar al usuario las rutas de origen y destino.
    """
    
    consola.print(Panel("[bold blue] Introduce la carpeta de origen y la carpeta de destino que vas a utilizar [/bold blue]", border_style="cyan"))
    
    # Pedimos las dos rutas y eliminamos espacios que sobren.
    carpeta_origen=Prompt.ask("[bold blue] Carpeta de origen [/bold blue]",console=consola).strip()
    carpeta_destino= Prompt.ask("[bold blue] Carpeta de destino [/bold blue]",console=consola).strip()
    
    # Este condicional comprueba si nuestra ruta de origen existe y es una carpeta.
    if not os.path.isdir (carpeta_origen):
        consola.print(Panel("[red] La carpeta de origen no existe o no es una carpeta.",title="Error",border_style="red"))
        return None
    
    # Este condicional comprueba que la ruta de destino existe y si existe debe de ser una carpeta.
    if os.path.exists(carpeta_destino) and not os.path.isdir(carpeta_destino):
        consola.print(Panel("[red] La ruta de destino existe pero no es una carpeta.",title="Error",border_style="red"))
        return None
    
    # Este condicional comprueba si el origen y el destino coinciden o si estan uno dentro del otro.
    if una_dentro_de_otra (carpeta_origen, carpeta_destino):
        consola.print(Panel("[red] El origen y el destino no pueden ser iguales ni tampoco puedes estar uno dentro del otro",title="Error",border_style="red"))
        return None
    
    return carpeta_origen,carpeta_destino

def nombre_disponible (ruta_destino, nombre_archivo):
    """
    Este método comprueba si el nombre del archivo ya existe en la ruta de destino. 
    Si existe se añade un número al nombre para que no sean iguales.
    """
    
    # Unimos la ruta de destino con el nombre del archivo.
    ruta= os.path.join(ruta_destino,nombre_archivo)
    
    # Comprobamos si el archivo ya existe.
    if not os.path.exists(ruta):
        return ruta
    
    # Separamos el nombre del archivo y su extensión.
    nombre, extension = os.path.splitext(nombre_archivo)
    contador = 1

    # Se van modificando los nombres hasta que se encuentre uno disponible.
    while True:
        n_nombre = f"{nombre}_{contador}{extension}"
        n_ruta = os.path.join(ruta_destino,n_nombre)
        
        # Comprobamos si el nombre nuevo está libre.
        if not os.path.exists(n_ruta):
            return n_ruta
        
        # Vamos aumentando el contador para probar con otro nombre diferente.
        contador += 1
    
def clasificar_archivo(ruta_origen,nombre_archivo,ruta_destino, historial):
    """
    Este método se encarga de mover un archivo a una subcarpeta que se corresponde con la extensión que tenga.
    Guarda el movimiento que hemos hecho en el historial.
    """
    
    # Juntamos la ruta del origen con el nombre del archivo.
    ruta = os.path.join(ruta_origen,nombre_archivo)
    
    # Obtenemos la extensión del archivo.
    extension = obtener_extension(nombre_archivo)
    
    # Creamos la variable con la ruta de la carpeta correspondiente a la extensión del archivo.
    carpeta = os.path.join(ruta_destino,extension)
    
    # Creamos la carpeta si todavía no existe.
    os.makedirs(carpeta,exist_ok=True)
    
    # Obtenemos el tamaño del archivo antes moverlo
    tamaño = os.path.getsize(ruta)
    
    # Buscamos un nombre que este disponible.
    ruta_n = nombre_disponible(carpeta,nombre_archivo)
    
    # Movemos el arhivo desde la ruta de origen a la ruta de destino
    shutil.move(ruta,ruta_n)
    
    # Añadimos a la lista del historial el movimiento.
    historial.append(f"{ruta} -> {extension}/{os.path.basename(ruta_n)}")
    
    # Devolvemos el tamaño del archivo.
    return tamaño

def clasificar_carpeta_recursivo(ruta_actual,ruta_destino, historial):
    """
    Este método recorre la carpeta de origen y todas las subcarpeta para clasificar los archivos que vaya encontrando.
    Devuelve el tamaño total de los archivos.
    """
    
    # Inicializamos el tamaño total de los archivos.
    total = 0
    
    # Recorremos todos los elementos que hay dentro de la carpeta actual.
    for archivo in os.listdir(ruta_actual):
        ruta_archivos = os.path.join(ruta_actual,archivo)
        
        # Si el elemento es una carpeta, entramos en ella utilizando la recursividad
        if os.path.isdir(ruta_archivos):
            total += clasificar_carpeta_recursivo(ruta_archivos,ruta_destino,historial)
        
        # Si el elemento es un archivo, lo clasificamos llamando al método clasificar_archivo.
        elif os.path.isfile(ruta_archivos):
            total += clasificar_archivo(ruta_actual,archivo,ruta_destino,historial)

    # Devolvemos el tamaño total de los archivos clasificados.
    return total   

def contar_archivos_recursivo(ruta_actual):
    """
    Este método cuenta todos los archivos que hay en una carpeta y en sus subcarpetas mediante recursividad.
    Devuelve el número total de los archivos que se han encontrado.
    """
    
    # Inicializamos el contador de archivos.
    contador = 0
    
    # Recorremos todos los archivos de la carpeta.
    for archivo in os.listdir(ruta_actual):
        ruta_archivos = os.path.join(ruta_actual,archivo)
        
        # En el caso de que sea una carpeta, entramos en ella y contamos también sus archivos mediante la recursividad.
        if os.path.isdir(ruta_archivos):
            contador+= contar_archivos_recursivo(ruta_archivos)
            
        # En el caso de que sea un archivo, vamos aumentando el contador.
        elif os.path.isfile(ruta_archivos):
            contador += 1
            
    # Devolvemos el número total de todos los archivos que hayamos encontrado.
    return contador 

def mostrar_informe(consola,historial, tamano_total, archivos_origen, archivos_destino):
    """
    Este método muestra el informe final con los archivos clasificado, sus movimientos y el tamaño total
    """
    
    # Creamos la primera tabla con el informe final.
    tabla1 = Table(title="Informe final")
    tabla1.add_column("Concepto", style="white")
    tabla1.add_column("Valor", style="bold cyan")
    
    # Añadimos las filas a la primera tabla.
    tabla1.add_row("Archivos movidos", str(len(historial)))
    
    # Añadimos el tamaño total movido en caso de que el tamaño sea 0 el color sera verde y si es mayor de 0 sera en amarillo.
    if tamano_total == 0:
        tabla1.add_row("Tamaño total movido", f"[green]{tamano_legible(tamano_total)}[/green]")
    else:
        tabla1.add_row("Tamaño total movido",f"[yellow]{tamano_legible(tamano_total)}[/yellow]")
    
    # Si no quedan archivos en el origen, mostramos el valor en verde, en caso contrario en rojo
    if archivos_origen == 0:
        tabla1.add_row("Archivos que quedan en el origen", f"[bold green]{archivos_origen}[/bold green]")
    else:
        tabla1.add_row("Archivos que quedan en el origen", f"[bold red]{archivos_origen}[/bold red]")
        
    tabla1.add_row("Archivos en el destino (con subcarpetas)", f"[bold blue]{archivos_destino}[/bold blue]")
    
    # Mostramos la primera tabla.
    consola.print(tabla1)
    
    # Creamos la segunda tabla con los movimientos que se han hecho.
    tabla2 = Table(title="Movimientos realizados")
    tabla2.add_column("Nº",style = "bold green")
    tabla2.add_column("Origen -> Destino", style="white")
    
    # Recorremos la lista del historial y añadimos cada movimiento a la segunda tabla.
    contador = 1
    for movimiento in historial:
        tabla2.add_row(str(contador),movimiento)
        contador += 1
        
    # Mostramos la segunda tabla.
    consola.print(tabla2)