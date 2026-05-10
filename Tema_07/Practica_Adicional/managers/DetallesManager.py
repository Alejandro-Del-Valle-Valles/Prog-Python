from models.DetallesPedido import DetallePedido
from helpers.ErrorPersonalizado import ErrorPersonalizado
from repository.DetallesPedidoRepository import DetallesPedidoCRUD
from helpers.SolicitarDatos import SolicitarDatos
from helpers.Extensiones import printerr, pausa_y_limpia, enter_limpiar

__OPCIONES = ("Listar detalles", "Crear detalle", "Actualizar detalle", "Eliminar detalle")

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
            opcion = SolicitarDatos.pedir_numero_entero("Introduce una opción por favor: ", es_positivo=True)
            __manejar_menu(opcion)
    except:
        printerr("Ha ocurrido un error inesperado mientras se administraban los detalles. Volviendo al menu...")
        pausa_y_limpia(3)

def __manejar_menu(opcion: int):
    match opcion:
        case 0:
            print("Volviendo al menú...")
            pausa_y_limpia()
        case 1:
            __listar_detalles()
        case 2:
            __crear_detalle()
        case 3:
            __actualizar_detalle()
        case 4:
            __eliminar_detalle()
        case _:
            printerr("La opción elegida no es válida.")

def __listar_detalles():
    """
    Lista los detalles
    """
    try:
        detalles = DetallesPedidoCRUD.get_all()
        if not detalles:
            print("No hay detalles registrados.")
        else:
            for detalle in detalles:
                print(detalle)
    except Exception as ex:
        printerr(f"Error al listar: {ex}")
    enter_limpiar()

def __crear_detalle():
    """
    Crea un nuevo detalle
    """
    try:
        id_pedido = SolicitarDatos.pedir_numero_entero("Introduce el ID del pedido: ", es_positivo=True, permitir_nulo=False)
        id_producto = SolicitarDatos.pedir_numero_entero("Introduce el ID del producto: ", es_positivo=True, permitir_nulo=False)
        cantidad = SolicitarDatos.pedir_numero_entero("Introduce la cantidad: ", es_positivo=True, permitir_nulo=False)
        subtotal = SolicitarDatos.pedir_numero_decimal("Introduce el subtotal: ", es_positivo=True, permitir_nulo=False)
        
        detalle = DetallePedido(id_pedido=id_pedido, id_producto=id_producto, cantidad=cantidad, subtotal=subtotal)
        
        if DetallesPedidoCRUD.create_detalle(detalle):
            print("Detalle creado correctamente.")
        else:
            printerr("No se pudo crear el detalle. Verifica que los IDs de pedido y producto existan.")
    except (ErrorPersonalizado, ValueError) as ex:
        printerr(ex)
    enter_limpiar()

def __actualizar_detalle():
    """
    Actualiza un detalle. Si un campo se deja en blanco no se actualiza ese campo
    """
    try:
        id_detalle = SolicitarDatos.pedir_numero_entero("Introduce el ID del detalle a actualizar: ", es_positivo=True, permitir_nulo=False)
        detalle_actual = DetallesPedidoCRUD.get_by_id(id_detalle)
        
        if not detalle_actual:
            raise ErrorPersonalizado("El detalle indicado no existe.")
        
        print("Deja en blanco los campos que no desees modificar:")
        
        cantidad_str = SolicitarDatos.pedir_str(f"Cantidad actual ({detalle_actual.cantidad}): ", permitir_vacio=True)
        subtotal_str = SolicitarDatos.pedir_str(f"Subtotal actual ({detalle_actual.subtotal}€): ", permitir_vacio=True)

        cantidad_final = int(cantidad_str) if cantidad_str else detalle_actual.cantidad
        subtotal_final = float(subtotal_str) if subtotal_str else detalle_actual.subtotal

        detalle_modificado = DetallePedido(
            id_pedido=detalle_actual.id_pedido, 
            id_producto=detalle_actual.id_producto, 
            cantidad=cantidad_final, 
            subtotal=subtotal_final, 
            id_detalle=id_detalle
        )
        
        if DetallesPedidoCRUD.update_detalle(detalle_modificado):
            print("Detalle actualizado correctamente.")
        else:
            printerr("No se pudo actualizar el detalle.")
    except (ErrorPersonalizado, ValueError) as ex:
        printerr(f"Error en los datos introducidos: {ex}")
    enter_limpiar()

def __eliminar_detalle():
    """
    Elimina un detalle por su ID
    """
    try:
        id_detalle = SolicitarDatos.pedir_numero_entero("Introduce el ID del detalle a eliminar: ", es_positivo=True, permitir_nulo=False)
        if DetallesPedidoCRUD.delete_detalle(id_detalle):
            print("Detalle eliminado correctamente.")
        else:
            printerr("No se pudo eliminar el detalle. Es posible que el ID no exista.")
    except ErrorPersonalizado as ex:
        printerr(ex)
    enter_limpiar()