#SOLUCIÓN CON JSON
import json
from pathlib import Path
from Menu import Menu
from Mago import Mago

__NOMBRE_JSON = "magos.json"
DICCIONARIO_MAGOS = {} #Nombre clave, Mago valor

def cargar_magos():
    try:
        with open(__NOMBRE_JSON, "r", encoding="utf-8") as archivo:
            magos = json.load(archivo)
            for mago in magos:
                nombre = mago["nombre"]
                edad = mago["edad"]
                sangre = mago["sangre"]
                casa = mago["casa"]
                nota_media = mago["nota_media"]
                DICCIONARIO_MAGOS[nombre] = Mago(nombre, edad, sangre, casa, nota_media)
    except FileNotFoundError:
        print("El fichero con los magos no se ha encontrado.")
    except Exception as ex:
        print(f"Ha ocurrido un error al cargar los magos: {ex}")

def registrar_mago():
    nombre = pedir_str("Ingrese el nombre del mago: ").strip()
    if nombre in DICCIONARIO_MAGOS:
        print(f"{nombre} ya existe.")
    elif len(nombre.split(' ')) != 1:
        print("El nombre del mago no puede contener espacios.")
    else:
        edad = pedir_numero_entero("Ingrese la edad del mago: ")
        sangre = pedir_str("Ingrese la sangre del mago: ")
        casa = pedir_str("Ingrese la casa del mago: ")
        nota_media = pedir_nota()
        mago = Mago(nombre, edad, sangre, casa, nota_media)
        DICCIONARIO_MAGOS[nombre] = mago
        print(f"{nombre} ha sido registrado con éxito.")

def listar_magos():
    for mago in DICCIONARIO_MAGOS.values():
        print(mago)

def expulsar_mago():
    nombre = pedir_str("Ingrese el nombre del mago: ")
    if nombre not in DICCIONARIO_MAGOS:
        print(f"{nombre} no existe.")
    else:
        del DICCIONARIO_MAGOS[nombre]
        print(f"{nombre} ha sido expulsado con éxito.")

def enfrentar_magos():
    mago_uno: Mago
    mago_dos: Mago
    while True:
        nombres = pedir_str("Ingrese el nombre de los dos magos separados por un espacio: ").strip().split(" ")
        if len(nombres) == 2:
            nombre_uno = nombres[0]
            nombre_dos = nombres[1]
            if nombre_uno in DICCIONARIO_MAGOS and nombre_dos in DICCIONARIO_MAGOS:
                mago_uno = DICCIONARIO_MAGOS[nombre_uno]
                mago_dos = DICCIONARIO_MAGOS[nombre_dos]
                Mago.enfrentar(mago_uno, mago_dos)
                break
            elif nombre_uno not in DICCIONARIO_MAGOS:
                print(f"{nombre_uno} no existe.")
            else:
                print(f"{nombre_dos} no existe.")
        else:
            print("Introduce solo dos magos.")

def modificar_mago():
    nombre = pedir_str("Ingrese el nombre del mago: ")
    if nombre not in DICCIONARIO_MAGOS:
        print(f"{nombre} no existe.")
    elif len(nombre.split(' ')) != 1:
        print("El nombre del mago no puede contener espacios.")
    else:
        edad = pedir_numero_entero("Ingrese la edad del mago: ")
        sangre = pedir_str("Ingrese la sangre del mago: ")
        casa = pedir_str("Ingrese la casa del mago: ")
        nota_media = pedir_nota()
        mago = Mago(nombre, edad, sangre, casa, nota_media)
        DICCIONARIO_MAGOS[nombre] = mago
        print(f"{nombre} ha sido modificado con éxito.")

def salir():
    try:
        with open(__NOMBRE_JSON, "w", encoding="utf-8") as archivo:
            magos = []
            for mago in DICCIONARIO_MAGOS.values():
                magos.append({
                    "nombre": mago.nombre,
                    "edad": mago.edad,
                    "sangre": mago.sangre,
                    "casa": mago.casa,
                    "nota_media": mago.nota_media
                })
            json.dump(magos, archivo, ensure_ascii=False, indent=4)
    except Exception as ex:
        print(f"Ha ocurrido un error al guardar los magos: {ex}")
    print("Saliendo...")

def ejecutar_opcion(opcion):
    match opcion:
        case 0:
            salir()
        case 1:
            registrar_mago()
        case 2:
            listar_magos()
        case 3:
            enfrentar_magos()
        case 4:
            expulsar_mago()
        case 5:
            modificar_mago()
        case _:
            print("Opción no válida")

def pedir_str(mensaje):
    cadena: str
    while True:
        cadena = input(mensaje)
        if cadena.strip() != "":
            break
        else:
            print("Por favor, ingrese una cadena válida.")
    return cadena

def pedir_numero_entero(mensaje):
    numero: int
    while True:
        try:
            numero = int(input(mensaje))
            if numero >= 0:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")
    return numero

def pedir_nota():
    numero: float
    while True:
        try:
            numero = float(input("Ingrese la nota media del curso: "))
            if 0 <= numero <= 10:
                break
        except ValueError:
            print("Por favor, ingrese una nota válida que esté entre 0 y 10.")
    return numero

def main():
    try:
        cargar_magos()
        opcion = -1
        while opcion != 0:
            Menu.mostrar_menu()
            opcion = pedir_numero_entero("Ingrese una opción: ")
            ejecutar_opcion(opcion)

    except Exception as ex:
        print(f"Ha ocurrido un error inesperado: {ex}")
        salir()

if __name__ == '__main__':
    main()