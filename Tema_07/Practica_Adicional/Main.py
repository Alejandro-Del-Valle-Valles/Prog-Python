# Fichero principal de la practica
from datetime import date, datetime
from ErrorPersonalizado import ErrorPersonalizado
from Conexion import conectar, inicializar_tablas
from SolicitarDatos import SolicitarDatos

OPCIONES: tuple = ("Gestionar Opciones", "Gestionar Productos", "Gestionar Pedidos", "Gestionar Detalles Pedido")
COLOR_ROJO: str = "\033[31m" #Código del color rojo para los str.
COLOR_RESET: str = "\033[0m"

#MÉTODOS MENU
def manejar_menu(opcion: int):
    """
    Ejecuta el método correspondiente a la opción que se le pasa por parámetro
    Args:
        opcion (int): Opción elegida por el usuario, es el numero del metodo a ejecutar.
    """
    match(opcion) :
        case 0:
            print("Saliendo del programa...")
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case _:
            print(f"{COLOR_ROJO}La opción elegida no es válida{COLOR_RESET}")

def main():
    """
    Maneja el menú y la ejecución principal del programa.
    """
    conexion = None
    try: 
        conexion = conectar()
        if not conexion:
            raise ErrorPersonalizado("No se pudo conextar con la BBDD, finalizando programa.")
        inicializar_tablas(conexion)
        opcion = -1
        while opcion != 0:
            for i in range(len(OPCIONES)):
                print(f"{i + 1}. {OPCIONES[i]}")
            print("0. Salir")
            opcion = SolicitarDatos.pedir_numero_entero("Introduce una opción por favor: ")
            manejar_menu(opcion)
    except ErrorPersonalizado as ex:
        print(f"{COLOR_ROJO}{ex}{COLOR_RESET}")
    except:
        print(f"{COLOR_ROJO}Ha ocurrido un error inesperado. Se ha finalizado el programa.{COLOR_RESET}")
    finally:
        if conexion:
            conexion.close()

if __name__ == '__main__':
    main()