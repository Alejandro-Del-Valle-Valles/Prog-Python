#Ejercicio propuesto en clase

from Menu import Menu
from Persona import Persona

dict_personas: dict[str, Persona] = {}

def preguntar_numero(pregunta: str) -> int:
    numero: int
    while True:
        try:
            numero = int(input(pregunta))
            if numero >= 0:
                break
        except ValueError:
            print(f"Debes introducir un número. ")
    return numero

def preguntar_str(pregunta: str) -> str:
    texto: str
    while True:
        texto = input(pregunta)
        if texto.strip() != "":
            break
        else:
            print("Debes introducir un texto.")
    return texto

def preguntar_condiciones(pregunta: str, confirmar: str = "Si", cancelar: str = "No") -> bool:
    respuesta: bool
    while True:
        respuesta = input(pregunta)
        if respuesta.lower() == confirmar.lower():
            respuesta = True
            break
        elif respuesta.lower() == cancelar.lower():
            respuesta = False
            break
        else:
            print(f"Debes introducir '{confirmar}' o '{cancelar}'.")
    return respuesta

def alta_persona():
    dni = preguntar_str("Introduce el DNI con letra: ")
    if(dni in dict_personas):
        print("Ya existe una persona con ese DNI.")
        return
    nombre = preguntar_str("Introduce el nombre: ")
    apellido = preguntar_str("Introduce el apellido: ")
    edad = preguntar_numero("Introduce la edad: ")
    tlf = preguntar_str("Introduce el teléfono: ")
    persona = Persona(dni, nombre, apellido, edad, tlf)
    dict_personas[dni] = persona
    print("Persona agregada correctamente.")

def listar_personas():
    if len(dict_personas) == 0:
        print("No hay personas registradas.")
        return
    for persona in dict_personas.values():
        print(persona)

def baja_persona():
    if len(dict_personas) == 0:
        print("No hay personas registradas.")
        return
    
    dni = preguntar_str("Introduce el DNI de la persona a dar de baja: ")
    if(dni not in dict_personas):
        print("No existe una persona con ese DNI.")
        return
    
    if(preguntar_condiciones(f"¿Estás seguro de que quieres dar de baja a la persona con DNI {dni}?(Si/No): ")):
        del dict_personas[dni]
        print("Persona eliminada correctamente.")
    else:
        print("Operación cancelada.")

def modificar_persona():
    if len(dict_personas) == 0:
        print("No hay personas registradas.")
        return
    
    dni = preguntar_str("Introduce el DNI de la persona a modificar: ")
    if(dni not in dict_personas):
        print("No existe una persona con ese DNI.")
        return
    
    print("Datos de la persona a modificar:")
    print(dict_personas[dni])
    nombre = preguntar_str("Introduce el nuevo nombre: ")
    apellido = preguntar_str("Introduce el nuevo apellido: ")
    edad = preguntar_numero("Introduce la nueva edad: ")
    tlf = preguntar_str("Introduce el teléfono: ")
    persona = Persona(dni, nombre, apellido, edad, tlf)
    if(preguntar_condiciones("¿Estás seguro de que quieres modificar a la persona?(Si/No): ")):
        dict_personas[dni] = persona
        print("Persona modificada correctamente.")
    else:
        print("Acción cancelada.")


def ejecutar_opcion(option: int):
    match option:
        case 0:
            print("Saliendo del programa...")
        case 1:
            alta_persona()
        case 2:
            listar_personas()
        case 3:
            baja_persona()
        case 4:
            modificar_persona()
        case _:
            print("Opción no válida")

def main():
    opcion = -1
    while opcion != 0:
        Menu.show_menu()
        opcion = int(input("Elige una opción: "))
        ejecutar_opcion(opcion)


if __name__ == '__main__':
    main()