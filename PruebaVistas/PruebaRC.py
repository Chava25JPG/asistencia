import serial

# Configurar el puerto serial
ser = serial.Serial('/dev/ttyUSB3', 9600) # Cambia '/dev/ttyUSB2' por el puerto serial de tu Arduino
class RC():

    def obtener_uid(self):
        while True:
            # Leer los datos del puerto serial
            if ser.in_waiting > 0:
                uid = ser.readline().rstrip().decode('utf-8')
                print("su uid es:  ", uid)
                return uid


def main():
    rc = RC()
    uid = rc.obtener_uid()
    print(uid)

if __name__ == '__main__':
    main()