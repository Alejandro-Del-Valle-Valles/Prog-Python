class Person:
    def __init__(self, name: str, status: int = 1):
        self.set_name(name)
        self.__status = status

    def __str__(self) -> str:
        return f"Name: {self.__name}, Is_Active: {self.__status}"
    
    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, name:str):
        self.__name = name.strip().capitalize()
        
    def get_status(self) -> int:
        """0 is not active, 1 is active, 2 is winner.

        Returns:
            int: 0 is not active, 1 is active, 2 is winner.
        """
        return self.__status
    
    def set_status(self, status: int):
        if status in range(0, 3):
            self.__status = status
        else:
            self.__status = 0
            print("Invalid status")
        
    def __eq__(self, other) -> bool:
        return self.__name == other.__name
    
    def __hash__(self) -> int:
        return hash(self.__name)