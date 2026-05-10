from models.Clientes import Cliente
from helpers.Conexion import conectar

class ClientesCrud:
#Clase encargada de realizar operaciones CRUD sobre clientes.
    
    @staticmethod
    def get_all() -> list:
        clientes: list = []
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "SELECT nombre, email, telefono, id_cliente FROM Clientes"
                cursor.execute(query)
                datos = cursor.fetchall()
                clientes = [Cliente(*fila) for fila in datos]
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return clientes
    
    @staticmethod
    def get_by_id(id: int) -> Cliente:
        cliente: Cliente = None
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "SELECT nombre, email, telefono, id_cliente FROM Clientes WHERE id_cliente = %s"
                cursor.execute(query, (id,))
                datos = cursor.fetchone()
                if datos:
                    cliente = Cliente(*datos)
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return cliente


    @staticmethod
    def create_cliente(cliente: Cliente) -> bool:
        creado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "INSERT INTO Clientes (nombre, email, telefono) VALUES (%s, %s, %s)"
                cursor.execute(query, (cliente.nombre, cliente.email, cliente.telefono))
                conexion.commit()
                creado = cursor.rowcount > 0
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return creado


    @staticmethod
    def update_cliente(cliente: Cliente) -> bool:
        actualizado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "UPDATE Clientes SET nombre = %s, email = %s, telefono = %s WHERE id_cliente = %s"
                cursor.execute(query, (cliente.nombre, cliente.email, cliente.telefono, cliente.id))
                conexion.commit()
                actualizado = cursor.rowcount > 0
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return actualizado

    @staticmethod
    def delete_cliente(id: int) -> bool:
        eliminado = False
        conexion = conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                query = "DELETE FROM Clientes WHERE id_cliente = %s"
                cursor.execute(query, (id,))
                conexion.commit()
                eliminado = cursor.rowcount > 0
            except:
                conexion.rollback()
            finally:
                cursor.close()
                conexion.close()

        return eliminado