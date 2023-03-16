from conexion import Conexion

class Grupo:
    def init(self):
        pass


    def obtener_datos_grupo(self):
        id = input("introduce el id: ")
        GradoYGrupo = input("Introduce el grado y grupo '0°X'")
        especialidad_id = input("Introduce el id de la especialidad: ")
        conn = Conexion.connect_to_db()
        cursor = conn.cursor()

        sql = "INSERT INTO grupos (id, GradoYGrupo, especialidad_id) VALUES(%s, %s, %s)"
        val= (id, GradoYGrupo,especialidad_id)
        cursor.execute(sql, val)
        conn.commit()
        print("grupo agregado exitosamente")
