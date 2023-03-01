import datetime
from src.conexion import connect_to_db
from src.agregaralumno import Alumno
from src.agregarmaestros import Maestro
from src.especialidad import Especialidad
from src.materia import Materia
from src.agregarGrupo import Grupo
from src.horario import Horario
from src.modulos import Modulo
from src.PRUEBAregistroconRC import Asistencia
from src.asignarRC import asignarRC

alumno = Alumno()
maestro= Maestro()
asistenciaa= Asistencia()
especialidad= Especialidad()
materia= Materia()
horario = Horario()
grupo = Grupo()
modulo = Modulo()



class todo:

    def registrar_asistencia(alumno_id):
        conn = connect_to_db()
        cur = conn.cursor()
        fecha = datetime.now().date()
        hora = datetime.now().time()
        cur.execute("INSERT INTO asistencia (alumno_id, fecha, asistio) VALUES (%s, %s, %s)", (alumno_id, fecha, True))
        conn.commit()
        print("La asistencia del alumno ha sido registrada con éxito.")

    def generar_tabla_asistencia(clase_id):
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("SELECT alumno.nombre, alumno.apellidoPaterno, alumno.apellidoMaterno, asistencia.fecha, asistencia.asistio FROM alumno JOIN asistencia ON alumno.id = asistencia.alumno_id WHERE alumno.clase_id = %s", (clase_id,))
        resultados = cur.fetchall()
        print("Nombre\t\tApellido Paterno\t\tApellido Materno\t\tFecha\t\tAsistió")
        for resultado in resultados:
            nombre = resultado[0]
            apellido_paterno = resultado[1]
            apellido_materno = resultado[2]
            fecha = resultado[3]
            asistio = resultado[4]
            print("{}\t\t{}\t\t{}\t\t{}\t\t{}".format(nombre, apellido_paterno, apellido_materno, fecha, asistio))

while True:
    def menu_principal():
        print("Bienvenido a la aplicación de asistencia escolar")
        print("1. Agregar alumno")
        print("2. Agregar maestro")
        print("3. Registrar asistencia de alumno")
        print("4. Ver asistencia de clase")
        print("5. agregar grupo")
        print("6. agregar especialidad")
        print("7. agregar materias")
        print("8. agregar horario")
        print("9. agregar modulos")
        print("10. Asignar Rfid nuevo a alumno")
        print("0. salir")
        opcion = int(input("Seleccione una opción: "))
        todoall= todo()
        if opcion == 1:
            alumno.add_alumno()
        elif opcion == 2:
            maestro.agregar_maestro()
        elif opcion == 3:
            asistenciaa.run()
        elif opcion == 4:
            todoall.generar_tabla_asistencia()
        elif opcion == 5:
            grupo.obtener_datos_grupo()
        elif opcion == 6:
            especialidad.obtener_datos_especialidad()
        elif opcion ==7 :
            materia.obtener_datos_materia()
        elif opcion ==8 :
            horario.obtener_datos_horario()
        elif opcion ==9 :
            modulo.obtener_datos_modulo()
        elif opcion ==10 :
            asignarRC()
        elif opcion == 0:
            print("Saliendo de la aplicación...")
            exit()
        else:
            print("Opción inválida, por favor seleccione una opción válida.")
    menu_principal()
