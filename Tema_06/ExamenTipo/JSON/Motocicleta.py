from Vehiculo import Vehiculo

class Motocicleta(Vehiculo):

    TIPOS_CASCOS = ("Intergal", "Jet", "Abatible")

    def __init__(self, matricula, marca, modelo, anyo: int, precio_base: float, cilindrada: int, tipo_casco_incluido):
        super().__init__(matricula, marca, modelo, anyo, precio_base)
        self.cilindrada = cilindrada
        self.tipo_casco_inlcuido = tipo_casco_incluido
        
    def __str__(self):
        return f"Motocicleta: Matricula {self.matricula} | Marca {self.marca} | Modelo {self.precio_base} | Año {self.anyo} | Precio Base {self.precio_base:.2f} | Cilindrada {self.cilindrada} | Casco {self.tipo_casco_inlcuido}"