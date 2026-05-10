from Productos import Producto
from ErrorPersonalizado import ErrorPersonalizado
from ClientesCRUD import ClientesCrud
from SolicitarDatos import SolicitarDatos
from Extensiones import printerr, pausa_y_limpia

__OPCIONES = ("Listar productos", "Crear producto", "Actualizar producto", "Eliminar producto")

def menu_productos():
    """
    Menú de gestión de datos de productos
    """
    try:
        opcion: int = -1
        while opcion != 0:
            for i in range(len(__OPCIONES)):
                print(f"{i + 1}. {__OPCIONES[i]}")
            print("0. Salir")
            opcion = SolicitarDatos.pedir_numero_entero("Introduce una opción por favor: ")
            __manejar_menu(opcion)
    except:
        printerr("Ha ocurrido un error inesperado mientras se administraban los productos. Volviendo al menu...")
        pausa_y_limpia(3)

def __manejar_menu(opcion: int):
    match opcion:
        case 0:
            print("Volviendo al menú...")
            pausa_y_limpia()
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case _:
            printerr("La opción elegida no es válida.")