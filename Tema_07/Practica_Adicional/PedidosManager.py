from Pedidos import Pedido
from ErrorPersonalizado import ErrorPersonalizado
from ClientesCRUD import ClientesCrud
from SolicitarDatos import SolicitarDatos
from Extensiones import printerr, pausa_y_limpia, enter_limpiar
from PedidosCRUD import PedidosCRUD
from datetime import date

__OPCIONES = ("Listar pedidos", "Crear pedidos", "Actualizar pedidos", "Eliminar pedidos")

def menu_pedidos():
    """
    Menú de gestión de datos de pedidos
    """
    try:
        opcion: int = -1
        while opcion != 0:
            for i in range(len(__OPCIONES)):
                print(f"{i + 1}. {__OPCIONES[i]}")
            print("0. Salir")
            opcion = SolicitarDatos.pedir_numero_entero("Introduce una opción por favor: ")
            __manejar_menu(opcion)
    except Exception as ex:
        printerr("Ha ocurrido un error inesperado mientras se administraban los pedidos. Volviendo al menu...")
        pausa_y_limpia(3)

def __manejar_menu(opcion: int):
    match opcion:
        case 0:
            print("Volviendo al menú...")
            pausa_y_limpia()
        case 1:
            __listar_pedidos()
        case 2:
            __crear_pedido()
        case 3:
            __actualizar_pedido()
        case 4:
            __eliminar_pedido()
        case _:
            printerr("La opción elegida no es válida.")

def __listar_pedidos():
    try:
        pedidos = PedidosCRUD.get_all()
        if len(pedidos) == 0:
            print("No hay pedidos registrados.")
        else:
            for pedido in pedidos:
                print(pedido)
    except ErrorPersonalizado as ex:
        printerr(ex)
    enter_limpiar()

def __crear_pedido():
    try:
        id_cliente = SolicitarDatos.pedir_numero_entero("Introduce el ID del cliente:", es_positivo=True, permitir_nulo=False)
        fecha = SolicitarDatos.pedir_fecha("Introduce la fecha del pedido:", fecha_maxima=date.today())
        total = SolicitarDatos.pedir_numero_decimal("Introduce el total del pedido:", es_positivo=True, permitir_nulo=False)
        
        pedido = Pedido(id_cliente=id_cliente, fecha=fecha, total=total)
        if PedidosCRUD.create_pedido(pedido):
            print("Pedido creado correctamente.")
        else:
            printerr("No se pudo crear el pedido.")
    except ErrorPersonalizado as ex:
        printerr(ex)
    except ValueError as ex:
        printerr(ex)
    enter_limpiar()

def __actualizar_pedido():
    try:
        id_pedido = SolicitarDatos.pedir_numero_entero("Introduce el ID del pedido a actualizar:", es_positivo=True, permitir_nulo=False)
        pedido = PedidosCRUD.get_by_id(id_pedido)
        if pedido == None:
            raise ErrorPersonalizado("El pedido no existe.")
        fecha = SolicitarDatos.pedir_fecha("Introduce la nueva fecha del pedido:", fecha_maxima=date.today())
        total = SolicitarDatos.pedir_numero_decimal("Introduce el nuevo total del pedido:", es_positivo=True)

        pedido = Pedido(id_cliente=pedido.id_cliente, fecha=fecha, total=total, id_pedido=id_pedido)
        if PedidosCRUD.update_pedido(pedido):
            print("Pedido actualizado correctamente.")
        else:
            printerr("No se pudo actualizar el pedido. Es posible que el ID no exista.")
    except ErrorPersonalizado as ex:
        printerr(ex)
    except ValueError as ex:
        printerr(ex)
    enter_limpiar()

def __eliminar_pedido():
    try:
        id_pedido = SolicitarDatos.pedir_numero_entero("Introduce el ID del pedido a eliminar:", es_positivo=True)
        if PedidosCRUD.delete_pedido(id_pedido):
            print("Pedido eliminado correctamente.")
        else:
            printerr("No se pudo eliminar el pedido. Es posible que el ID no exista.")
    except ErrorPersonalizado as ex:
        printerr(ex)
    enter_limpiar()