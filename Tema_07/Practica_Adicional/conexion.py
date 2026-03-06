#Manejador de la conexión y ejecución de querys en la BBDD
import sqlite3

COLOR_ROJO: str = "\033[31m" #Código del color rojo para los str.
COLOR_RESET: str = "\033[0m"
CONEXION = sqlite3.connect("tienda.db")
CURSOR = CONEXION.cursor()

def inicializar_tablas():
    """
    Crea las tablas en la BBDD si no existen
    """
    try:
        CURSOR.execute("PRAGMA foreign_keys = ON;")

        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS Clientes (
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) NOT NULL,
                email VARCHAR(150) UNIQUE NOT NULL,
                telefono VARCHAR(20)              
            )
        """)
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS Productos (
                id_producto INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(150) NOT NULL,
                precio DECIMAL(10,2) NOT NULL CHECK(precio >= 0),
                stock INT NOT NULL CHECK(stock >= 0)
            )
        """)
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS Pedidos (
                id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INTEGER NOT NULL,
                fecha DATE NOT NULL,
                total DECIMAL(10,2) NOT NULL CHECK (total >= 0),
                FOREIGN KEY(id_cliente) REFERENCES Clientes(id_cliente)
                            ON DELETE SET NULL
            )
        """)
        CURSOR.execute("""
            CREATE TABLE IF NOT EXISTS Detalle_Pedido (
                id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
                id_pedido INTEGER NOT NULL,
                id_producto INTEGER NOT NULL,
                cantidad INTEGER NOT NULL CHECK(cantidad > 0),
                subtotal DECIMAL(10,2) NOT NULL CHECK(subtotal >= 0),
                FOREIGN KEY(id_pedido) REFERENCES Pedidos(id_pedido)
                            ON DELETE CASCADE,
                FOREIGN KEY(id_producto) REFERENCES Productos(id_prodcuto)
                            ON DELETE SET NULL
            )
        """)
        
        CONEXION.commit()
    except:
        print(f"{COLOR_ROJO}Ha ocurrido un error durante la creación de las tablas.{COLOR_RESET}")