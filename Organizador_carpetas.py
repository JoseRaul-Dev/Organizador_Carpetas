import os
import shutil
from rich.console import Console
from rich.panel import Panel

consola=Console()

def mostrar_Cabecera(consola):
    consola.print(Panel("[bold blue]Clasificación de archivos[/bold blue]",title="[bold blue]Organizador de carpetas[/bold blue]",border_style="bold blue"))
    
def obtener_extension(nombre_archivo):
    extension = os.path.splitext(nombre_archivo)
    if extension:
        return extension [1:].lower()
    return "sin extension"