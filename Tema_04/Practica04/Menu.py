from Actions import *

class Menu:
    __options_menu: tuple = ("Agregar Persona", "Eliminar Persona", 
                       "Mostrar Personas", "Lanzar Sorte0")
    
    def ask_Option() -> int:
        option: int
        while True:
            try:
                option = int(input("Ingrese una opción: "))
                if option >= 0:
                    break
                else:
                    print("Ingrese un númeor positivo")
            except:
                print()
        return option

    def show_menu():
        for i in range(len(Menu.__options_menu)):
            print(f"{i+1}. {Menu.__options_menu[i]}")
        print("0. Salir")
        
    def execute_menu_options(option: int):
        match option:
            case 0:
                print("Saliendo del programa...")
            case 1:
                Actions.create_Person()
            case 2:
                Actions.delete_Person()
            case 3:
                Actions.show_Persons()
            case 4:
                Actions.do_raffle()
            case _:
                print("Opción no válida")