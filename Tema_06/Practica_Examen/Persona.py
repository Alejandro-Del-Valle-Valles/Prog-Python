class Persona:
    
    def __init__(self, dni: str, nombre: str, apellidos: str, edad: int, tlf: str):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.tlf = tlf

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value: str):
        self.__nombre = value.strip().capitalize() if value.strip() != "" else "Sin nombre"
        
    @property
    def apellidos(self):
        return self.__apellidos
    
    @apellidos.setter
    def apellidos(self, value: str):
        self.__apellidos = value.strip().capitalize() if value.strip() != "" else "Sin Apellido"
        
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, value: int):
        self.__edad = value if value > -1 else 0
        
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self, value: str):
        self.__dni = value.strip() if value.strip() != "" else "Sin DNI"
        
    @property
    def tlf(self):
        return self.__tlf
    
    @tlf.setter
    def tlf(self, value: str):
        self.__tlf = value.strip() if value.strip().isdigit() else "Sin teléfono"

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellidos} | {self.edad} Años | DNI: {self.dni} | Nº Tlf: {self.tlf}"
    
    def __repr__(self):
        return f"Persona({self.nombre}, {self.apellidos}, {self.edad}, {self.dni}, {self.tlf})"
    
    def __eq__(self, other):
        return self.dni == other.dni
    
    def __hash__(self):
        return hash(self.dni)