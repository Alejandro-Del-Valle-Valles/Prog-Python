from decimal import Decimal

class DetallePedido:

    def __init__(self, id_pedido: int, id_producto: int, cantidad: int, subtotal: float,  id_detalle: int = 0):
        self.__id_detalle = id_detalle
        self.__id_pedido = id_pedido
        self.__id_producto = id_producto
        self.cantidad = cantidad
        self.subtotal = subtotal

    @property
    def id_detalle(self) -> int:
        return self.__id_detalle
    
    @property
    def id_pedido(self) -> int:
        return self.__id_pedido
    
    @property
    def id_producto(self) -> int:
        return self.__id_producto
    
    @property
    def cantidad(self) -> int:
        return self.cantidad
    
    @cantidad.setter
    def cantidad(self, value: int):
        if value == None:
            raise ValueError("La cantidad no puede ser nula.")
        if value < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = value

    @property
    def subtotal(self) -> float:
        return self.subtotal
    
    @subtotal.setter
    def subtotal(self, value: float):
        if value == None:
            raise ValueError("El subtotal no puede ser nulo.")
        if value < 0:
            raise ValueError("El subtotal no puede ser negativo.")
        d = Decimal(str(value)).normalize()
        digits_tuple = d.as_tuple()
        
        total_digits = len(digits_tuple.digits)
        decimal_places = abs(digits_tuple.exponent)
        if total_digits > 10 or decimal_places > 2:
            raise ValueError("El subtotal no puede tener más de 10 dígitos y no pude tener más de 3 decimales.")
        
        self.subtotal = value

    def __str__(self):
        return f"ID Detalle Pedido: {self.__id_detalle} | ID Pedido: {self.__id_pedido} | ID Producto: {self.__id_producto} | Cantidad: {self.cantidad} | Subtotal: {self.subtotal}€"
    
    def __eq__(self, value):
        if not isinstance(value, DetallePedido):
            return False
        return value.id_detalle == self.id_detalle