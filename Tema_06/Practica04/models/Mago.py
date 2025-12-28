from EnteMagico import EnteMagico

class Campeon(EnteMagico):

    def __init__(self, nombre: str, vida: int, vida_maxima: int, energia: int, hechizos: list[str]):
        self.set_nombre(nombre)
        self.set_vida_maxima(vida_maxima)
        self.set_vida(vida)
        self.energia = energia
        self.hechizos = hechizos

    @property
    def get_energia(self) -> int:
        return self.energia
    
    @get_energia.setter
    def set_energia(self, energia: int):
        self.energia = energia if energia > 0 else 0

    @property
    def get_hechizos(self) -> list[str]:
        return self.hechizos
    
    @get_hechizos.setter
    def set_hechizos(self, hechizos: list[str]):
        self.hechizos = hechizos

    def aprender_hechizo(self, hechizo: str):
        self.hechizos.append(hechizo)

    def atacar(self, enemigo: EnteMagico):
        pass

    def __str__(self):
        return f"Soy {self._nombre}, {f"tengo {self.__vida} puntos de vida" if self.__vida > 0 else "he sido derrotado,"}, tengo {self.energia} puntos de energía, y se usar {len(self.hechizos)}"
    
    def __repr__(self) -> str:
            """
            :return: String JSON representation of the object.
            :rtype: str
            """
            return f"{{\"nombre\": \"{self._nombre}\", \"vida\": {self.__vida}, \"vida_maxima\": {self._vida_maxima}, \"energia\": {self.energia}, \"hechizos\": {self.hechizos}}}"
    
    def __len__(self) -> int:
        return len(self.hechizos)