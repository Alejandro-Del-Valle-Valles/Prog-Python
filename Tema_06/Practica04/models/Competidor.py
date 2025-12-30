class Competidor:
    
    def __init__(self, casa: str):
        self.casa = casa
        self.puntos = 0

    @property
    def casa(self) -> str:
        return self._casa
    
    @casa.setter
    def casa(self, casa: str):
        self._casa = casa.strip().capitalize() if casa and casa.strip() != "" else "Desconocida"

    @property
    def puntos(self) -> int:
        return self._puntos
    
    @puntos.setter
    def puntos(self, puntos: int):
        self._puntos = puntos if puntos > 0 else 0

    def ganar_puntos(self, cantidad: int):
        self.puntos += cantidad

    def __str__(self):
        return f"[Competidor] Casa {self.casa} | {self.puntos} Puntos."

