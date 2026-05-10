# Extensión del método print para imprimir en rojo para errores
import os
import time

def printerr(*args, **kwargs):
    print("\033[91m", end="") 
    print(*args, **kwargs)
    print("\033[0m", end="", flush=True)

def pausa_y_limpia(segundos: int = 1):
    """Pausa la ejecución unos segundos y limpia la consola

    Args:
        segundos (int): Segundos a pausar la consola, por defecto 1
    """
    time.sleep(segundos)
    limpiar_consola()

def limpiar_consola():
    """
    Limpia la consola
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def enter_limpiar(mensaje: str = "Pulsa enter para continuar..."):
    """
    Espera a que el usuario pulse enter para continuar y limpiar la consola
    """
    input(mensaje)
    limpiar_consola()