"""
Práctica 03 de Python: Manejo de ficheros
Autor: Alejandro del Valle Vallés
"""
MENU_OPTIONS: tuple[str] = ("Conversión UTF-8 a Latin-1", "Conversión Latin-1 a UTF-8", 
                            "Conversión JSON a Longitud Fija.", "Conversión Longitud Fija a JSON")

def ask_menu_option() -> int:
    """
    Ask the user to input an option from the menu.
    
    :return: number of the selected option
    :rtype: int
    """
    option: int
    while True:
        try:
            option = int(input("Introduce una opción: "))
            if option > -1:
                break
            else:
                raise Exception
        except:
            print("La opción debe ser un número entero positivo.")
    return option

def ask_user_want_continue() -> bool:
    """
    Ask the user if want to continue with the acction.
    
    :return: True if they want to continue, False otherwise.
    :rtype: bool
    """
    response: str = ""
    while response != "si" and response != "no":
        try:
            response = input("¿Quieres continuar? (si/no): ").strip().lower()
            if response != "si" and response != "no":
                raise Exception
        except:
            print("La respuesta debe ser 'si' o 'no'.")
    return response == "si";
            


def execute_menu_option(option: int):
    """
    Execute the seleted option of the menu or notify if the option is invalid.
    
    :param option: number of the selected option.
    :type option: int
    """
    match option:
        case 0:
            print("Saliendo del programa...")
        case 1:
            convert_utf8_to_latin1()
        case 2:
            convert_latin1_to_utf8()
        case 3:
            convert_json_to_fixed_length()
        case 4:
            convert_fixed_length_to_json()
        case _:
            print("La opción introducia no es válida.")

def show_menu():
    """
    Show the options of the program.
    """
    i = 1
    for option in MENU_OPTIONS:
        print(f"{i}. {option}")
        i += 1
    print("0. Salir")

def convert_utf8_to_latin1():
    """
    Trasnform a file from UTF-8 to Latin-1 erasing all not supproted characters.
    """
    print("Antes de continuar, si el fichero contiene emojis u otros caracteres no sporotados por Latin-1 se eliminarán.")
    want_continue = ask_user_want_continue()
    if want_continue:
        pass
    else:
        print("Acción cancelada.")

def convert_latin1_to_utf8():
    """
    Trasnform a file from Latin-1 to UTF-8.
    """
    pass

def convert_json_to_fixed_length():
    """
    Trasnform a JSON file to a fixed length txt file.
    """
    pass

def convert_fixed_length_to_json():
    """
    Trasnform a fixed length txt file to a JSON file.
    """
    pass

def main():
    try:
        option: int = -1
        while option != 0:
            show_menu()
            option = ask_menu_option()
            execute_menu_option(option)
    except Exception as ex:
        print(f"Ha ocurrido un error inesperado durante la ejecución del programa: {ex}")

if __name__ == "__main__":
    main()