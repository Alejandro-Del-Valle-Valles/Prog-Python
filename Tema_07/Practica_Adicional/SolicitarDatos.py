from datetime import date, datetime
from ErrorPersonalizado import ErrorPersonalizado

__COLOR_ROJO: str = "\033[31m" #Código del color rojo para los str.
__COLOR_RESET: str = "\033[0m"
__FORMATO_FECHA = "%d/%m/%Y"


class SolicitarDatos:
# Clase Auxiliar para Solicitar Datos

    @staticmethod
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
                print(f"{__COLOR_ROJO}{ex}{__COLOR_RESET}")
            except:
                print(f"{__COLOR_ROJO}Debes introducir un número.{__COLOR_RESET}")
        return numero

    @staticmethod
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
                print(f"{__COLOR_ROJO}{ex}{__COLOR_RESET}")
            except:
                print(f"{__COLOR_ROJO}Debes introducir un número.{__COLOR_RESET}")
        return numero

    @staticmethod
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
                print(f"{__COLOR_ROJO}{ex}{__COLOR_RESET}")
            except:
                print(f"{__COLOR_ROJO}Ha ocurrido un error inesperado.{__COLOR_RESET}")
        return texto

    @staticmethod
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
                fecha = datetime.strptime(fecha_input, __FORMATO_FECHA).date()
                if fecha_maxima != None and fecha > fecha_maxima:
                    raise ErrorPersonalizado(f"La fecha no puede ser mayor a {fecha_maxima.strftime(__FORMATO_FECHA)}")
                break
            except ErrorPersonalizado as ex:
                print(f"{__COLOR_ROJO}{ex}{__COLOR_RESET}")
            except:
                print(f"{__COLOR_ROJO}Debes introducir una fecha con el formato indicado.{__COLOR_RESET}")
        return fecha