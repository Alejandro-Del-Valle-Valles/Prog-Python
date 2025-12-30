from abc import ABC, abstractmethod
from service.ReglasToreno import ReglasTorneo

class EnteMagico(ABC):

    def __init__(self, nombre: str, vida: int):
        self._nombre = nombre
        self.__vida = vida
        self._vida_maxima = vida

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str):
        """
        Settea el nombre del EnteMagico capitalizado, y si el nombre no es válido, lo settea a "Desconocido".
        
        :param nombre: Nombre del EnteMagico.
        :type nombre: str
        """
        self._nombre = nombre.strip().capitalize() if nombre and nombre.strip() else "Desconocido"

    @property
    def vida(self) -> int:
        return self.__vida
    
    @vida.setter
    def vida(self, vida: int):
        """
        Settea la vida del EnteMagico, si es inferior a 0, lo settea a 0, y si es superior a la vida máxima, lo settea a la vida máxima.
        
        :param vida: Vida del ente EnteMagico.
        :type vida: int
        """
        if vida > 0:
            self.__vida = vida if self._vida_maxima >= vida else self._vida_maxima
        else:
            print(self.nombre, " ha sido derrotado.")
            self.__vida = 0

    @property
    def vida_maxima(self) -> int:
        return self._vida_maxima
    
    @vida_maxima.setter
    def vida_maxima(self, vida_maxima: int):
        """
        Settea la vida máxima 
        
        :param vida_maxima: Puntos de vida máxima del EnteMagico.
        :type vida_maxima: int
        """
        self._vida_maxima = vida_maxima if vida_maxima > 1 else 1

    @abstractmethod
    def atacar(self, enemigo: 'EnteMagico'):
        """
        Ataca al enemigo y le inflinge daño.
        
        :param enemigo: Enemigo a atacar
        :type enemigo: 'EnteMagico'
        """
        pass

    @abstractmethod
    def __str__(self):
        return super().__str__()
    
    @abstractmethod
    def __repr__(self):
        return super().__repr__()