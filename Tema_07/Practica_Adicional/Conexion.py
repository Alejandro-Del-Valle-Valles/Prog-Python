#Manejador de la conexión y ejecución de querys en la BBDD
import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv

COLOR_ROJO: str = "\033[31m" #Código del color rojo para los str.
COLOR_RESET: str = "\033[0m"

def conectar():
    """Devuelve una conexión a la BBDD

    Returns:
        connection : Conexion a la BBDD o None si no se pudo conectar.
    """
    load_dotenv()
    conexion = None
    try:
        conexion = psycopg2.connect(
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD"),
            host = os.getenv("HOST"),
            port = os.getenv("PORT"),
            database = os.getenv("DATABASE")
        )
    except:
        print(f"{COLOR_ROJO}Ha ocurrido un error con la apertura de la conexión.{COLOR_RESET}")
    return conexion


def inicializar_tablas(conexion):
    """
    Crea las tablas en la BBDD si no existen
    """
    if conexion:
        CURSOR = conexion.cursor()
        try:
            CURSOR.execute("""
                CREATE TABLE IF NOT EXISTS Clientes (
                    id_cliente SERIAL PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    email VARCHAR(150) UNIQUE NOT NULL,
                    telefono VARCHAR(20)              
                )
            """)
            CURSOR.execute("""
                CREATE TABLE IF NOT EXISTS Productos (
                    id_producto SERIAL PRIMARY KEY,
                    nombre VARCHAR(150) NOT NULL,
                    precio DECIMAL(10,2) NOT NULL CHECK(precio >= 0),
                    stock INT NOT NULL CHECK(stock >= 0)
                )
            """)
            CURSOR.execute("""
                CREATE TABLE IF NOT EXISTS Pedidos (
                    id_pedido SERIAL PRIMARY KEY,
                    id_cliente INTEGER NOT NULL,
                    fecha DATE NOT NULL,
                    total DECIMAL(10,2) NOT NULL CHECK (total >= 0),
                    CONSTRAINT fk_cliente FOREIGN KEY(id_cliente) REFERENCES Clientes(id_cliente)
                                ON DELETE SET NULL
                )
            """)
            CURSOR.execute("""
                CREATE TABLE IF NOT EXISTS Detalle_Pedido (
                    id_detalle SERIAL PRIMARY KEY,
                    id_pedido INTEGER NOT NULL,
                    id_producto INTEGER NOT NULL,
                    cantidad INTEGER NOT NULL CHECK(cantidad > 0),
                    subtotal DECIMAL(10,2) NOT NULL CHECK(subtotal >= 0),
                    CONSTRAINT fk_pedido FOREIGN KEY(id_pedido) REFERENCES Pedidos(id_pedido)
                                ON DELETE CASCADE,
                    CONSTRAINT fk_producto FOREIGN KEY(id_producto) REFERENCES Productos(id_producto)
                                ON DELETE SET NULL
                )
            """)
            
            conexion.commit()
        except (Exception, Error) as ex:
            conexion.rollback()
            print(f"{COLOR_ROJO}Ha ocurrido un error durante la creación de las tablas: {ex}{COLOR_RESET}")