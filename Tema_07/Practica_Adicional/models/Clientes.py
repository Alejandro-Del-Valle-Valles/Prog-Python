class Cliente:

    def __init__(self, nombre: str, email: str, telefono: str, id: int = 0):
        self.__id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @nombre.setter
    def nombre(self, value: str):
        value = value.strip()
        if not value or value == "":
            raise ValueError("El nombre no puede estar vacío.")
        if len(value) > 100:
            raise ValueError("El nombre no puede tener más de 100 caracteres.")
        self.__nombre = value.capitalize()
    
    @property
    def email(self) -> str:
        return self.__email
    
    @email.setter
    def email(self, value: str):
        value = value.strip()
        if not value or value == "":
            raise ValueError("El email no puede estar vacío.")
        if len(value) > 150:
            raise ValueError("El email no puede contener más de 150 caracteres.")
        if not '@' and '.' in value:
            raise ValueError("El email no tiene el formato correcto. Debe contener @ y extensión (.com, .es, etc)")
        self.__email = value

    @property
    def telefono(self) -> str:
        return self.__telefono
    
    @telefono.setter
    def telefono(self, value: str):
        value = value.strip()
        if not value or value == "":
            raise ValueError("El número de teléfono no puede estar vacío.")
        if len(value) > 20:
            raise ValueError("El número de teléfono no puede contenermás de 20 caracteres.")
        self.__telefono = value

    def __eq__(self, value) -> bool:
        if not isinstance(value, Cliente):
            return False
        return self.id == value.id
    
    def __str__(self):
        return f"Id: {self.id} | Nombre: {self.nombre} | Email: {self.email} | Tlfn: {self.telefono}"