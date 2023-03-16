import tkinter as tk

def mostrar_mensaje():
    mensaje = "Acerque el tag"
    label.config(text=mensaje)

root = tk.Tk()

boton = tk.Button(root, text="Mostrar mensaje", command=mostrar_mensaje)
boton.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
