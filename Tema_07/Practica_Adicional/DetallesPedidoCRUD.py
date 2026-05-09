from DetallesPedido import DetallePedido
from Conexion import conectar

class DetallesPedidoCRUD:

    @staticmethod
    def get_all() -> list:
        detalles: list = []
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "SELECT id_pedido, id_producto, cantidad, subtotal, id_detalle FROM Detalle_Pedido"
                cursor.execute(query)
                datos = cursor.fetchall()
                detalles = [DetallePedido(*fila) for fila in datos]
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return detalles


    @staticmethod
    def create_detalle(detalle: DetallePedido) -> bool:
        creado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "INSERT INTO Deatlle_Pedido (id_pedido, id_producto, cantidad, subtotal) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (detalle.id_pedido, detalle.id_producto, detalle.cantidad, detalle.subtotal))
                creado = cursor.rowcount > 0
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return creado


    @staticmethod
    def update_detalle(pedido: DetallePedido) -> bool:
        actualizado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "UPATE Detalle_Pedido SET cantidad = %s, subtotal = %s WHERE id_detalle = %s"
                cursor.execute(query, (pedido.cantidad, pedido.subtotal, pedido.id_detalle))
                actualizado = cursor.rowcount > 0
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return actualizado

    @staticmethod
    def delete_detalle(id: int) -> bool:
        eliminado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "DELETE FROM Detalle_Pedido WHERE id_detalle = %s"
                cursor.execute(query, (id))
                eliminado = cursor.rowcount > 0
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return eliminado