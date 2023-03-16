from conexion import Conexion

class Especialidad:
    def init(self):
        pass

    def obtener_datos_especialidad(self):
        id = input("Introduce el id de la especialidad: ")
        nombre = input("Introduce el nombre de la especialidad: ")
        
        conn = Conexion.connect_to_db()
        cursor = conn.cursor()
        sql = "INSERT INTO especialidad (id, nombre) VALUES (%s, %s)"
        val = (id, nombre)
        cursor.execute(sql, val)
        conn.commit()
        print("Especialidad agregada exitosamente")