import random
from Person import Person
from Repository import *

class Actions:
    
    def __ask_Name():
        name: str = ""
        while name.strip() == "":
            name = input("Ingrese el nombre de la persona: ")
        return name
    
    def create_Person():
        name = Actions.__ask_Name()
        person: Person = Person(name)
        if Repository.list_of_persons.__contains__(person):
            print("La persona ya existe")
        else:
            Repository.list_of_persons.append(person)
            print("Persona creada")
            
    def delete_Person():
        name = Actions.__ask_Name()
        person: Person = Person(name)
        if Repository.list_of_persons.__contains__(person):
            if person.get_status() == 1:
                index: int = Repository.list_of_persons.index(person)
                Repository.list_of_persons[index] = person.set_status(0)
                print("Persona eliminada")
            else:
                print("La persona ya está eliminada")
        else:
            print("La persona no existe.")
            
    def show_Persons():
        for person in Repository.list_of_persons:
            print(person)
            
    def do_raffle():
        actives: list = [p for p in Repository.list_of_persons if p.get_status() == 1]
        
        if not actives:
            print("No hay personas activas para rifar.")
            return

        try:
            index_selected_person: int = random.randint(0, len(actives) - 1)
            selected_person: Person = actives[index_selected_person]
            selected_person.set_status(3) 
            print(f"La persona ganadora es: {selected_person.get_name()}")

        except Exception as e:
            print(f"Ocurrió un error en la rifa: {e}")