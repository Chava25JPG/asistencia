from conexion import Conexion
from PruebaRC import obtener_uid
conexion = Conexion()
conn = conexion.connect_to_db()

def asignarRC():
    # Pedir al usuario que ingrese el ID del alumno
    alumno_id = input("Ingrese el ID del alumno: ")

    # Verificar si el alumno existe en la base de datos
    cursor = conn.cursor()
    query = "SELECT * FROM alumno WHERE id = %s"
    cursor.execute(query, (alumno_id,))
    result = cursor.fetchone()

    if result is not None:
        # Si el alumno existe, pedir al usuario que ingrese la nueva tarjeta RFID
        print("acerque la nueva tarjeta")
        uid = obtener_uid()
        nueva_rfid = uid

        # Actualizar la tarjeta RFID del alumno
        query = "UPDATE alumno SET RFIDcard = %s WHERE id = %s"
        cursor.execute(query, (nueva_rfid, alumno_id))
        conn.commit()

        print("Se ha asignado/reasignado la tarjeta RFID al alumno correctamente.")
    else:
        # Si el alumno no existe, informar al usuario
        print("El ID de alumno ingresado no existe en la base de datos.")

