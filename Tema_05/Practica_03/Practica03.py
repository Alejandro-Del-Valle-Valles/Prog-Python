"""
Práctica 03 de Python: Manejo de ficheros
Autor: Alejandro del Valle Vallés
"""

import os
import detectar_codif as detect_codf
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
            
def ask_file_path() -> Path:
    """
    Ask the user to introduce a path. It can be absoluthe or variable path.
    Returns:
        Path: absolute path 
    """
    path: Path = None
    while path is None:
        try:
            response = input("Introduce la ruta del fichero: ").strip()
            clean_console()
            if response == "":
                raise Exception("El fichero no puede estar vacío.")
            
            path = Path(response)
            if not path.exists() or not path.is_file():
                raise Exception("El fichero debe existir.")
            path = path.absolute()
        except Exception as ex:
            print(ex)
    return path

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

def convert_file(origin_encode: str, target_encode: str, origin_path: Path, target_path: Path) -> bool:
    """
    Convert one file from one encoding to another. It creates a new file with the name of the new encoding in the same Directory of the original file.
    
    :param origin_encode: encode of the original file
    :type origin_encode: str
    :param target_encode: encode for the new file
    :type target_encode: str
    :param origin_path: path of the original file
    :type origin_path: Path
    :param target_path: path of the new file
    :type target_path: Path
    :return: bool if it was created or not.
    :rtype: bool
    """
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

def fixed_str(text: str, length: int) -> str:
    """
    Trasnform a str to a specific length. If is samller, it will put spaces, else it will be cuted.
    
    :param text: text to tranasform
    :type text: str
    :param length: length of the new text
    :type length: int
    :return: fixed str with the specified length
    :rtype: str
    """
    return text.ljust(length)[:length]

def convert_utf8_to_latin1():
    """
    Trasnform a file from UTF-8 to Latin-1 erasing all not supproted characters.
    """
    print("Antes de continuar, si el fichero contiene emojis u otros caracteres no sporotados por Latin-1 se eliminarán.")
    want_continue = ask_user_want_continue()
    if want_continue:
        file_path = ask_file_path()
        output_filepath = f"{file_path.stem}_latin1{file_path.suffix}"
        encoded = convert_file("utf-8", "latin-1", file_path, output_filepath)
        if encoded:
            print(f"Se ha convertido correctamente en {output_filepath}")
        else:
            print("No se ha podido convertir el fichero.")
    else:
        print("Acción cancelada.")

def convert_latin1_to_utf8():
    """
    Trasnform a file from Latin-1 to UTF-8.
    """
    file_path = ask_file_path()
    output_filepath = f"{file_path.stem}_utf8{file_path.suffix}"
    encoded = convert_file("latin-1", "utf-8", file_path, output_filepath)
    if encoded:
        print(f"Se ha convertido correctamente en {output_filepath}")
    else:
        print("No se ha podido convertir el fichero.")

def convert_json_to_fixed_length():
    """
    Trasnform a JSON file to a fixed length txt file.
    Number of Characters
    Nombre: 10
    Apellidos: 30
    Edad: 3
    Usuario: 10
    Telefono: 15
    Clave: 20
    Dirección: 80
    """
    file_path = ask_file_path()
    if file_path.suffix == ".json":
        try:
            json_data: list[dict]
            with open(file_path, 'r', encoding=detect_codf.detectar_codificacion(file_path)) as file:
                json_data = json.load(file)
            
            new_name = f"{file_path.stem}_to_fixed.txt"
            with open(file_path.with_name(new_name), 'w', encoding='utf-8') as file:
                for user in json_data:
                    line = f"{fixed_str(user.get('Nombre', ''), 10)} {fixed_str(user.get('Apellidos', ''), 30)} {fixed_str(user.get('Edad', ''), 3)} {fixed_str(user.get('Usuario', ''), 10)} {fixed_str(user.get('Telefono', ''), 15)} {fixed_str(user.get('Clave', ''), 20)} {fixed_str(user.get('Direccion', ''), 80)}\n"
                    file.write(line)
            print("Fichero creado correcatmente. Lo puedes encontrar en la misma carpeta del fichero original.")
        except (FileNotFoundError, IndexError, Exception) as ex:
            print(f"Ha ocurrido un error al leer/serializar: {ex}")
    else:
        print("El fichero no es un fichero JSON.")

def convert_fixed_length_to_json():
    """
    Trasnform a fixed length txt file to a JSON file.
    """
    file_path: Path = ask_file_path()
    if file_path.suffix == ".txt":
        data: list[str] = []
        json_data = []
        try:
            with open(file_path, 'r', encoding=detect_codf.detectar_codificacion(file_path)) as file:
                for line in file:
                    data = [item for item in line.strip().split(" ") if item]
                    json_data.append({
                        "Nombre": data[0],
                        "Apellidos": data[1],
                        "Edad": data[2],
                        "Usuario": data[3],
                        "Telefono": data[4],
                        "Clave": data[5],
                        "Direccion": data[6]
                    })
            new_name = f"{file_path.stem}_converted_to_json.json"
            with open(file_path.with_name(new_name), 'w', encoding='utf-8') as json_file:
                json.dump(json_data, json_file, ensure_ascii=False, indent=4)
            print("El fichero se ha convertido correctamente. Lo encontrarás en la misma ruta.")
        except (FileNotFoundError, IndexError, Exception) as ex:
            print(f"Ha ocurrido un error al leer/serializar: {ex}")
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