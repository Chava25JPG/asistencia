from prettytable import PrettyTable
from datetime import datetime, timedelta
from conexion import Conexion
from PruebaRC import obtener_uid
import smtplib
from tkinter import ttk
import tkinter as Tk

#from email.mime.text import MIMEText
#from email.mime.text import MIMEApplication
conexion=Conexion()
conn = conexion.connect_to_db()
cursor = conn.cursor()

class Asistencia:

    #def enviar_correo(destinatario, asunto, mensaje):
        # Configurar datos del servidor SMTP
        #servidor_smtp = 'smtp.gmail.com'
        #puerto_smtp = 587
        #correo_origen = 'saseza8@gmail.com' # Cambiar por tu dirección de correo electrónico
        #contrasena = 'anakhzhnwxumrnmi' # Cambiar por tu contraseña

        # Crear objeto de conexión SMTP y realizar autenticación
        #server = smtplib.SMTP(servidor_smtp, puerto_smtp)
        #server.starttls()
        #server.login(correo_origen, contrasena)

        # Crear mensaje de correo electrónico
        #correo = f"From: {correo_origen}\nTo: {destinatario}\nSubject: {asunto}\n\n{mensaje}"

        # Enviar correo electrónico
        #server.sendmail(correo_origen, destinatario, correo)

        # Cerrar conexión SMTP
        #server.quit()


    def get_maestro(self, rfid):
        sql_maestro = "SELECT * FROM maestro WHERE RFIDcard = %s"
        cursor.execute(sql_maestro, (rfid,))
        return cursor.fetchone()

    def get_alumno(self, rfid):
        sql_alumno = "SELECT a.id, a.nombre, a.apellidoPaterno, a.apellidoMaterno, g.GradoYGrupo, e.nombre FROM alumno a JOIN grupos g ON a.grupo_id = g.id JOIN especialidad e ON g.especialidad_id = e.id WHERE a.RFIDcard = %s"
        cursor.execute(sql_alumno, (rfid,))
        return cursor.fetchone()

    def get_horario(self, maestro_id, dia_de_la_semana):
        sql_horario = "SELECT materia_id, materia.nombre, modulos.hora_inicio, modulos.hora_fin FROM horario JOIN materia ON horario.materia_id = materia.id JOIN modulos ON horario.modulo_id = modulos.id WHERE horario.maestro_id = %s AND horario.dia = %s"
        cursor.execute(sql_horario, ( maestro_id, dia_de_la_semana))
        return cursor.fetchall()

    def obtener_materia_ids(self, maestro_id, dia_de_la_semana):
        horario = self.get_horario(maestro_id, dia_de_la_semana)
        materia_ids = [fila[0] for fila in horario]
        return materia_ids


    def registrar_asistencia(self, alumno_id, maestro_id, materia_id):
        sql_asistencia = "INSERT INTO asistencia (alumno_id, maestro_id, materia_id, hora_de_entrada, fecha, asistio) VALUES (%s, %s, %s, %s, %s, %s)"
        hora_actual = datetime.now().strftime('%H:%M:%S')
        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        cursor.execute(sql_asistencia, (alumno_id, maestro_id, materia_id, hora_actual, fecha_actual, True))
        conn.commit()


        # Obtener correo electrónico del tutor del alumno
        #cursor.execute("SELECT CorreoTutor FROM alumnos WHERE id = %s", (alumno_id,))
        #tutor = cursor.fetchone()[0]

        # Enviar correo electrónico al tutor del alumno
        #destinatario = tutor
        #asunto = f"Asistencia de {alumno_id} registrada"
        #mensaje = f"La asistencia de {alumno_id} ha sido registrada el {fecha_actual} a las {hora_actual}."
        #self.enviar_correo(destinatario, asunto, mensaje)


    def run(self):
        while True:
            print("Escanea el tag del maestro: ")
            uidM = obtener_uid()
            rfid = uidM

            maestro = self.get_maestro(rfid)
            if maestro:
                # Es maestro
                print("Maestro")
                t = PrettyTable(['Nombre', 'Apellido Paterno', 'Apellido Materno'])
                t.add_row([maestro[1], maestro[2], maestro[3]])
                print(t)

                # Obtener día de la semana actual
                dia_de_la_semana = input("Introduce el dia: ")#datetime.now().strftime('%A')

                # Obtener el horario del maestro para el día de la semana actual
                horario = self.get_horario(maestro[0], dia_de_la_semana)
                if horario:
                    # Pedir RFID del alumno para registrar la asistencia
                    while True:
                        print("escanea la tarjeta del alumno")
                        uidA = obtener_uid()
                        rfid_alumno = uidA
                        alumno = self.get_alumno(rfid_alumno)
                        if alumno:
                            alumno_id = alumno[0]
                            maestro_id = maestro[0]
                            materia_id = horario[0][0]
                            objeto.registrar_asistencia(alumno_id, maestro_id, materia_id)
                            print("Alumno",alumno[1] ,"registrado con exito")

                        else:
                            print("El RFID ingresado no corresponde a un alumno, Cerrando clase")


                            break
                else:
                    print("El maestro no tiene horario programado para hoy.")
            else:
                alumno = self.get_alumno(rfid)
                if alumno:
                    print("Primero debe accesar un maestro.")
                else:
                    print("El TAG ingresado no es válido. Intenta de nuevo.")

objeto = Asistencia()
objeto.run()

#asistencia= Asistencia()