from conexion import Conexion
from PruebaRC import obtener_uid

class Alumno:
        def init(self):
            pass

        def obtener_datos_alumno(self):
            #id = input("Introduce el id del alumno: ")
            nombre = input("Introduce el nombre: ")
            apellidoPaterno = input("Introduce el apellido paterno: ")
            apellidoMaterno = input("Introduce el apellido materno: ")
            grupo_id = input("Introduce el id de la grupo: ")
            print("Acerque el TAG")
            RFIDcard = obtener_uid()
            return (nombre, apellidoPaterno, apellidoMaterno, grupo_id, RFIDcard)

        def add_alumno(self):
            datos_alumno = self.obtener_datos_alumno()
            conexion = Conexion()
            conn = conexion.connect_to_db()
            cursor = conn.cursor()
            sql = "INSERT INTO alumno (nombre, apellidoPaterno, apellidoMaterno, grupo_id, RFIDcard) VALUES (%s, %s, %s, %s, %s)"
            val = datos_alumno
            cursor.execute(sql, val)
            conn.commit()
            print("Alumno agregado exitosamente")


    