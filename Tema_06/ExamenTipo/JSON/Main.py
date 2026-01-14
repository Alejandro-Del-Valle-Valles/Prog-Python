# Simulacor de examen con el examen tipo del aula virtual
from datetime import datetime
from Automovil import Automovil
from Vehiculo import Vehiculo
from Motocicleta import Motocicleta
import json

NOMBRE_JSON = "examen.json"
VEHICULOS_DICT = {}

def cargar_datos():
    try:
        with open(NOMBRE_JSON, "r") as fichero:
            datos = json.load(fichero)
            for vehiculo in datos:
                matricula = vehiculo["matricula"]
                marca = vehiculo["marca"]
                modelo = vehiculo["modelo"]
                anyo = vehiculo["anyo"]
                precio_base = vehiculo["precio_base"]
                try:
                    puertas = vehiculo["numero_puertas"]
                    tipo_combustible = vehiculo["tipo_combustible"]
                    automovil = Automovil(matricula, marca, modelo, anyo, precio_base, puertas, tipo_combustible)
                    VEHICULOS_DICT[matricula] = automovil
                except:
                    cilindrada = vehiculo["cilindrada"]
                    casco = vehiculo["tipo_casco_incluido"]
                    motocicleta = Motocicleta(matricula, marca, modelo, anyo, precio_base, cilindrada, casco)
                    VEHICULOS_DICT[matricula] = motocicleta
    except:
        print("Ha ocurrido un error inesperado al cargar los datos.")

def guardar_datos():
    try:
        datos = []
        for vehiculo in VEHICULOS_DICT.values():
            if isinstance(vehiculo, Automovil):
                datos.append({
                    "matricula": vehiculo.matricula,
                    "marca": vehiculo.marca,
                    "modelo": vehiculo.modelo,
                    "anyo": vehiculo.anyo,
                    "precio_base": vehiculo.precio_base,
                    "numero_puertas": vehiculo.numero_puertas,
                    "tipo_combustible": vehiculo.tipo_combustible
                })
            elif isinstance(vehiculo, Motocicleta):
                datos.append({
                    "matricula": vehiculo.matricula,
                    "marca": vehiculo.marca,
                    "modelo": vehiculo.modelo,
                    "anyo": vehiculo.anyo,
                    "precio_base": vehiculo.precio_base,
                    "cilindrada": vehiculo.cilindrada,
                    "tipo_casco_incluido": vehiculo.tipo_casco_inlcuido
                })
        with open(NOMBRE_JSON, "w") as fichero:
            json.dump(datos, fichero, indent=4)
        print("Datos guardados")
    except:
        print("Ha ocurrido un error al guardar los datos")

def crear_auto():
    try:
        matricula_correcta = False
        matricula: str
        while not matricula_correcta:
            matricula = preguntar_string_no_vacio("Introduce la mátrícula del vehículo (0000 AAA): ")
            matricula_correcta = Vehiculo.validar_matricula(matricula)
            if matricula_correcta and matricula not in VEHICULOS_DICT:
                break
            else:
                print("La matrícula no es correcta. Pruebe de nuevo")
                matricula_correcta = False
        marca = preguntar_string_no_vacio("Introduce la marca: ")
        modelo = preguntar_string_no_vacio("Introduce el modelo: ")
        anyo: int
        while True:
            anyo = preguntar_entero_positivo("Introduce el año de fabricación: ")
            if 1900 <= anyo <= datetime.now().year:
                break
            else:
                print("Debes introducir un año superior a 1899 e igual o inferior al actual.")
        precio_base = preguntar_precio()
        puertas = preguntar_entero_positivo("Introduce el numero de puertas: ", 2)
        combustible: str
        while True:
            combustible = preguntar_string_no_vacio("Introduce el tipo de combustible: ")
            if combustible in Automovil.TIPOS_COMBUISTIBLES:
                break
            else:
                print("Debes itroducir un tipo de combustible válido.")
        coche = Automovil(matricula, marca, modelo, anyo, precio_base, puertas, combustible)
        VEHICULOS_DICT[matricula] = coche
        guardar_datos()
    except:
        print("Error al crar el automovil")
    

