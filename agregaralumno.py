from conexion import connect_to_db

class Alumno:
        def init(self):
            pass

        def obtener_datos_alumno(self):
            id = input("Introduce el id del alumno: ")
            nombre = input("Introduce el nombre: ")
            apellidoPaterno = input("Introduce el apellido paterno: ")
            apellidoMaterno = input("Introduce el apellido materno: ")
            grupo_id = input("Introduce el id de la grupo: ")
            RFIDcard = input("Introduce el número de la tarjeta RFID: ")
            return (id, nombre, apellidoPaterno, apellidoMaterno, grupo_id, RFIDcard)

        def add_alumno(self):
            datos_alumno = self.obtener_datos_alumno()
            conn = connect_to_db()
            cursor = conn.cursor()
            sql = "INSERT INTO alumno (id, nombre, apellidoPaterno, apellidoMaterno, grupo_id, RFIDcard) VALUES (%s, %s, %s, %s, %s, %s)"
            val = datos_alumno
            cursor.execute(sql, val)
            conn.commit()
            print("Alumno agregado exitosamente")


    