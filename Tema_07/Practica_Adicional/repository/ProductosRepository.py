from models.Productos import Producto
from helpers.Conexion import conectar

class ProductosCRUD:

    @staticmethod
    def get_all() -> list:
        productos: list = []
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "SELECT nombre, precio, stock, id_producto FROM Productos"
                cursor.execute(query)
                datos = cursor.fetchall()
                productos = [Producto(*fila) for fila in datos]
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return productos
    
    @staticmethod
    def get_by_id(id: int) -> Producto:
        producto: Producto = None
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "SELECT nombre, precio, soctk, id_producto FROM Productos WHERE id_producto = %s"
                cursor.execute(query, (id,))
                datos = cursor.fetchone()
                if datos:
                    producto = Producto(*datos)
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return producto


    @staticmethod
    def create_producto(producto: Producto) -> bool:
        creado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "INSERT INTO Productos (nombre, precio, stock) VALUES (%s, %s, %s)"
                cursor.execute(query, (producto.nombre, producto.precio, producto.stock))
                conexion.commit()
                creado = cursor.rowcount > 0
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return creado


    @staticmethod
    def update_cliente(producto: Producto) -> bool:
        actualizado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "UPATE Productos SET nombre = %s, precio = %s, stock = %s WHERE id_producto = %s"
                cursor.execute(query, (producto.nombre, producto.precio, producto.stock, producto.id))
                conexion.commit()
                actualizado = cursor.rowcount > 0
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return actualizado

    @staticmethod
    def delete_producto(id: int) -> bool:
        eliminado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "DELETE FROM Productos WHERE id_producto = %s"
                cursor.execute(query, (id,))
                conexion.commit()
                eliminado = cursor.rowcount > 0
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return eliminado
