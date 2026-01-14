from Vehiculo import Vehiculo

class Automovil(Vehiculo):

    TIPOS_COMBUISTIBLES = ("DIE", "GAS", "ELE", "GLP")

    def __init__(self, matricula, marca, modelo, anyo: int, precio_base: float, numero_puertas: int, tipo_combustible):
        super().__init__(matricula, marca, modelo, anyo, precio_base)
        self.numero_puertas = numero_puertas
        self.tipo_combustible = tipo_combustible

    def __str__(self):
        return f"Automovil: Matricula {self.matricula} | Marca {self.marca} | Modelo {self.precio_base} | Año {self.anyo} | Precio Base {self.precio_base:.2f} | Puertas {self.numero_puertas} | Combustible {self.tipo_combustible}"
    
    