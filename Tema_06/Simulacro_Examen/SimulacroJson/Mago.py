class Mago:

    def __init__(self, nombre: str, edad: int, sangre: str, casa: str, nota_media: float):
        self.nombre = nombre
        self.edad = edad
        self.sangre = sangre
        self.casa = casa
        self.nota_media = nota_media

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value if value.strip() != "" else "Desconocido"

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, value):
        self._edad = value if value > 0 else 0

    @property
    def sangre(self):
        return self._sangre

    @sangre.setter
    def sangre(self, value):
        self._sangre = value if value.strip() != "" else "Desconocida"

    @property
    def casa(self):
        return self._casa

    @casa.setter
    def casa(self, value):
        self._casa = value if value.strip() != "" else "Desconocida"

    @property
    def nota_media(self):
        return self._nota_media

    @nota_media.setter
    def nota_media(self, value):
        if 0 <= value <= 10:
            self._nota_media = value
        elif value > 10:
            self._nota_media = 10
        else:
            self._nota_media = 0

    @classmethod
    def enfrentar(cls, mago_uno, mago_dos):
        if mago_uno.nota_media > mago_dos.nota_media:
            print(f"{mago_uno.nombre} gana a {mago_dos.nombre}")
        elif mago_uno.nota_media < mago_dos.nota_media:
            print(f"{mago_dos.nombre} gana a {mago_uno.nombre}")
        else:
            print("Ambos magos empatan.")

    def __str__(self):
        return f"Nombre: {self._nombre} | Edad: {self._edad} | Sangre: {self._sangre} | Casa: {self._casa} | Nota Media: {self._nota_media}"
    
    def __eq__(self, value):
        return self._nombre.lower() == value._nombre.lower()