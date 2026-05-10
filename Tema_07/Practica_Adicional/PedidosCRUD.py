from Pedidos import Pedido
from Conexion import conectar
from psycopg2 import Error
from ErrorPersonalizado import ErrorPersonalizado

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
            except Error as ex:
                conexion.rollback()
                raise ErrorPersonalizado(f"Error al obtener los pedidos de la base de datos: {ex}")
            except Exception as ex:
                raise ErrorPersonalizado(f"Error inesperado al obtener los pedidos: {ex}")
            finally:
                cursor.close()
                conexion.close()

        return pedidos
    
    @staticmethod
    def get_by_id(id: int) -> Pedido:
        pedido: Pedido = None
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "SELECT id_cliente, fecha, total, id_pedido FROM Pedidos WHERE id_pedido = %s"
                cursor.execute(query, (id))
                datos = cursor.fetchone()
                if datos:
                    pedido = Pedido(*datos)
            except Error as ex:
                conexion.rollback()
                raise ErrorPersonalizado(f"Error al obtener el pedido de la base de datos: {ex}")
            except Exception as ex:
                conexion.rollback()
                raise ErrorPersonalizado(f"Error inesperado al obtener el pedido: {ex}")
            finally:
                cursor.close()
                conexion.close()

        return pedido


    @staticmethod
    def create_pedido(pedido: Pedido) -> bool:
        creado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "INSERT INTO Pedidos (id_cliente, fecha, total) VALUES (%s, %s, %s)"
                cursor.execute(query, (pedido.id_cliente, pedido.fecha, pedido.total))
                conexion.commit()
                creado = cursor.rowcount > 0
            except Error as ex:
                conexion.rollback()
                #Este condicional ha sido creado con IA
                if ex.pgcode == '23503':
                    raise ErrorPersonalizado("El cliente asociado no existe en la base de datos.")
                elif ex.pgcode == '23514':
                    raise ErrorPersonalizado("El total del pedido no cumple con las restricciones (debe ser mayor o igual a 0).")
                else:
                    raise ErrorPersonalizado(f"Error en la base de datos al crear el pedido: {ex}")
            except Exception as ex:
                conexion.rollback()
                raise ErrorPersonalizado(f"Error inesperado al crear el pedido: {ex}")
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
                query = "UPDATE Pedidos SET fecha = %s, total = %s WHERE id_pedido = %s"
                cursor.execute(query, (pedido.fecha, pedido.total, pedido.id_pedido))
                conexion.commit()
                actualizado = cursor.rowcount > 0
            except Error as ex:
                conexion.rollback()
                #Este condicional ha sido creado con IA
                if ex.pgcode == '23514':
                    raise ErrorPersonalizado("El total del pedido no cumple con las restricciones (debe ser mayor o igual a 0).")
                else:
                    raise ErrorPersonalizado(f"Error en la base de datos al actualizar el pedido: {ex}")
            except Exception as ex:
                conexion.rollback()
                raise ErrorPersonalizado(f"Error inesperado al actualizar el pedido: {ex}")
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
                cursor.execute(query, (id,))
                conexion.commit()
                eliminado = cursor.rowcount > 0
            except Error as ex:
                conexion.rollback()
                raise ErrorPersonalizado(f"Error de base de datos al eliminar el pedido: {ex}")
            except Exception as ex:
                conexion.rollback()
                raise ErrorPersonalizado(f"Error inesperado al eliminar el pedido: {ex}")
            finally:
                cursor.close()
                conexion.close()

        return eliminado