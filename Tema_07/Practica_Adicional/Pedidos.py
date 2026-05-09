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
        return self.fecha
    
    @fecha.setter
    def fecha(self, value: date):
        if value == None:
            raise ValueError("La fecha no puede ser nula")
        self.fecha = value

    @property
    def total(self) -> float:
        return self.total
    
    @total.setter
    def total(self, value: float):
        if value == None:
            raise ValueError("El total no puede ser nulo.")
        if value < 0:
            raise ValueError("El total no puede ser negativo.")
        d = Decimal(str(value)).normalize()
        digits_tuple = d.as_tuple()
        
        total_digits = len(digits_tuple.digits)
        decimal_places = abs(digits_tuple.exponent)
        if total_digits > 10 or decimal_places > 2:
            raise ValueError("El total no puede tener más de 10 dígitos y no pude tener más de 3 decimales.")
        self.total = value

    def __str__(self):
        return f"ID Pedido: {self.id_pedido} | ID Cliente: {self.id_cliente} | Fecha: {self.fecha} | Total: {self.total}"
    
    def __eq__(self, value):
        if not isinstance(value, Pedido):
            return False
        return value.id_pedido == self.id_pedido