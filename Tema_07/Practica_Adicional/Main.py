# Fichero principal de la practica
from datetime import date, datetime
from helpers.ErrorPersonalizado import ErrorPersonalizado
from helpers.Conexion import conectar, inicializar_tablas
from helpers.SolicitarDatos import SolicitarDatos
from managers.ClientesManager import menu_clientes
from managers.ProductosManager import menu_productos
from managers.PedidosManager import menu_pedidos
from managers.DetallesManager import menu_detalles
from helpers.Extensiones import printerr, limpiar_consola, pausa_y_limpia

OPCIONES: tuple = ("Gestionar Clientes", "Gestionar Productos", "Gestionar Pedidos", "Gestionar Detalles Pedido")

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
            pausa_y_limpia(3)
        case 1:
            limpiar_consola()
            menu_clientes()
            limpiar_consola()
        case 2:
            limpiar_consola()
            menu_productos()
            limpiar_consola()
        case 3:
            limpiar_consola()
            menu_pedidos()
            limpiar_consola()
        case 4:
            limpiar_consola()
            menu_detalles()
            limpiar_consola()
        case _:
            printerr("La opción elegida no es válida")

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
        printerr(ex)
    except:
        printerr("Ha ocurrido un error inesperado. Se ha finalizado el programa.")
    finally:
        if conexion:
            conexion.close()

if __name__ == '__main__':
    main()