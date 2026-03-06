# Fichero principal de la practica
from datetime import date, datetime
from ErrorPersonalizado import ErrorPersonalizado

OPCIONES: tuple = ("Gestionar Opciones", "Gestionar Productos", "Gestionar Pedidos", "Gestionar Detalles Pedido")
COLOR_ROJO: str = "\033[31m" #Código del color rojo para los str.
COLOR_RESET: str = "\033[0m"
FORMATO_FECHA = "%d/%m/%Y"

#MÉTODOS PARA PEDIR DATOS
def pedir_numero_entero(pregunta: str, es_positivo: bool = False) -> int:
    """
    Pide un número entero al usuario. Mientras no sea un número entero, se volverá a pedir.
    Args:
        pregunta (str): texto a mostrar como pregunta.
        es_positivo (bool): Por defecto False. True solo permite números igual o mayor a 0.
    Returns:
        int: numero introducido
    """
    numero: int
    while True:
        try:
            print(pregunta)
            numero = int(input())
            if es_positivo and numero < 0:
                raise ErrorPersonalizado("Debes introdcuir un número positivo (0 o superior)")
            break
        except ErrorPersonalizado as ex:
            print(f"{COLOR_ROJO}{ex}{COLOR_RESET}")
        except:
            print(f"{COLOR_ROJO}Debes introducir un número.{COLOR_RESET}")
    return numero

def pedir_numero_decimal(pregunta: str, es_positivo: bool = False) -> float:
    """
    Pide un número con decimal al usuario. Mientras no sea un número con decimal, se volverá a pedir.
    Args:
        pregunta (str): texto a mostrar como pregunta.
        es_positivo (bool): True solo permite números igual o mayor a 0. Defaults to False.
    Returns:
        float: numero introducido
    """
    numero: float
    while True:
        try:
            print(pregunta)
            numero = float(input())
            if es_positivo and numero < 0:
                raise ErrorPersonalizado(f"Debes introducir un número positivo (0 o mayor)")
            break
        except ErrorPersonalizado as ex:
            print(f"{COLOR_ROJO}{ex}{COLOR_RESET}")
        except:
            print(f"{COLOR_ROJO}Debes introducir un número.{COLOR_RESET}")
    return numero

def pedir_str(pregunta: str, longitud_maxima: int = None) -> str:
    """
    Pide un string al usuario. Mientras no introduzca nada o supere el nº de caracteres si lo hay, volverá a pedirlo.
    Args:
        pregunta (str): Pregunta a mostrar.
        longitud_maxima (int, optional): Longitud máxima (Incluida) permitida del texto. Defaults to None.

    Returns:
        str: texto introducido
    """
    texto: str
    while True:
        try:
            print(pregunta)
            texto = input().strip()
            if longitud_maxima != None and len(texto) > longitud_maxima:
                raise ErrorPersonalizado(f"El texto no puede contener más de {longitud_maxima} caracteres")
            if texto == None or texto == "":
                raise ErrorPersonalizado("El texto no puede estar vacío.")
            break
        except ErrorPersonalizado as ex:
            print(f"{COLOR_ROJO}{ex}{COLOR_RESET}")
        except:
            print(f"{COLOR_ROJO}Ha ocurrido un error inesperado.{COLOR_RESET}")
    return texto

def pedir_fecha(pregunta: str, fecha_maxima: date = None) -> date:
    """
    Pide al usuario que introduzca una fecha con formato dd/MM/yyyy. Mientras no introduzca fecha o sea posterior, vuelve a pedirla.
    Args:
        pregunta (str): Pregunta a mostrar
        fecha_maxima (date, optional): Fecha maxíma incluida. Defaults to None.

    Returns:
        date: Fecha introducida
    """
    fecha: date
    while True:
        try:
            print(pregunta + " (dd/MM/yyyy)")
            fecha_input: str = input().strip()
            fecha = datetime.strptime(fecha_input, FORMATO_FECHA).date()
            if fecha_maxima != None and fecha > fecha_maxima:
                raise ErrorPersonalizado(f"La fecha no puede ser mayor a {fecha_maxima.strftime(FORMATO_FECHA)}")
            break
        except ErrorPersonalizado as ex:
            print(f"{COLOR_ROJO}{ex}{COLOR_RESET}")
        except:
            print(f"{COLOR_ROJO}Debes introducir una fecha con el formato indicado.{COLOR_RESET}")
    return fecha


#MÉTODOS MENU
def manejar_menu(opcion: int):
    """
    Ejecuta el método correspondiente a la opción que se le pasa por parámetro
    Args:
        opcion (int): Opción elegida por el usuario, es el numero del metodo a ejecutar.
    """
    match(opcion) :
        case 0:
            print("Saliendo del programa...")
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case _:
            print(f"{COLOR_ROJO}La opción elegida no es válida{COLOR_RESET}")

def main():
    """
    Maneja el menú y la ejecución principal del programa.
    """
    opcion = -1
    while opcion != 0:
        for i in range(len(OPCIONES)):
            print(f"{i + 1}. {OPCIONES[i]}")
        print("0. Salir")
        opcion = pedir_numero_entero("Introduce una opción por favor: ")
        manejar_menu(opcion)


if __name__ == '__main__':
    main()