def crear_moto():
    try:
        matricula_correcta = False
        matricula: str
        while not matricula_correcta:
            matricula = preguntar_string_no_vacio("Introduce la mátrícula del vehículo (0000 AAA): ")
            matricula_correcta = Vehiculo.validar_matricula(matricula)
            if matricula_correcta and matricula not in VEHICULOS_DICT:
                break
            else:
                matricula_correcta = False
                print("La matrícula no es correcta o ya está en uso. Pruebe de nuevo")
        marca = preguntar_string_no_vacio("Introduce la marca: ")
        modelo = preguntar_string_no_vacio("Introduce el modelo: ")
        anyo: int
        while True:
            anyo = preguntar_entero_positivo("Introduce el año de fabricación: ")
            if 1900 <= anyo <= datetime.now().year:
                break
            else:
                print("Debes introducir un año superior a 1899 e igual o inferior al actual.")
        precio_base = preguntar_precio()
        cilindrada = 2001
        while cilindrada > 2000:
            cilindrada = preguntar_entero_positivo("Introduce la cilindrada: ")
            if cilindrada > 2000:
                print("La cilindrada debe ser menor a 2000")
        casco: str
        while True:
            casco = preguntar_string_no_vacio("Introduce el tipo de casco: ")
            if casco in Motocicleta.TIPOS_CASCOS:
                break
            else:
                print("Debes itroducir un tipo de casco válido.")
        moto = Motocicleta(matricula, marca, modelo, anyo, precio_base, cilindrada, casco)
        VEHICULOS_DICT[matricula] = moto
        guardar_datos()
    except:
        print("Error al crar el mootcicleta")

#Opción 1
def crear_vehiculo():
    opcion: int
    while True:
        print("1. Automovil")
        print("2. Motocicleta")
        opcion = preguntar_entero_positivo("Introduce el vehículo que quieres crear: ")
        if opcion == 1:
            crear_auto()
            break
        elif opcion == 2:
            crear_moto()
            break
        else:
            print("Introduce una de las 2 opciones.")

#Opción 2
def listar_vehciulos():
    indice = 0
    for vehiculo in VEHICULOS_DICT.values():
        indice += 1
        print(f"{indice}. {vehiculo}")

