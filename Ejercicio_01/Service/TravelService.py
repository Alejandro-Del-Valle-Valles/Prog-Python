from Service import AskDataService
from Service import PersonService

def ask_To_Travel():
    if PersonService.person != None:
        distance: int = AskDataService.ask_Int("Introduce la distancia a la que quieres viajar (Km): ")
        if distance < 10:
            print("Ve andando.")
        else:
            if PersonService.person.age >= 18:
                print("Ve en coche.")
            else:
                print("Ve en bus.")
    else:
        print("Primero debes registrarte.")