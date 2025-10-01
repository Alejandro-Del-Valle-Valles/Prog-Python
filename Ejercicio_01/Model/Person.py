class Person:
    
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name: str):
        if isinstance(new_name, str) and new_name.strip():
            self._name = new_name
        else:
            raise ValueError("El nombre debe de ser un texto.")
        
    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, new_age: int):
        if isinstance(new_age, int) and new_age > 0:
            self._age = new_age
        else:
            raise ValueError("La edad debe ser superior a 0.")