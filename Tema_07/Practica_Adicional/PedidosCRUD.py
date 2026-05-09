from Pedidos import Pedido
from Conexion import conectar

class PedidosCRUD:

    @staticmethod
    def get_all() -> list:
        pedidos: list = []
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "SELECT id_cliente, fecha, total, id_pedido FROM Pedidos"
                cursor.execute(query)
                datos = cursor.fetchall()
                pedidos = [Pedido(*fila) for fila in datos]
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return pedidos


    @staticmethod
    def create_pedido(pedido: Pedido) -> bool:
        creado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "INSERT INTO Pedidos (id_cliente, fecha, total) VALUES (%s, %s, %s)"
                cursor.execute(query, (pedido.id_cliente, pedido.fecha, pedido.total))
                creado = cursor.rowcount > 0
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return creado


    @staticmethod
    def update_pedido(pedido: Pedido) -> bool:
        actualizado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "UPATE Productos SET fecha = %s, total = %s WHERE id_pedido = %s"
                cursor.execute(query, (pedido.fecha, pedido.total, pedido.id_pedido))
                actualizado = cursor.rowcount > 0
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return actualizado

    @staticmethod
    def delete_pedido(id: int) -> bool:
        eliminado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "DELETE FROM Pedidos WHERE id_pedido = %s"
                cursor.execute(query, (id))
                eliminado = cursor.rowcount > 0
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return eliminado