from datetime import date, datetime
from ErrorPersonalizado import ErrorPersonalizado
from Extensiones import printerr

__FORMATO_FECHA = "%d/%m/%Y"


class SolicitarDatos:
# Clase Auxiliar para Solicitar Datos

    @staticmethod
    def pedir_numero_entero(pregunta: str, es_positivo: bool = False, permitir_nulo = True) -> int:
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
                if not permitir_nulo and not numero:
                    raise ErrorPersonalizado("El número no puede ser nulo.")
                if es_positivo and numero < 0:
                    raise ErrorPersonalizado("Debes introdcuir un número positivo (0 o superior)")
                break
            except ErrorPersonalizado as ex:
                printerr(ex)
            except:
                printerr("Debes introducir un número.")
        return numero

    @staticmethod
    def pedir_numero_decimal(pregunta: str, es_positivo: bool = False, permitir_nulo = True) -> float:
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
                if not permitir_nulo and not numero:
                    raise ErrorPersonalizado("El número no puede ser nulo.")
                if es_positivo and numero < 0:
                    raise ErrorPersonalizado(f"Debes introducir un número positivo (0 o mayor)")
                break
            except ErrorPersonalizado as ex:
                printerr(ex)
            except:
                printerr("Debes introducir un número.")
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
                if not texto or texto == "":
                    raise ErrorPersonalizado("El texto no puede estar vacío.")
                break
            except ErrorPersonalizado as ex:
                printerr(ex)
            except:
                printerr("Ha ocurrido un error inesperado.")
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
                if fecha_maxima and fecha > fecha_maxima:
                    raise ErrorPersonalizado(f"La fecha no puede ser mayor a {fecha_maxima.strftime(__FORMATO_FECHA)}")
                break
            except ErrorPersonalizado as ex:
                printerr(ex)
            except:
                printerr("Debes introducir una fecha con el formato indicado.")
        return fecha