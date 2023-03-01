import mysql.connector

def connect_to_db():
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Zaragoza2525",
            database="asistencia_escuela"
        )
        if conn.is_connected():
            print("Conexión exitosa")
            return conn
        else:
            print("No se pudo conectar correctamente")

