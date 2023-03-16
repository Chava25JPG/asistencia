import mysql.connector
from conexion import connect_to_db
from prettytable import PrettyTable


conn = connect_to_db()

# Crear un cursor para ejecutar la consulta
cursor = conn.cursor()

# Ejecutar la consulta
query = "SELECT id, nombre, aula FROM clase"
cursor.execute(query)
# Crear una tabla
tabla = PrettyTable()
tabla.field_names = ["ID", "Nombre", "Aula"]

# Agregar los datos a la tabla
for (id, nombre, aula) in cursor:
    tabla.add_row([id, nombre, aula])

# Mostrar la tabla
print(tabla)

# Cerrar el cursor y la conexión
cursor.close()
conn.close()