import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from conexion1 import connect_to_db
import threading 

import serial
ser = serial.Serial('/dev/ttyUSB3', 9600) # Cambia '/dev/ttyUSB2' por el puerto serial de tu Arduino
especialidad_id = None
uidTC = None  # variable global para almacenar el valor de retorno
grupo_id = None
grupo_idhorario = None
materia_idhorario = None
modulo_idhorario = None
maestro_idhorario = None


#app = ctk.CTk()
#app = tkinter.Tk()
#app.geometry("1200x500")
estiloBotonBlue = {"corner_radius": 5, "border_width": 0, "text_color": "#FFFAF0","hover_color" : "#696969", "fg_color": "#6495ED", "font": ("Comfortaa", 15, "bold")}

estiloBoton = {"corner_radius": 5, "border_width": 0, "text_color": "#000000","hover_color" : "#696969", "fg_color": "#FAF0E6", "font": ("Comfortaa", 15, "bold")}

etiquetaStyle = {"text_color" : "#FAF0E6", "font": ("Comfortaa", 15, "bold"), "anchor": "w"}

entryStyle = {"corner_radius": 5, "border_width" : 2, "font": ("Comfortaa", 10, "bold")}


class RC():
    def obtener_uid(self):
        global uidTC
        while True:
            if ser.in_waiting > 0:
                uidTC = ser.readline().rstrip().decode('utf-8')
                print(uidTC)
                return uidTC

