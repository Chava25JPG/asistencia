from datetime import datetime

# Creamos un diccionario para mapear los números a los nombres de los días
days = {
0: 'Lunes',
1: 'Martes',
2: 'Miércoles',
3: 'Jueves',
4: 'Viernes',
5: 'Sábado',
6: 'Domingo'
}

# Obtenemos el día de la semana
weekday = datetime.today().weekday()

# Imprimimos el día de la semana
print("Hoy es:", days[weekday])