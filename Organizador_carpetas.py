import os
import shutil
from rich.console import Console
from rich.panel import Panel

consola=Console()

def mostrar_Cabecera(consola):
    consola.print(Panel("[bold blue]Clasificación de archivos[/bold blue]",title="[bold blue]Organizador de carpetas[/bold blue]",border_style="bold blue"))
    
def obtener_extension(nombre_archivo):
    _, extension = os.path.splitext(nombre_archivo)
    if extension:
        return extension [1:].lower()
    return "sin extension"

def tamano_legible(tamano_bytes):
    unidades = ["bytes", "KB", "MB", "GB"]
    tamaño = float(tamano_bytes)
    indice = 0
    
    while tamaño >= 1024 and indice < len(unidades) - 1:
        tamaño /= 1024
        indice += 1
    
    if indice == 0:
        return f"{int(tamaño)} {unidades[indice]}"
    return f"{tamaño :.2f} {unidades[indice]}"