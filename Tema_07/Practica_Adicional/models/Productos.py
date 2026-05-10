from decimal import Decimal

class Producto:

    def __init__(self, nombre: str, precio: float, stock: int, id: int):
        self.__id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value: str):
        value = value.strip()
        if not value or value == "":
            raise ValueError("El nombre no puede estar vacío.")
        if len(value) > 150:
            raise ValueError("El nombre no puede tener más de 150 caracteres.")
        self.__nombre = value.capitalize()

    @property
    def precio(self) -> float:
        return self.__precio
    
    @precio.setter
    def precio(self, value: float):
        if not value:
            raise ValueError("El precio no puede estar vacío.")
        if value < 0:
            raise ValueError("El precio no puede ser negativo.")
        
        partes = str(float(value)).split('.')
        enteros = partes[0]
        decimales = partes[1] if len(partes) > 1 else ""
        if len(enteros) > 8 or len(decimales) > 2:
            raise ValueError("El subtotal no puede exceder los 10 dígitos (máximo 8 enteros y 2 decimales).")
        
        self.__precio = value
        
    @property
    def stock(self) -> int:
        return self.__stock
    
    @stock.setter
    def stock(self, value: int):
        if not value:
            raise ValueError("El stock no puede ser nulo.")
        if value < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__stock = value

    def __str__(self) -> str:
        return f"ID: {self.id} | Nombre: {self.nombre} | Precio: {self.precio}€ | Stock: {self.stock}"
    
    def __eq__(self, value):
        if not isinstance(value, Producto):
            return False
        return value.id == self.id