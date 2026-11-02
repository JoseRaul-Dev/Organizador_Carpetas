"""
Este archivo sirve para comprobar el funcionamiento del método tamano_legible()
"""

from Organizador_carpetas import tamano_legible

def prueba_tamaño():
    
    """
    Este método sirve para comprobar que nuestro método tamano_legible() funciona.
    """
    
    print(tamano_legible(0))
    print(tamano_legible(1023))
    print(tamano_legible(1024))
    print(tamano_legible(1048576))
    print(tamano_legible(1073741824))

# Mediante este condicional ejecutamos las pruebas.
if __name__ == "__main__":
    prueba_tamaño()