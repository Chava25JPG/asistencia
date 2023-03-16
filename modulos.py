from conexion import Conexion

class Modulo:
    def init(self):
        pass

    def obtener_datos_modulo(self):
        id = input("Introduce el id del módulo: ")
        nombre = input("Introduce el nombre: ")
        hora_inicio = input("Introduce la hora de inicio (formato HH:MM): ")
        hora_fin = input("Introduce la hora de fin (formato HH:MM): ")

        conn = Conexion.connect_to_db()
        cursor = conn.cursor()
        sql = "INSERT INTO modulos (id, nombre, horario_id) VALUES (%s, %s, %s, %s)"
        val = (id, nombre, hora_inicio, hora_fin)
        cursor.execute(sql, val)
        conn.commit()
        print("Módulo agregado exitosamente")