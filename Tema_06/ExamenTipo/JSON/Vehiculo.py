from abc import ABC

class Vehiculo(ABC):

    def __init__(self, matricula, marca, modelo, anyo: int, precio_base: float):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.anyo = anyo
        self.precio_base = precio_base

    @classmethod
    def validar_matricula(cls, matricula: str) -> bool:
        datos = matricula.split()
        return len(datos) == 2 and len(datos[0]) == 4 and datos[0].isnumeric() and len(datos[1]) == 3 and datos[1].isalpha()
    #Cambiado, verifica que 0000 AAA es el estilo
