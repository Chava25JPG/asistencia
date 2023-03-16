from conexion import connect_to_db
import datetime

class Asistencia:
    def __init__(self):
        pass

    def obtener_datos_asistencia(self):
        id = input("introduce el id")
        alumno_id = input("Introduce el id del alumno: ")
        modulo_id = input("Introduce el id del módulo: ")
        asistio = input("Introduce si asistió (0 para no y 1 para sí): ")
        
        fecha = datetime.datetime.now().date()
        hora_de_entrada = datetime.datetime.now().time()
        conn = connect_to_db()
        cursor = conn.cursor()
        sql = "INSERT INTO asistencia (id, alumno_id, modulo_id, fecha, hora_de_entrada, asistio) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (id, alumno_id, modulo_id, fecha, hora_de_entrada, asistio)
        cursor.execute(sql, val)
        conn.commit()
        print("Asistencia agregada exitosamente")