#Opción 3
def actualizar_vehiculo():
    matricula: str
    while True:
        matricula = preguntar_string_no_vacio("Introduce la matrícula del vehículo a modificar: ")
        if Vehiculo.validar_matricula(matricula) and matricula in VEHICULOS_DICT:
            break
        else:
            print("La matrícula es incorrecta o no existe ningún vehiculo con esa matrícula.")
    vehiculo = VEHICULOS_DICT[matricula]
    opcion = 0
    while opcion < 1  or opcion > 8:
        print("Elige que quieres cambiar")
        print("1. Marca")
        print("2. Modelo")
        print("3. Precio")
        print("4. Anyo")
        if isinstance(vehiculo, Automovil):
            print("5. Nuermo de Puertas")
            print("6. Tipo de combustible")
            opcion = preguntar_entero_positivo("Elige una opción: ")
        elif isinstance(vehiculo, Motocicleta):
            print("5. Cilindrada")
            print("6. Tipo de casco")
            opcion = preguntar_entero_positivo("Elige una opción: ")
            if opcion == 5:
                opcion = 7
            elif opcion == 6:
                opcion = 8
    match opcion:
        case 1:
            vehiculo.marca = preguntar_string_no_vacio("Introduce la marca: ")
        case 2:
            vehiculo.modelo = preguntar_string_no_vacio("Introduce el modelo: ")
        case 3:
            anyo: int
            while True:
                anyo = preguntar_entero_positivo("Introduce el año de fabricación: ")
                if 1900 <= anyo <= datetime.now().year:
                    break
                else:
                    print("Debes introducir un año superior a 1899 e igual o inferior al actual.")
            vehiculo.anyo = anyo
        case 4:
            vehiculo.precio_base = preguntar_precio()
        case 5:
            if isinstance(vehiculo, Automovil):
                vehiculo.numero_puertas = preguntar_entero_positivo("Introduce el numero de puertas", 2)
        case 6:
            if isinstance(vehiculo, Automovil):
                combustible: str
                while True:
                    combustible = preguntar_string_no_vacio("Introduce el tipo de combustible: ")
                    if combustible in Automovil.TIPOS_COMBUISTIBLES:
                        break
                    else:
                        print("Debes itroducir un tipo de combustible válido.")
                vehiculo.tipo_combustible = combustible
        case 7:
            if isinstance(vehiculo, Motocicleta):
                cilindrada = 2001
                while cilindrada > 2000:
                    cilindrada = preguntar_entero_positivo("Introduce la cilindrada: ")
                    if cilindrada > 2000:
                        print("La cilindrada debe ser menor a 2000")
                vehiculo.cilindrada = cilindrada
        case 8:
            if isinstance(vehiculo, Motocicleta):
                casco: str
                while True:
                    casco = preguntar_string_no_vacio("Introduce el tipo de casco: ")
                    if casco in Motocicleta.TIPOS_CASCOS:
                        break
                    else:
                        print("Debes itroducir un tipo de casco válido.")
                vehiculo.tipo_casco_inlcuido = casco
    VEHICULOS_DICT[matricula] = vehiculo
    guardar_datos()

#Opción 4
def eliminar_vehiculo():
    matricula: str
    while True:
        matricula = preguntar_string_no_vacio("Introduce la matrícula del vehículo a eliminar: ")
        if Vehiculo.validar_matricula(matricula) and matricula in VEHICULOS_DICT:
            VEHICULOS_DICT.pop(matricula)
            guardar_datos()
            break
        else:
            print("La matrícula es incorrecta o no existe ningún vehiculo con esa matrícula.")

def preguntar_entero_positivo(mensaje, minimo = 0) -> int:
    numero: int
    while True:
        try:
            numero = int(input(mensaje))
            if numero > minimo:
                break
            else:
                print(f"El número debe ser mayor que {minimo}.")
        except ValueError:
            print("Debes introducir un número entero positivo.")
    return numero

def preguntar_string_no_vacio(mensaje) -> str:
    texto: str
    while True:
        texto = input(mensaje)
        if texto.strip != "":
            break
        else:
            print("Debe introducir un texto")
    return texto.strip()

def preguntar_precio() -> float:
    precio: float
    while True:
        try:
            precio = float(input("Introduce el precio base del vehículo: "))
            if precio >= 0:
                break
            else:
                print("El precio debe ser positivo")
        except:
            print("Debes introducir un valor numérico con decimales que sea positivo.")
    return precio

def ejecutar_acciones_menu_principal(opcion):
    match opcion:
        case 1:
            crear_vehiculo()
        case 2:
            listar_vehciulos()
        case 3:
            actualizar_vehiculo()
        case 4:
            eliminar_vehiculo()
        case _:
            print("La opción introducida no es válida.")

def main():
    try:
        print("1. Crear Vehículo")
        print("2. Listar Vehículos")
        print("3. Actualizar Vehículo")
        print("4. Eliminar Vehículo")
        print("5. Salir")

        opcion = preguntar_entero_positivo("Selecciona una opción: ")
        if opcion == 5:
            print("Fin del programa")
            return
        
        ejecutar_acciones_menu_principal(opcion)
        
        main()
    except:
        print("Ha ocurrido un error inesperado. Fin del programa.")

if __name__ == "__main__":
    cargar_datos()
    main()