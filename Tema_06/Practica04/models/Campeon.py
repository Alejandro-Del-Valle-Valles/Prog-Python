from models.Mago import Mago
from models.Competidor import Competidor

class Campeon(Mago, Competidor):

    def __init__(self, nombre: str, vida: int, energia: int, casa: str):
        Mago.__init__(self, nombre, vida, energia)
        Competidor.__init__(self, casa)

    def __str__(self):
        return f"[Campeón] {self.nombre} | Casa {self.casa} | HP {self.vida}/{self.vida_maxima} | {self.energia} Energía | {self.puntos} Puntos."
    
    def __repr__(self) -> str:
            """
            :return: String con formato JSON del objeto.
            :rtype: str
            """
            return f"{{\"nombre\": \"{self.nombre}\", \"vida\": {self.vida}, \"vida_maxima\": {self.vida_maxima}, \"energia\": {self.energia}, \"hechizos\": {self.hechizos}, \"casa\": \"{self.casa}\", \"puntos\": {self.puntos}}}"
    
    def __eq__(self, value):
         """
         Comprueba si dos objetos son iguales si ambos son Campeones y si ambos tienen la misma vida y energía.
         
         :param value: Objetos a comparar
         :type value: object (Campeon)
         """
         if not isinstance(value, Campeon):
            return False
         return self.vida == value.vida and self.energia == value.energia