import serial.tools.list_ports
import tkinter as tk
import serial

# Función para detectar los puertos en los que están conectados los Arduinos
def detect_ports():
    ports = serial.tools.list_ports.comports()
    arduino_ports = []
    for port in ports:
        print(port.description) # Agregado para imprimir la descripción de cada puerto
        if "Arduino" in port.description or "CH341" in port.description:
            arduino_ports.append(port.device)
    return arduino_ports


# Función para seleccionar el puerto deseado
def select_port(port):
    response = send_serial_message(port, "Hello Arduino!")
    print(f"El Arduino está conectado en el puerto {port} y respondió: {response}")

# Función para enviar un mensaje al Arduino a través del puerto serial
def send_serial_message(port, message):
    ser = serial.Serial(port, 9600, timeout=1)
    ser.write(message.encode())
    response = ser.readline().decode().strip()
    ser.close()
    return response

# Crear la ventana principal
root = tk.Tk()
root.title("Detectar Puerto Arduino")

# Crear el menú desplegable para seleccionar el puerto
ports_menu = tk.StringVar(root)
ports_menu.set("Seleccione un puerto")
ports = detect_ports()
if ports:
    ports_menu_options = ports
else:
    ports_menu_options = ["No se detectó ningún Arduino"]
ports_menu_dropdown = tk.OptionMenu(root, ports_menu, *ports_menu_options, command=select_port)
ports_menu_dropdown.pack()

# Ejecutar la aplicación
root.mainloop()
