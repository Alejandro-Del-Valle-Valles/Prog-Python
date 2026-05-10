from datetime import date
from decimal import Decimal

class Pedido:

    def __init__(self, id_cliente: int, fecha: date, total: float, id_pedido: int = 0):
        self.__id_pedido = id_pedido
        self.__id_cliente = id_cliente
        self.fecha = fecha
        self.total = total

    @property
    def id_pedido(self) -> int:
        return self.__id_pedido
    
    @property
    def id_cliente(self) -> int:
        return self.__id_cliente
    
    @property
    def fecha(self) -> date:
        return self.__fecha
    
    @fecha.setter
    def fecha(self, value: date):
        if not value:
            raise ValueError("La fecha no puede ser nula")
        self.__fecha = value

    @property
    def total(self) -> float:
        return self.__total
    
    @total.setter
    def total(self, value: float):
        if not value:
            raise ValueError("El total no puede ser nulo.")
        if value < 0:
            raise ValueError("El total no puede ser negativo.")
        
        partes = str(float(value)).split('.')
        enteros = partes[0]
        decimales = partes[1] if len(partes) > 1 else ""
        if len(enteros) > 8 or len(decimales) > 2:
            raise ValueError("El subtotal no puede exceder los 10 dígitos (máximo 8 enteros y 2 decimales).")
        
        self.__total = value

    def __str__(self):
        return f"ID Pedido: {self.id_pedido} | ID Cliente: {self.id_cliente} | Fecha: {self.fecha} | Total: {self.total}"
    
    def __eq__(self, value):
        if not isinstance(value, Pedido):
            return False
        return value.id_pedido == self.id_pedido