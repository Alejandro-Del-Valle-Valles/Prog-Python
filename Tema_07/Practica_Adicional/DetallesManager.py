from DetallesPedido import DetallePedido
from ErrorPersonalizado import ErrorPersonalizado
from ClientesCRUD import ClientesCrud
from SolicitarDatos import SolicitarDatos
from Extensiones import printerr, pausa_y_limpia

__OPCIONES = ("Listar detalles", "Crear detalles", "Actualizar detalles", "Eliminar detalles")

def menu_detalles():
    """
    Menú de gestión de datos de detalles de pedidos
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
        printerr("Ha ocurrido un error inesperado mientras se administraban los pedidos. Volviendo al menu...")
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