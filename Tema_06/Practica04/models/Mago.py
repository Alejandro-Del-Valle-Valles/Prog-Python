from models.EnteMagico import EnteMagico
from service.ReglasToreno import ReglasTorneo

class Mago(EnteMagico):

    def __init__(self, nombre: str, vida: int, energia: int):
        super().__init__(nombre, vida)
        self.energia = energia
        self.hechizos = []

    @property
    def energia(self) -> int:
        return self._energia
    
    @energia.setter
    def energia(self, energia: int):
        """
        Settea el nivel de energia del mago, si es inferior a 0, lo settea a 0.
        
        :param energia: Nivel de energia del mago
        :type energia: int
        """
        self._energia = energia if energia > 0 else 0

    @property
    def hechizos(self) -> list[str]:
        return self._hechizos
    
    @hechizos.setter
    def hechizos(self, hechizos: list[str]):
        self._hechizos = hechizos

    def aprender_hechizo(self, hechizo: str):
        """
        Añade un hechizo a la lista de hechizos del mago.
        
        :param hechizo: Nombre del hechizo
        :type hechizo: str
        """
        self.hechizos.append(hechizo)

    def atacar(self, enemigo: EnteMagico):
        """
        Hace daño al enemigo con un hechizo.
        
        :param enemigo: Enemigo a atacar
        :type enemigo: EnteMagico
        """
        danyo: int = 0
        if self.energia >= 5:
            self.energia -= 5
            danyo = ReglasTorneo.calcular_danyo(20, 0)
        enemigo.vida -= danyo
        print(f"{self.nombre} lanza un hechizo a básico a {enemigo.nombre} (-{danyo} HP)")

    def __str__(self):
        return f"[Mago] {self.nombre} | HP {self.vida}/{self.vida_maxima} | {self.energia} Energía | {len(self.hechizos)} Hechizo."
    
    def __repr__(self) -> str:
            """
            :return: String con formato JSON del objeto.
            :rtype: str
            """
            return f"{{\"nombre\": \"{self.nombre}\", \"vida\": {self.vida}, \"vida_maxima\": {self.vida_maxima}, \"energia\": {self.energia}, \"hechizos\": {self.hechizos}}}"
    
    def __len__(self) -> int:
        return len(self.hechizos)