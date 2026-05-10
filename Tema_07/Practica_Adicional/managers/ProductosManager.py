from models.Productos import Producto
from helpers.ErrorPersonalizado import ErrorPersonalizado
from repository.ProductosRepository import ProductosCRUD  # Corregido el import
from helpers.SolicitarDatos import SolicitarDatos
from helpers.Extensiones import printerr, pausa_y_limpia, enter_limpiar

__OPCIONES = ("Listar productos", "Crear producto", "Actualizar producto", "Eliminar producto")

def menu_productos():
    """
    Menú de gestión de datos de productos.
    """
    try:
        opcion: int = -1
        while opcion != 0:
            for i in range(len(__OPCIONES)):
                print(f"{i + 1}. {__OPCIONES[i]}")
            print("0. Salir")
            opcion = SolicitarDatos.pedir_numero_entero("Introduce una opción por favor: ", es_positivo=True)
            __manejar_menu(opcion)
    except Exception as ex:
        print(ex)
        printerr("Ha ocurrido un error inesperado mientras se administraban los productos. Volviendo al menu...")
        pausa_y_limpia(3)

def __manejar_menu(opcion: int):
    match opcion:
        case 0:
            print("Volviendo al menú...")
            pausa_y_limpia()
        case 1:
            __listar_productos()
        case 2:
            __crear_producto()
        case 3:
            __actualizar_producto()
        case 4:
            __eliminar_producto()
        case _:
            printerr("La opción elegida no es válida.")

def __listar_productos():
    """
    Muestra todos los productos
    """
    try:
        productos = ProductosCRUD.get_all()
        if not productos:
            print("No hay productos registrados.")
        else:
            for producto in productos:
                print(producto)
    except Exception as ex:
        printerr(f"Error al listar: {ex}")
    enter_limpiar()

def __crear_producto():
    """
    Crea un nuevo producto
    """
    try:
        nombre = SolicitarDatos.pedir_str("Introduce el nombre del producto (max 150): ", longitud_maxima=150)
        precio = SolicitarDatos.pedir_numero_decimal("Introduce el precio: ", es_positivo=True, permitir_nulo=False)
        stock = SolicitarDatos.pedir_numero_entero("Introduce el stock inicial: ", es_positivo=True, permitir_nulo=False)
        
        producto = Producto(nombre=nombre, precio=precio, stock=stock, id=0)
        
        if ProductosCRUD.create_producto(producto):
            print("Producto creado correctamente.")
        else:
            printerr("No se pudo crear el producto.")
    except (ErrorPersonalizado, ValueError) as ex:
        printerr(ex)
    enter_limpiar()

def __actualizar_producto():
    """
    Actualiza un producto. Los datos no introducidos se mantienen sin modificar.
    """
    try:
        id_producto = SolicitarDatos.pedir_numero_entero("Introduce el ID del producto a actualizar: ", es_positivo=True, permitir_nulo=False)
        producto_actual = ProductosCRUD.get_by_id(id_producto)
        
        if not producto_actual:
            raise ErrorPersonalizado("El producto indicado no existe.")
        
        print("Deja en blanco los campos que no desees modificar:")
        nombre = SolicitarDatos.pedir_str(f"Nombre actual ({producto_actual.nombre}): ", longitud_maxima=150, permitir_vacio=True)
        
        precio_str = SolicitarDatos.pedir_str(f"Precio actual ({producto_actual.precio}€): ", permitir_vacio=True)
        stock_str = SolicitarDatos.pedir_str(f"Stock actual ({producto_actual.stock}): ", permitir_vacio=True)

        nombre_final = nombre if nombre else producto_actual.nombre
        precio_final = float(precio_str) if precio_str else producto_actual.precio
        stock_final = int(stock_str) if stock_str else producto_actual.stock

        producto_modificado = Producto(nombre=nombre_final, precio=precio_final, stock=stock_final, id=id_producto)
        
        if ProductosCRUD.update_cliente(producto_modificado):
            print("Producto actualizado correctamente.")
        else:
            printerr("No se pudo actualizar el producto.")
    except (ErrorPersonalizado, ValueError) as ex:
        printerr(f"Error en los datos introducidos: {ex}")
    enter_limpiar()

def __eliminar_producto():
    """
    Elimina un producto
    """
    try:
        id_producto = SolicitarDatos.pedir_numero_entero("Introduce el ID del producto a eliminar: ", es_positivo=True, permitir_nulo=False)
        if ProductosCRUD.delete_producto(id_producto):
            print("Producto eliminado correctamente.")
        else:
            printerr("No se pudo eliminar el producto. Es posible que el ID no exista.")
    except ErrorPersonalizado as ex:
        printerr(ex)
    enter_limpiar()