"""
Práctica 03 de Python: Manejo de ficheros
Autor: Alejandro del Valle Vallés
"""

import os
import Files.detectar_codif as detect_codf
from pathlib import Path
import json

MENU_OPTIONS: tuple[str] = ("Conversión UTF-8 a Latin-1", "Conversión Latin-1 a UTF-8", 
                            "Conversión JSON a Longitud Fija.", "Conversión Longitud Fija a JSON")
FILES_PATH: str = Path("Files").absolute()

# QUESTION METHODS

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
    clean_console()
    return response == "si";
            
def ask_file_path() -> str:
    """
    Ask the user to introduce a path. It can be absoluthe or variable path.
    Returns:
        str: absolute path 
    """
    response: str = ""
    path: Path
    while response == "":
        try:
            response = input("Introduce la ruta del fichero: ").strip()
            clean_console()
            if response == "":
                raise Exception
            
            path = Path(response)
            if not path.exists() or not path.is_file():
                raise Exception
            response = path.absolute()
        except:
            print("La ruta del fichero no puede estar vacía, tiene que existir y ser un fichero.")
    return response

# MENU METHODS

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
    
def clean_console():
    """
    Clean the console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    
# CONVERT METHDOS

def convert_file(origin_encode: str, target_encode: str, origin_path: str, target_path: str) -> bool:
    encoded: bool
    
    try:
        with open(origin_path, 'r', encoding=origin_encode) as file_in:
            content = file_in.read()

        with open(target_path, 'w', encoding=target_encode, errors="ignore") as file_out:
            file_out.write(content)
        encoded = True
    except:
        encoded = False
        
    return encoded

def convert_utf8_to_latin1():
    """
    Trasnform a file from UTF-8 to Latin-1 erasing all not supproted characters.
    """
    print("Antes de continuar, si el fichero contiene emojis u otros caracteres no sporotados por Latin-1 se eliminarán.")
    want_continue = ask_user_want_continue()
    if want_continue:
        file_path = ask_file_path()
        name, ext = os.path.splitext(file_path)
        output_filepath = f"{name}_latin1{ext}"
        encoded = convert_file("utf-8", "latin-1", file_path, output_filepath)
        if encoded:
            print(f"Se ha convertido correctamente en {FILES_PATH}/{output_filepath}")
        else:
            print("No se ha podido convertir el fichero.")
    else:
        print("Acción cancelada.")

def convert_latin1_to_utf8():
    """
    Trasnform a file from Latin-1 to UTF-8.
    """
    file_path = ask_file_path()
    name, ext = os.path.splitext(file_path)
    output_filepath = f"{name}_utf8{ext}"
    encoded = convert_file("latin-1", "utf-8", file_path, output_filepath)
    if encoded:
        print(f"Se ha convertido correctamente en {FILES_PATH}/{output_filepath}")
    else:
        print("No se ha podido convertir el fichero.")

def convert_json_to_fixed_length():
    """
    Trasnform a JSON file to a fixed length txt file.
    Number of Characters
    Nombre: 10
    Apellidos: 30
    Edad: 3
    Nombre usuario: 10
    Telefono: 15
    Contraseña: 20
    Dirección: 80
    """
    file_path = ask_file_path()
    if file_path[::-5] == ".json":
        pass
    else:
        print("El fichero no es un fichero JSON.")

def convert_fixed_length_to_json():
    """
    Trasnform a fixed length txt file to a JSON file.
    """
    file_path = ask_file_path()
    if file_path[::-4] == ".txt":
        with open(file_path, 'r', encoding=detect_codf.detectar_codificacion(file_path)) as file:
            for line in file:
                print(line)
    else:
        print("El fichero no es un fichero de longitud fija.")

# MAIN

def main():
    try:
        option: int = -1
        while option != 0:
            show_menu()
            option = ask_menu_option()
            clean_console()
            execute_menu_option(option)
    except Exception as ex:
        print(f"Ha ocurrido un error inesperado durante la ejecución del programa: {ex}")

if __name__ == "__main__":
    main()