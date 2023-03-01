from datetime import datetime
from src.conexion import connect_to_db

conn = connect_to_db()

# Solicitar RFID por consola
rfid = input("Introduzca el RFID del alumno: ")

# Crear un cursor para ejecutar la consulta
cursor = conn.cursor()

# Ejecutar la consulta para buscar el alumno por su RFID
query = "SELECT * FROM alumno WHERE RFIDcard = %s"
cursor.execute(query, (rfid,))

# Obtener el resultado de la consulta
alumno = cursor.fetchone()

# Si no se encontró el alumno, imprimir mensaje y salir del programa
if alumno is None:
    print("Alumno no encontrado")
    cursor.close()
    conn.close()
    exit()

# Obtener los datos del alumno
id_alumno = alumno[0]
nombre = alumno[1]
apellido_paterno = alumno[2]
apellido_materno = alumno[3]
grupo_id = alumno[4]

# Obtener la fecha y hora actual
fecha = datetime.now().date()
hora = datetime.now().time().strftime('%H:%M:%S')

# Ejecutar la consulta para registrar la asistencia
query = "INSERT INTO asistencia (alumno_id, materia_id, maestro_id, hora_de_entrada, fecha, asistio) VALUES (%s, %s, %s, %s, %s, %s)"
cursor.execute(query, (id_alumno, 1, 1, hora, fecha, True))

# Confirmar los cambios
conn.commit()

# Imprimir mensaje de asistencia registrada exitosamente
print("Asistencia registrada exitosamente para el alumno:")
print("Nombre:", nombre)
print("Apellido paterno:", apellido_paterno)
print("Apellido materno:", apellido_materno)
print("grupo id:", grupo_id)

# Cerrar el cursor y la conexión
cursor.close()
conn.close()