class Frame1(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        botonAA = ctk.CTkButton(self, text= "Agregar un nuevo Alumno", 
                                **estiloBoton, command= self.agregarAlumnoFun )
        
        botonAM = ctk.CTkButton(self, text= "Agregar un nuevo Maestro", 
                                **estiloBoton, command= self.agregarMaetoFun )
        
        botonVA = ctk.CTkButton(self, text= "Ver Asistencias",
                                 **estiloBoton, command= self.verAsistencia)
        
        botonAG = ctk.CTkButton(self, text= "Agregar un nuevo Grupo", 
                                **estiloBoton, command= self.agregarGrupo )
        
        botonAE = ctk.CTkButton(self, text= "Agregar una nueva Especialidad", 
                                **estiloBoton, command= self.agregarEspecialidad )
        
        botonAMa = ctk.CTkButton(self, text= "Agregar una nueva Materia",
                                **estiloBoton, command= self.agregarMateriaFun )
        
        botonAH = ctk.CTkButton(self, text= "Agregar un nuevo horario para Grupo",
                                **estiloBoton, command= self.agregarHorarioFun )
        
        botonAMo = ctk.CTkButton(self, text= "Agregar un nuevo Modulo", 
                                **estiloBoton, command= self.agregarModuloFun )
        
        BotonARFIDNAa= ctk.CTkButton(self, text= "Asignar un nuevo TAG a Alumno", 
                                **estiloBoton, command= self.asignarTagAfun )
        
        BotonARFIDNAm= ctk.CTkButton(self, text= "Asignar un nuevo TAG a Maestro",
                                **estiloBoton, command= self.asignarTagMfun )

        botonAA.place(relx=0.02, rely=0.05, relwidth=0.25, relheight=0.1)
        botonAM.place(relx=0.02, rely=0.175, relwidth=0.25, relheight=0.1)
        botonVA.place(relx=0.02, rely=0.30, relwidth=0.25, relheight=0.1)
        botonAG.place(relx=0.02, rely=0.425, relwidth=0.25, relheight=0.1)
        botonAE.place(relx=0.02, rely=0.55, relwidth=0.25, relheight=0.1)
        botonAMa.place(relx=0.02, rely=0.675, relwidth=0.25, relheight=0.1)
        botonAH.place(relx=0.02, rely=0.80, relwidth=0.25, relheight=0.1)
        botonAMo.place(relx=0.375, rely=0.05, relwidth=0.25, relheight=0.1)
        BotonARFIDNAa.place(relx=0.375, rely=0.175, relwidth=0.25, relheight=0.1)
        BotonARFIDNAm.place(relx=0.375, rely=0.30, relwidth=0.25, relheight=0.1)

        self.toplevel_window = None


        #funciones para abrir las ventanas emergentes:

    def agregarAlumnoFun (self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AgregarAlumno(self)
        else:
            self.toplevel_window.focus()
    
    def agregarMaetoFun (self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = Agregarmaeto(self)
        else:
            self.toplevel_window.focus()
            
    def verAsistencia (self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = VerAsistencia(self)
        else:
            self.toplevel_window.focus()
            
    def agregarGrupo (self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AgregarGrupo(self)
        else:
            self.toplevel_window.focus()
            
    def agregarEspecialidad (self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AgregarEspecialidad(self)
        else:
            self.toplevel_window.focus()
            
    
    
    def agregarMateriaFun (self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AgregarMateria(self)
        else:
            self.toplevel_window.focus()
    
    def agregarModuloFun (self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AgregarModulo(self)
        else:
            self.toplevel_window.focus()
            
    def agregarHorarioFun (self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AgregarHorario(self)
        else:
            self.toplevel_window.focus()
            
    def asignarTagAfun (self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AsignarTagAlum(self)
        else:
            self.toplevel_window.focus()
            
    def asignarTagMfun (self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AsignarTagMaestro(self)
        else:
            self.toplevel_window.focus()
            



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x800")
        self.title("CHV Control de Asistencia")
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = Frame1(master=self)
        self.my_frame.grid(row=0, column=0, padx=30, pady=30, sticky="nsew")

class AgregarAlumno(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x500")
        self.title("Agregar Alumno")


        butARFID = ctk.CTkButton(self, text="Asignar RFID", **estiloBoton, command=self.start_obtener_uid_thread)
        butARFID.place(relx=0.05, rely=0.45, relwidth=0.25, relheight=0.075)

        etiquetaNA = ctk.CTkLabel(self, text = "Nombre/s del alumno:", **etiquetaStyle)
        etiquetaNA.place(relx=0.05, rely=0.05, relwidth=0.25, relheight = 0.075)

        self.enNom = ctk.CTkEntry(self, placeholder_text="Escriba el Nombre", **entryStyle)
        self.enNom.place(relx=0.375, rely=0.05, relwidth=0.25, relheight = 0.075)

        etiquetaAP= ctk.CTkLabel(self, text= "Apellido Paterno:", **etiquetaStyle)
        etiquetaAP.place(relx=0.05, rely=0.15, relwidth=0.25, relheight = 0.075)

        self.enAP = ctk.CTkEntry(self, placeholder_text="Escriba el Apellido", **entryStyle)
        self.enAP.place(relx=0.375, rely=0.15, relwidth=0.25, relheight = 0.075)

        etiquetaAM= ctk.CTkLabel(self, text= "Apellido Materno:", **etiquetaStyle)
        etiquetaAM.place(relx=0.05, rely=0.25, relwidth=0.25, relheight = 0.075)

        self.enAM = ctk.CTkEntry(self, placeholder_text="Escriba el Apellido", **entryStyle)
        self.enAM.place(relx=0.375, rely=0.25, relwidth=0.25, relheight = 0.075)

        self.grupo_seleccionado = tk.StringVar(self)
        self.grupo_seleccionado.set("Seleccione un grupo")


        conn = connect_to_db()
        cursor = conn.cursor()
        
        cursor.execute("SELECT GradoYGrupo FROM grupos")
        grupos_disponibles = [row[0] for row in cursor.fetchall()]

        conn.close()

        def obtener_grupo_id(opcion_seleccionada):
            global grupo_id
            conn = connect_to_db()
            cursor = conn.cursor()
            
            cursor.execute("SELECT id FROM grupos WHERE GradoYGrupo = %s", (opcion_seleccionada,))
            grupo_id = cursor.fetchone()[0]
            print("grupo_id seleccionado:", grupo_id)
            conn.close()
            return grupo_id

# Creamos el OptionMenu y lo configuramos
        menu = tk.OptionMenu(self, self.grupo_seleccionado, *grupos_disponibles, command=obtener_grupo_id)
        menu.place(relx=0.05, rely=0.35, relwidth=0.25, relheight=0.075)


 #       butARFID = ctk.CTkButton(self, text= "asignar RFID", **estiloBoton, command = rfidA)
  #      butARFID.place(relx=0.05, rely=0.45, relwidth=0.25, relheight = 0.075)

        butGuargarAA = ctk.CTkButton(self, text= "Guardar", **estiloBotonBlue, command= self.guardar )
        butGuargarAA.place(relx=0.875, rely=0.9, relwidth=0.1, relheight = 0.075)

        self.mensaje1_text = ""
        self.mensaje1 = ctk.CTkLabel(self, text="")
        self.mensaje1.place(relx=0.325, rely=0.45, relwidth=0.25, relheight=0.075)

        
        

    def start_obtener_uid_thread(self):
        self.mensaje1.configure(text="Acerque el Tag")
        self.thread_obtener_uid = threading.Thread(target=RC().obtener_uid)
        self.thread_obtener_uid.start()
        self.after(100, self.check_thread)

   # def obtener_uid_thread(self):
    #    rc = RC()
     #   self.uid = rc.obtener_uid()
      #  print(self.uid)


    def check_thread(self):
        if self.thread_obtener_uid and not self.thread_obtener_uid.is_alive():
            self.mensaje1.configure(text=self.mensaje1_text)
            self.after(3000, lambda: self.mensaje1.configure(text=""))
        else:
            self.after(100, self.check_thread)


#Funcion del Boton Guardar
    def guardar(self):
        conn = connect_to_db()
        cursor = conn.cursor()

        global uidTC
        global grupo_id
        nombreAlum = self.enNom.get()
        apePAlum = self.enAP.get()
        apeMAlum = self.enAM.get()

        # Verificamos que se hayan ingresado todos los campos
        if nombreAlum != "" and apePAlum != "" and apeMAlum != "" and uidTC != "" and grupo_id != "":
            sql = "INSERT INTO alumno (nombre, apellidoPaterno, apellidoMaterno, grupo_id, RFIDcard) VALUES (%s, %s, %s, %s, %s)"
            val = (nombreAlum, apePAlum, apeMAlum, grupo_id, uidTC)
            cursor.execute(sql, val)
            conn.commit()
            print("Alumno agregado exitosamente")

            # Borramos el texto de los campos del formulario
            self.enNom.delete(0, tk.END)
            self.enAP.delete(0, tk.END)
            self.enAM.delete(0, tk.END)

        else:
            print("Por favor complete todos los campos")

        conn.close()
    
class Agregarmaeto(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x500")
        self.title("Agregar Maestro")



        butARFID = ctk.CTkButton(self, text="Asignar RFID", **estiloBoton, command=self.start_obtener_uid_thread)
        butARFID.place(relx=0.05, rely=0.35, relwidth=0.25, relheight=0.075)

        etiquetaNM = ctk.CTkLabel(self, text = "Nombre/s del Maestro:", **etiquetaStyle)
        etiquetaNM.place(relx=0.05, rely=0.05, relwidth=0.25, relheight = 0.075)

        self.enNom = ctk.CTkEntry(self, placeholder_text="Escriba el Nombre", **entryStyle)
        self.enNom.place(relx=0.375, rely=0.05, relwidth=0.25, relheight = 0.075)

        etiquetaAP= ctk.CTkLabel(self, text= "Apellido Paterno:", **etiquetaStyle)
        etiquetaAP.place(relx=0.05, rely=0.15, relwidth=0.25, relheight = 0.075)

        self.enAP = ctk.CTkEntry(self, placeholder_text="Escriba el Apellido", **entryStyle)
        self.enAP.place(relx=0.375, rely=0.15, relwidth=0.25, relheight = 0.075)

        etiquetaAM= ctk.CTkLabel(self, text= "Apellido Materno:", **etiquetaStyle)
        etiquetaAM.place(relx=0.05, rely=0.25, relwidth=0.25, relheight = 0.075)

        self.enAM = ctk.CTkEntry(self, placeholder_text="Escriba el Apellido", **entryStyle)
        self.enAM.place(relx=0.375, rely=0.25, relwidth=0.25, relheight = 0.075)


 #       butARFID = ctk.CTkButton(self, text= "asignar RFID", **estiloBoton, command = rfidA)
  #      butARFID.place(relx=0.05, rely=0.45, relwidth=0.25, relheight = 0.075)

        butGuargarAA = ctk.CTkButton(self, text= "Guardar", **estiloBotonBlue, command= self.guardar )
        butGuargarAA.place(relx=0.875, rely=0.9, relwidth=0.1, relheight = 0.075)

        self.mensaje1_text = ""
        self.mensaje1 = ctk.CTkLabel(self, text="")
        self.mensaje1.place(relx=0.325, rely=0.45, relwidth=0.25, relheight=0.075)

        
        

    def start_obtener_uid_thread(self):
        self.mensaje1.configure(text="Acerque el Tag")
        self.thread_obtener_uid = threading.Thread(target=RC().obtener_uid)
        self.thread_obtener_uid.start()
        self.after(100, self.check_thread)

   # def obtener_uid_thread(self):
    #    rc = RC()
     #   self.uid = rc.obtener_uid()
      #  print(self.uid)


    def check_thread(self):
        if self.thread_obtener_uid and not self.thread_obtener_uid.is_alive():
            self.mensaje1.configure(text=self.mensaje1_text)
            self.after(3000, lambda: self.mensaje1.configure(text=""))
        else:
            self.after(100, self.check_thread)


#Funcion del Boton Guardar
    def guardar(self):
        conn = connect_to_db()
        cursor = conn.cursor()

        global uidTC
        global grupo_id
        nombreAlum = self.enNom.get()
        apePMaes = self.enAP.get()
        apeMMaes = self.enAM.get()

        # Verificamos que se hayan ingresado todos los campos
        if nombreAlum != "" and apePMaes != "" and apeMMaes != "" and uidTC != "" and grupo_id != "":
            sql = "INSERT INTO maestro (nombre, apellidoPaterno, apellidoMaterno, RFIDcard) VALUES (%s, %s, %s, %s)"
            val = (nombreAlum, apePMaes, apeMMaes, uidTC)
            cursor.execute(sql, val)
            conn.commit()
            print("Maestro agregado exitosamente")

            # Borramos el texto de los campos del formulario
            self.enNom.delete(0, tk.END)
            self.enAP.delete(0, tk.END)
            self.enAM.delete(0, tk.END)

        else:
            print("Por favor complete todos los campos")

        conn.close()
    

class VerAsistencia(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x500")
        self.title("Ver Asistencia")


        # Crear cuadros de texto para ingresar la materia y la fecha
        materia_label = tk.Label(self, text="Materia:")
        materia_label.grid(row=0, column=0)

        materia_entry = tk.Entry(self)
        materia_entry.grid(row=0, column=1)

        fecha_label = tk.Label(self, text="Fecha (AAAA-MM-DD):")
        fecha_label.grid(row=1, column=0)

        fecha_entry = tk.Entry(self)
        fecha_entry.grid(row=1, column=1)

        # Crear treeview para mostrar los resultados
        resultados_treeview = ttk.Treeview(self, columns=("nombre", "hora_de_entrada"))
        resultados_treeview.heading("nombre", text="Nombre")
        resultados_treeview.heading("hora_de_entrada", text="Hora de entrada")
        resultados_treeview.grid(row=2, column=0, columnspan=2)

        # Función para mostrar la tabla de asistencia
        def mostrar_asistencia():
            conn = connect_to_db()
            # Obtener la materia y fecha ingresadas
            materia = materia_entry.get()
            fecha = fecha_entry.get()

            # Limpiar el treeview
            resultados_treeview.delete(*resultados_treeview.get_children())

            # Crear cursor para ejecutar la consulta
            cursor = conn.cursor()

            # Consulta SQL para obtener la información de asistencia según la materia y fecha especificadas
            query = "SELECT alumno.nombre, asistencia.hora_de_entrada FROM asistencia JOIN alumno ON asistencia.alumno_id = alumno.id JOIN materia ON asistencia.materia_id = materia.id WHERE materia.nombre = %s AND asistencia.fecha = %s"

            # Ejecutar la consulta
            cursor.execute(query, (materia, fecha))

            # Obtener los resultados de la consulta
            resultados = cursor.fetchall()

            # Mostrar los resultados en el treeview
            if len(resultados) > 0:
                for resultado in resultados:
                    resultados_treeview.insert("", tk.END, values=resultado)
            else:
                resultados_treeview.insert("", tk.END, text="No se encontraron resultados")

            # Botón para mostrar la tabla de asistencia
        self.mostrar_boton = ctk.CTkButton(self, text="Mostrar asistencia", command=mostrar_asistencia)
        self.mostrar_boton.grid(row=5, column=0, columnspan=3)


class AgregarGrupo(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x500")
        self.title("Agregar Grupo Nuevo")


        etiquetaGG = ctk.CTkLabel(self, text = "Grado y Grupo", **etiquetaStyle)
        etiquetaGG.place(relx=0.05, rely=0.05, relwidth=0.25, relheight = 0.075)

        self.enNom = ctk.CTkEntry(self, placeholder_text="Escriba el Grado y Grupo", **entryStyle)
        self.enNom.place(relx=0.375, rely=0.05, relwidth=0.25, relheight = 0.075)

        butGuargarAA = ctk.CTkButton(self, text= "Guardar", **estiloBotonBlue, command= self.guardar )
        butGuargarAA.place(relx=0.875, rely=0.9, relwidth=0.1, relheight = 0.075)



        self.especialidad_seleccionado = tk.StringVar(self)
        self.especialidad_seleccionado.set("Seleccione una Espacialidad")


        conn = connect_to_db()
        cursor = conn.cursor()


        
        cursor.execute("SELECT nombre FROM especialidad")
        especialidad_disponibles = [row[0] for row in cursor.fetchall()]

        conn.close()





        def obtener_especialidad_id(opcion_seleccionada1):
            global especialidad_id
            conn = connect_to_db()
            cursor = conn.cursor()
            
            cursor.execute("SELECT id FROM especialidad WHERE nombre = %s", (opcion_seleccionada1,))
            especialidad_id = cursor.fetchone()[0]
            print("grupo_id seleccionado:", especialidad_id)
            conn.close()
            return especialidad_id

# Creamos el OptionMenu y lo configuramos
        menu = tk.OptionMenu(self, self.especialidad_seleccionado, *especialidad_disponibles, command=obtener_especialidad_id)
        menu.place(relx=0.05, rely=0.15, relwidth=0.25, relheight=0.075)

    def guardar(self):
        conn = connect_to_db()
        cursor = conn.cursor()

        global especialidad_id

        grupoo = self.enNom.get()

        # Verificamos que se hayan ingresado todos los campos
        if grupoo != "" :
            sql = "INSERT INTO grupos (GradoYGrupo, especialidad_id) VALUES (%s, %s)"
            val = (grupoo, especialidad_id)
            cursor.execute(sql, val)
            conn.commit()
            print("Grupo agregado exitosamente")

            # Borramos el texto de los campos del formulario
            self.enNom.delete(0, tk.END)

        else:
            print("Por favor complete todos los campos")

        conn.close()
    

class AgregarEspecialidad(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x500")
        self.title("Agregar Especialidad")

        etiquetaE= ctk.CTkLabel(self, text = "Especialidad", **etiquetaStyle)
        etiquetaE.place(relx=0.05, rely=0.05, relwidth=0.25, relheight = 0.075)

        self.enNom = ctk.CTkEntry(self, placeholder_text="Escriba la especialidad", **entryStyle)
        self.enNom.place(relx=0.375, rely=0.05, relwidth=0.25, relheight = 0.075)

        butGuargarAA = ctk.CTkButton(self, text= "Guardar", **estiloBotonBlue, command= self.guardar )
        butGuargarAA.place(relx=0.875, rely=0.9, relwidth=0.1, relheight = 0.075)


    def guardar(self):
        conn = connect_to_db()
        cursor = conn.cursor()

        aespecialidaaa = self.enNom.get()

        # Verificamos que se hayan ingresado todos los campos
        if aespecialidaaa != "" :
            sql = "INSERT INTO especialidad (nombre) VALUES (%s)"
            val = (aespecialidaaa)
            cursor.execute(sql, val)
            conn.commit()
            print("Especialidad agregado exitosamente")

            # Borramos el texto de los campos del formulario
            self.enNom.delete(0, tk.END)

        else:
            print("Por favor complete todos los campos")

        conn.close()
    



class AgregarMateria(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x500")
        self.title("Agregar Nueva Materia")

        etiquetaMAT= ctk.CTkLabel(self, text = "Materia", **etiquetaStyle)
        etiquetaMAT.place(relx=0.05, rely=0.05, relwidth=0.25, relheight = 0.075)

        self.enNom = ctk.CTkEntry(self, placeholder_text="Escriba la Materia: ", **entryStyle)
        self.enNom.place(relx=0.375, rely=0.05, relwidth=0.25, relheight = 0.075)

        butGuargarAA = ctk.CTkButton(self, text= "Guardar", **estiloBotonBlue, command= self.guardar )
        butGuargarAA.place(relx=0.875, rely=0.9, relwidth=0.1, relheight = 0.075)


    def guardar(self):
        conn = connect_to_db()
        cursor = conn.cursor()

        materiaaa = self.enNom.get()

        # Verificamos que se hayan ingresado todos los campos
        if materiaaa != "" :
            sql = "INSERT INTO materia (nombre) VALUES (%s)"
            val = (materiaaa)
            cursor.execute(sql, val)
            conn.commit()
            print("Materia agregado exitosamente")

            # Borramos el texto de los campos del formulario
            self.enNom.delete(0, tk.END)

        else:
            print("Por favor complete todos los campos")

        conn.close()
    

class AgregarHorario(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x500")
        self.title("Agregar Horario")

        conn = connect_to_db()
        cursor = conn.cursor()

        def obtener_grupoidhorario(opcion_seleccionada2):
            global grupo_idhorario
            opcion_seleccionada2 = str(opcion_seleccionada2)  # convertir a cadena

            parametros = (opcion_seleccionada2,)
            cursor.execute("SELECT id FROM grupos WHERE GradoYGrupo = %s", parametros)
            grupo_idhorario = cursor.fetchone()
            if grupo_idhorario:
                grupo_idhorario = grupo_idhorario[0]
                print("grupo_id seleccionado:", grupo_idhorario)
            else:
                print("No se encontró el grupo seleccionado")
            return grupo_idhorario

        self.grupo = tk.StringVar(self)
        self.grupo.set("Seleccione Una Opcion")

        cursor.execute("SELECT e.nombre, g.GradoYGrupo FROM grupos g JOIN especialidad e ON g.especialidad_id = e.id")
        grupos_disponibles = [(row[0] + " (" + row[1] + ")",) for row in cursor.fetchall()]

        menu1 = tk.OptionMenu(self, self.grupo, *grupos_disponibles, command=obtener_grupoidhorario)
        menu1.place(relx=0.05, rely=0.05, relwidth=0.25, relheight=0.075)

        conn.close()







        
        self.materiaVar = tk.StringVar(self)
        self.materiaVar.set("Selecciona Una Opcion")

        self.maestroVar = tk.StringVar(self)
        self.maestroVar.set("Selecciona Una Opcion")

        self.moduloVar = tk.StringVar(self)
        self.moduloVar.set("Selecciona Una Opcion")

        self.diasVar = tk.StringVar(self)
        self.diasVar.set("Seleccione Una Opcion")

        

       
        

        #PAra materia: 

        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("SELECT nombre FROM materia")
        materias_disponibles = [row[0] for row in cursor.fetchall()]

        conn.close()

        def obtener_materiaidhorario(opcion_seleccionada3):
            global modulo_idhoraio
            conn = connect_to_db()
            cursor = conn.cursor()
            
            cursor.execute("SELECT id FROM materia WHERE nombre = %s", (opcion_seleccionada3,))
            modulo_idhorario = cursor.fetchone()[0]
            print("modulo_id seleccionado:", modulo_idhorario)
            conn.close()
            return modulo_idhorario


        #PAra modulo: 

        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("SELECT hora_inicio, hora_fin FROM modulos")
        modulo_disponibles = [(row[0], row[1]) for row in cursor.fetchall()]

        conn.close()

        def obtener_moduloidhorario(opcion_seleccionada4):
            global modulo_idhorario
            conn = connect_to_db()
            cursor = conn.cursor()
    
            cursor.execute("SELECT id FROM modulos WHERE hora_inicio = %s AND hora_fin = %s", (opcion_seleccionada4, ))
            modulo_idhorario = cursor.fetchone()[0]
            print("modulo_id seleccionado:", modulo_idhorario)
            conn.close()
            return modulo_idhorario



        #PAra maestro: 

        conn = connect_to_db()
        cursor = conn.cursor()

        cursor.execute("SELECT nombre, apellidoPaterno FROM maestro")
        maestro_disponibles = [(row[0], row[1]) for row in cursor.fetchall()]

        conn.close()

        def obtener_maestroidhorario(opcion_seleccionada5):
            global maestro_idhorario
            conn = connect_to_db()
            cursor = conn.cursor()
    
            cursor.execute("SELECT id FROM maestro WHERE nombre = %s AND apellidoPaterno = %s", (opcion_seleccionada5, None))
            maestro_idhorario = cursor.fetchone()[0]
            print("modulo_id seleccionado:", maestro_idhorario)
            conn.close()
            return maestro_idhorario


        


        menu2 = tk.OptionMenu(self, self.materiaVar, *materias_disponibles, command=obtener_materiaidhorario)
        menu2.place(relx=0.05, rely=0.15, relwidth=0.25, relheight=0.075)


        menu3 = tk.OptionMenu(self, self.moduloVar, *modulo_disponibles, command=obtener_moduloidhorario)
        menu3.place(relx=0.05, rely=0.25, relwidth=0.25, relheight=0.075)


        dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
        self.diasVar.set(dias[0])
        dias_menu = tk.OptionMenu(self, self.diasVar, *dias)
        dias_menu.place(relx=0.05, rely=0.35, relwidth=0.25, relheight=0.075)


        menu4 = tk.OptionMenu(self, self.maestroVar, *maestro_disponibles, command=obtener_maestroidhorario)
        menu4.place(relx=0.05, rely=0.45, relwidth=0.25, relheight=0.075)


        butGuargarAA = ctk.CTkButton(self, text= "Guardar", **estiloBotonBlue, command= self.guardar )
        butGuargarAA.place(relx=0.875, rely=0.9, relwidth=0.1, relheight = 0.075)



    def guardar(self):
        conn = connect_to_db()
        cursor = conn.cursor()

        global materia_idhorario
        global grupo_idhorario
        global modulo_idhorario
        global maestro_idhorario

        diaas = self.diasVar.get()


        # Verificamos que se hayan ingresado todos los campos
        if diaas != "" and materia_idhorario != "" and grupo_id !="" and modulo_idhorario != "" and maestro_idhorario:
            sql = "INSERT INTO horario (grupo_id, dia, materia_id, maestro_id, modulo_id) VALUES (%s, %s, %s, %s, %s)"
            val = (grupo_idhorario, diaas, materia_idhorario, maestro_idhorario, modulo_idhorario)
            cursor.execute(sql, val)
            conn.commit()
            print("Materia agregado exitosamente")

        else:
            print("Por favor complete todos los campos")

        conn.close()
    



class AgregarModulo(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x500")
        self.title("Agregar Nuevo Modulo")



class AsignarTagAlum(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x500")
        self.title("Asignar Tag a Alumno")

class AsignarTagMaestro(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x500")
        self.title("Asignar Tag a Maestro")



app = App()
app.mainloop()




















