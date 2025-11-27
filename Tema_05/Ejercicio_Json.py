import json
import os

#MÉTODOS RELATIVOS AL MENÚ
opciones_menu = ("Alta", "Carga", "Salvado", "Listar")
personas: list[dict] = []

def preguntar_numero(pregunta: str = "Introduce una opción: ", esPositivo: bool = True) -> int:
    numero: int
    while True:
        try:
            numero = int(input(pregunta))
            if esPositivo and numero < 0:
                print("Debes introducir un número positivo.")
            else:
                break
        except:
            print("Debes introducir un número entero.")
            
    return numero

def mostrar_menu():
    i = 1
    for opcion in opciones_menu:
        print(f"{i}. {opcion}")
        i += 1
    print("0. Salir")
    
def ejecutar_opcion(opcion: int):
    match opcion:
        case 0:
            print("Saliendo...")
        case 1:
            alta()
        case 2:
            carga()
        case 3:
            salvado()
        case 4:
            listar()
        case _:
            print("Opción incorrecta.")
            
#MÉTODOS RELATIVOS A LAS ACCIONES
def alta():
    nombre: str = input("Introduce el nombre: ").strip().capitalize()
    edad: int = preguntar_numero("Introduce la edad: ")
    
    if nombre == "" or nombre == None:
        nombre = "Desconocido"
        
    personas.append({"nombre": nombre, "edad": edad})
    print(f"Se ha dado de alta a {nombre} con {edad} años.")
    

def carga():
    ruta = input("Introduce la ruta del fichero donde quieres guardar la información: ").strip()
    if ruta != "" or ruta != None:
        if ruta[-5:] == ".json":
            try:
                if os.path.exists(ruta):
                    with open(ruta, encoding="utf-8", mode="r") as f:
                        personas_existentes = json.load(f)
                        for persona in personas_existentes:
                            personas.append(persona)
                    print("Datos cargados correctamente.")
                else:
                    print("El fichero indicado no existe.")
            except:
                print("Ha oucrrido un error al extraer a las personas del fichero indicado.")

def salvado():
    ruta = input("Introduce la ruta del fichero donde quieres guardar la información: ").strip()
    if ruta != "" or ruta != None:
        if ruta[-5:] == ".json":
            try:
                if os.path.exists(ruta):
                    with open(ruta, encoding="utf-8", mode="r") as f:
                        personas_existentes = json.load(f)
                        for persona in personas_existentes:
                            personas.append(persona)
                            
                with open(ruta, encoding="utf-8", mode="w") as f:
                    json.dump(personas, f, indent=4)
                print("Se ha guardado la información correctamente en la ruta especificada.")
            except:
                print("Ha ocurrido un error al tratar de guardar la información.")
                print("Comprueba que la ruta sea correcta.")
        else:
            print("La ruta debe terminar en .json")
    else:
        print("Debe introducir una ruta.")

def listar():
    try:
        for persona in personas:
            print(f"{persona['nombre']} - {persona['edad']} años")
    except:
        print("Ha ocurrido un error al tratar de listar las personas.")

#MAIN
def main():
    try:
        opcion: int = -1;
        while opcion != 0:
            mostrar_menu()
            opcion = preguntar_numero("Introduce una opción: ", False)
            ejecutar_opcion(opcion)
    except:
        print("Ha ocurrido un error inesperado durante la ejecución. Finalizando el programa.")

if __name__ == '__main__':
    main()