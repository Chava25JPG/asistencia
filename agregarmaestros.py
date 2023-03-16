from conexion import Conexion
class Maestro:
        def __init__(self):
            pass

        def agregar_maestro(self):
            id = input("Introduce el id del maestro: ")
            nombre = input("Introduce el nombre: ")
            apellidoPaterno = input("Introduce el apellido paterno: ")
            apellidoMaterno = input("Introduce el apellido materno: ")
            RFIDcard = input("Introduce el número de la tarjeta RFID: ")

            conn = Conexion.connect_to_db()
            cursor = conn.cursor()
            sql = "INSERT INTO maestro (id, nombre, apellidoPaterno, apellidoMaterno, RFIDcard) VALUES (%s, %s, %s, %s, %s)"
            val = (id, nombre, apellidoPaterno, apellidoMaterno, RFIDcard)
            cursor.execute(sql, val)
            conn.commit()
            print("Maestro agregado exitosamente")

