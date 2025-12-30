from models.EnteMagico import EnteMagico
from service.ReglasToreno import ReglasTorneo

class Dragon(EnteMagico):

    __dragones_arena = 0

    def __init__(self, nombre: str, vida: int, tipo_fuego: str):
        super().__init__(nombre, vida)
        self.__tipo_fuego = tipo_fuego
        Dragon.__dragones_arena += 1


    @property
    def tipo_fuego(self) -> str:
        return self.__tipo_fuego
    
    @tipo_fuego.setter
    def tipo_fuego(self, tipo_fuego: str):
        self.__tipo_fuego = tipo_fuego.strip().capitalize() if tipo_fuego and tipo_fuego.strip() != "" else "Desconocido"

    @classmethod
    def get_dragones_arena(cls) -> int:
        return cls.__dragones_arena
    
    @classmethod
    def set_dragones_arena(cls, dragones_arena: int):
        cls.__dragones_arena = dragones_arena if dragones_arena > 0 else 0

    def atacar(self, enemigo: EnteMagico):
        """
        Hace daño al enemigo con fuego.
        
        :param enemigo: Enemigo a atacar
        :type enemigo: EnteMagico
        """
        danyo = ReglasTorneo.calcular_danyo(40, 5)
        print(f"{self.nombre} lanza esupe fuego {self.tipo_fuego} a {enemigo.nombre} (-{danyo} HP)")

    def __str__(self):
        return f"[Dragón] {self.nombre} | HP {self.vida}/{self.vida_maxima} | Fuego {self.tipo_fuego}"
    
    def __repr__(self) -> str:
            """
            :return: String con formato JSON del objeto.
            :rtype: str
            """
            return f"{{\"nombre\": \"{self.nombre}\", \"vida\": {self.vida}, \"vida_maxima\": {self.vida_maxima}}}"