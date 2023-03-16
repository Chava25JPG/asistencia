from curses import nocbreak
from conexion import Conexion

class Materia:
    def init(self):
        pass

    def obtener_datos_materia(self):
        id = input("Introduce el id de la materia: ")
        nombre = input("Introduce el nombre de la materia: ")
        
        conn = Conexion.connect_to_db()
        cursor = conn.cursor()
        sql = "INSERT INTO materia (id, nombre) VALUES (%s, %s)"
        val = (id, nombre)
        cursor.execute(sql, val)
        conn.commit()
        print("Materia agregada exitosamente")