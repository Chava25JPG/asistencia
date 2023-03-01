import datetime
from src.conexion import connect_to_db

cnx = connect_to_db()

cursor = cnx.cursor()

# Obtener el día actual
hoy = datetime.datetime.today().strftime('%A')

# Consulta SQL para contar el número de clases por materia en el día actual
consulta = ("""
    SELECT m.nombre, COUNT(*) AS num_clases
    FROM horario h
    INNER JOIN materia m ON h.materia_id = m.id
    WHERE h.dia = %s
    GROUP BY m.nombre
""")

# Ejecutar la consulta
cursor.execute(consulta, (hoy,))

# Mostrar los resultados
for (nombre, num_clases) in cursor:
    print(f'{nombre}: {num_clases} clases hoy')

# Cerrar la conexión a la base de datos
cursor.close()
cnx.close()