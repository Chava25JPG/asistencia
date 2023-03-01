from conexion import connect_to_db 

class Horario:
    def __init__(self):
        self.dias_semana = {
            "1": "Lunes",
            "2": "Martes",
            "3": "Miércoles",
            "4": "Jueves",
            "5": "Viernes"
        }

    def obtener_datos_horario(self):
        id = input("Introduce el id del horario: ")
        id_grupo = input("Introduce el id del grupo: ")
        while True:
            dia = input("Introduce el número del día de la semana (1= Lunes)(2=Martes)(3= Miercoles)(4= Jueves)(5= Viernes): ")
            if dia in self.dias_semana:
                break
            else:
                print("Día inválido. Por favor ingresa un número del 1 al 7.")
        dia_nombre = self.dias_semana[dia]
        materia_id = input("Introduce el id de la materia: ")
        maestro_id = input("Introduce el id de el maestro: ")
        modulo_id = input("introduce el numero de modulo: ")
        conn = connect_to_db()
        cursor = conn.cursor()

        sql = "INSERT INTO horario (id, grupo_id , dia, materia_id, maestro_id, modulo_id) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (id, id_grupo, dia_nombre, materia_id, maestro_id, modulo_id)
        cursor.execute(sql, val)
        conn.commit()
        print("Horario agregado exitosamente")
