from models.Clientes import Cliente
from helpers.ErrorPersonalizado import ErrorPersonalizado
from repository.ClientesRepository import ClientesCrud
from helpers.SolicitarDatos import SolicitarDatos
from helpers.Extensiones import printerr, pausa_y_limpia, enter_limpiar

__OPCIONES = ("Listar clientes", "Crear cliente", "Actualizar cliente", "Eliminar cliente")

def menu_clientes():
    """
    Menú de gestión de datos de clientes
    """
    try:
        opcion: int = -1
        while opcion != 0:
            for i in range(len(__OPCIONES)):
                print(f"{i + 1}. {__OPCIONES[i]}")
            print("0. Salir")
            opcion = SolicitarDatos.pedir_numero_entero("Introduce una opción por favor: ", es_positivo=True)
            __manejar_menu(opcion)
    except Exception:
        printerr("Ha ocurrido un error inesperado mientras se administraban los clientes. Volviendo al menu...")
        pausa_y_limpia(3)

def __manejar_menu(opcion: int):
    match opcion:
        case 0:
            print("Volviendo al menú...")
            pausa_y_limpia()
        case 1:
            __listar_clientes()
        case 2:
            __crear_cliente()
        case 3:
            __actualizar_cliente()
        case 4:
            __eliminar_cliente()
        case _:
            printerr("La opción elegida no es válida.")

def __listar_clientes():
    """
    Muestra todos los clientes de la BBDD
    """
    try:
        clientes = ClientesCrud.get_all()
        if not clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in clientes:
                print(cliente)
    except Exception as ex:
        printerr(f"Error al listar: {ex}")
    enter_limpiar()

def __crear_cliente():
    """
    Crea un nuevo cliente
    """
    try:
        nombre = SolicitarDatos.pedir_str("Introduce el nombre (max 100): ", longitud_maxima=100)
        email = SolicitarDatos.pedir_str("Introduce el email (max 150): ", longitud_maxima=150)
        telefono = SolicitarDatos.pedir_str("Introduce el teléfono (max 20): ", longitud_maxima=20)
        
        cliente = Cliente(nombre=nombre, email=email, telefono=telefono)
        
        if ClientesCrud.create_cliente(cliente):
            print("Cliente creado correctamente.")
        else:
            printerr("No se pudo crear el cliente.")
    except (ErrorPersonalizado, ValueError) as ex:
        printerr(ex)
    enter_limpiar()

def __actualizar_cliente():
    """
    Actualiza los datos introducidos del clientes. Si un dato no es introducido no se modifica.
    """
    try:
        id_cliente = SolicitarDatos.pedir_numero_entero("Introduce el ID del cliente a actualizar: ", es_positivo=True, permitir_nulo=False)
        cliente_actual = ClientesCrud.get_by_id(id_cliente)
        
        if not cliente_actual:
            raise ErrorPersonalizado("El cliente indicado no existe.")
        
        print("Deja en blanco los campos que no desees modificar:")
        nombre = SolicitarDatos.pedir_str(f"Nombre actual ({cliente_actual.nombre}): ", longitud_maxima=100, permitir_vacio=True)
        email = SolicitarDatos.pedir_str(f"Email actual ({cliente_actual.email}): ", longitud_maxima=150, permitir_vacio=True)
        telefono = SolicitarDatos.pedir_str(f"Teléfono actual ({cliente_actual.telefono}): ", longitud_maxima=20, permitir_vacio=True)

        nombre_final = nombre if nombre else cliente_actual.nombre
        email_final = email if email else cliente_actual.email
        telefono_final = telefono if telefono else cliente_actual.telefono

        cliente_modificado = Cliente(nombre=nombre_final, email=email_final, telefono=telefono_final, id=id_cliente)
        
        if ClientesCrud.update_cliente(cliente_modificado):
            print("Cliente actualizado correctamente.")
        else:
            printerr("No se pudo actualizar el cliente.")
    except (ErrorPersonalizado, ValueError) as ex:
        printerr(ex)
    enter_limpiar()

def __eliminar_cliente():
    """
    Elimina el cliente especificado
    """
    try:
        id_cliente = SolicitarDatos.pedir_numero_entero("Introduce el ID del cliente a eliminar: ", es_positivo=True, permitir_nulo=False)
        if ClientesCrud.delete_cliente(id_cliente):
            print("Cliente eliminado correctamente.")
        else:
            printerr("No se pudo eliminar el cliente. Es posible que el ID no exista.")
    except ErrorPersonalizado as ex:
        printerr(ex)
    enter_limpiar()