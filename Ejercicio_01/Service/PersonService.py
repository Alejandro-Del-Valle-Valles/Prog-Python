from Service import AskDataService
from Model.Person import Person

person: Person = None

def registration():
    global person
    name: str = AskDataService.ask_String("Introduce el nombre de la persona: ")
    age: int = AskDataService.ask_Int("Introduce la edad de la persona: ");
    person = Person(name, age)