from prettytable import PrettyTable
from src.conexion import connect_to_db

class BusquedaRFID:
    def __init__(self):
        pass
    
    def buscar(self):
        rfid = input("Introduce el RFIDcard: ")
        conn = connect_to_db()
        cursor = conn.cursor()
        
        # Buscar en tabla maestro
        sql_maestro = "SELECT * FROM maestro WHERE RFIDcard = %s"
        cursor.execute(sql_maestro, (rfid,))
        maestro = cursor.fetchone()
        if maestro:
            # Mostrar si es maestro y su información
            print("Maestro")
            t = PrettyTable(['Nombre', 'Apellido Paterno', 'Apellido Materno'])
            t.add_row([maestro[1], maestro[2], maestro[3]])
            print(t)
        
        # Buscar en tabla alumno
        sql_alumno = "SELECT a.nombre, a.apellidoPaterno, a.apellidoMaterno, g.GradoYGrupo, e.nombre FROM alumno a JOIN grupos g ON a.grupo_id = g.id JOIN especialidad e ON g.especialidad_id = e.id WHERE a.RFIDcard = %s"
        cursor.execute(sql_alumno, (rfid,))
        alumno = cursor.fetchone()
        if alumno:
            # Mostrar si es alumno y su información
            print("Alumno")
            t = PrettyTable(['Nombre', 'Apellido Paterno', 'Apellido Materno', 'Grado y Grupo', 'Especialidad'])
            t.add_row([alumno[0], alumno[1], alumno[2], alumno[3], alumno[4]])
            print(t)
            
        # Si no se encuentra en ninguna tabla, mostrar mensaje de error
        if not maestro and not alumno:
            print("No se encontró el RFIDcard en la base de datos")

busqueda = BusquedaRFID()
busqueda.buscar()


