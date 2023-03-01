import serial

# Configurar el puerto serial
ser = serial.Serial('/dev/ttyUSB2', 9600) # Cambia '/dev/ttyUSB2' por el puerto serial de tu Arduino

def obtener_uid():
    while True:
        # Leer los datos del puerto serial
        if ser.in_waiting > 0:
            uid = ser.readline().rstrip().decode('utf-8')
            return uid

