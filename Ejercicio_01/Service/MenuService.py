
__list_Of_Main_Options = ("Registro", "Viaje")
__exit_Option = "0. Salir"

def show_menu():
    i = 1
    for option in __list_Of_Main_Options:
        print(f"{i}. {option}: ")
        i += 1
    print(__exit_Option)
    