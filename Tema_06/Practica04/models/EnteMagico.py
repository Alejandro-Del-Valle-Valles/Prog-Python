from abc import ABC, abstractmethod

class EnteMagico(ABC):

    def __init__(self):
        self._nombre
        self.__vida
        self._vida_maxima

    @property
    def get_nombre(self, nombre: str) -> str:
        return self._nombre

    @get_nombre.setter
    def set_nombre(self, nombre: str):
        nombre = nombre.strip().capitalize()
        self._nombre = "Desconocido" if nombre == None or nombre == "" else nombre

    @property
    def get_vida(self) -> int:
        return self.__vida
    
    @get_vida.setter
    def set_vida(self, vida: int):
        if vida > 0:
            self.__vida = vida if self._vida_maxima >= vida else self._vida_maxima
        else:
            self.__vida = 0

    @property
    def get_vida_maxima(self) -> int:
        return self._vida_maxima
    
    @get_vida_maxima.setter
    def set_vida_maxima(self, vida_maxima: int):
        self._vida_maxima = vida_maxima if vida_maxima > 1 else 1

    @abstractmethod
    def atacar(self, enemigo: 'EnteMagico'):
        pass

    @abstractmethod
    def __str__(self):
        return super().__str__()
    
    @abstractmethod
    def __repr__(self):
        return super().__repr__()