import mysql.connector

class Conexion:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Zaragoza2525",
            database="asistencia_escuela"
        )
        
    def connect_to_db(self):
        if self.conn.is_connected():
            print("Conexión exitosa")
            return self.conn
        else:
            print("No se pudo conectar correctamente")
