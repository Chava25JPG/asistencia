#esto lo voy a ocupar mas adelante en vistasPru

import tkinter as tk

def opcion1():
    print("Seleccionaste la opción 1")

def opcion2():
    print("Seleccionaste la opción 2")

def opcion3():
    print("Seleccionaste la opción 3")

# Crear la ventana principal
root = tk.Tk()

# Crear el menú desplegable
opcion_menu = tk.StringVar(root)
opcion_menu.set("Selecciona una opción") # Valor por defecto

menu = tk.OptionMenu(root, opcion_menu, "Opción 1", "Opción 2", "Opción 3")
menu.pack()

# Definir la función a llamar cuando se seleccione una opción en el menú
def seleccionar_opcion(*args):
    opcion = opcion_menu.get()
    if opcion == "Opción 1":
        opcion1()
    elif opcion == "Opción 2":
        opcion2()
    elif opcion == "Opción 3":
        opcion3()

opcion_menu.trace("w", seleccionar_opcion) # "w" indica que se llamará la función cuando cambie el valor de la variable

# Mostrar la ventana
root.mainloop()













































































#Ejemplo bd tkinter
root = tk.Tk()
root.title("Agregar datos a la base de datos")

# Crear etiquetas y campos de entrada para nombre y edad
tk.Label(root, text="Nombre").grid(row=0, column=0)
nombre_entry = tk.Entry(root)
nombre_entry.grid(row=0, column=1)

tk.Label(root, text="Edad").grid(row=1, column=0)
edad_entry = tk.Entry(root)
edad_entry.grid(row=1, column=1)

# Crear botón para agregar datos
def agregar_datos():
    nombre = nombre_entry.get()
    edad = edad_entry.get()
    c.execute("INSERT INTO datos (nombre, edad) VALUES (?, ?)", (nombre, edad))
    conn.commit()
    nombre_entry.delete(0, tk.END)
    edad_entry.delete(0, tk.END)

agregar_datos_button = tk.Button(root, text="Agregar datos", command=agregar_datos)
agregar_datos_button.grid(row=2, column=1)

root.mainloop()
