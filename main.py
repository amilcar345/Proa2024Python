 import sqlite3
 
from estudiante import Estudiante
from profesor import Profesor
from materia import Materia
from calificacion import Calificacion

def mostrar_menu():
    print("\nSistema Escolar")
    print("1. Gestionar Estudiantes")
    print("2. Gestionar Profesores")
    print("3. Gestionar Materias")
    print("4. Gestionar Calificaciones")
    print("5. Salir")
    return input("Elige una opción: ")

def menu_estudiantes():
    print("\n--- Gestión de Estudiantes ---")
    print("1. Agregar Estudiante")
    print("2. Modificar Estudiante")
    print("3. Eliminar Estudiante")
    print("4. Consultar Estudiantes")
    print("5. Volver al menú principal")
    return input("Elige una opción: ")

def gestionar_estudiantes():
    while True:
        opcion = menu_estudiantes()

        if opcion == '1':  # Agregar Estudiante
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = int(input("Edad: "))
            estudiante = Estudiante(nombre, apellido, edad)
            estudiante.guardar()
            print("Estudiante agregado con éxito.")
        
        elif opcion == '2':  # Modificar Estudiante
            id = int(input("ID del Estudiante a modificar: "))
            nombre = input("Nuevo Nombre: ")
            apellido = input("Nuevo Apellido: ")
            edad = int(input("Nueva Edad: "))
            Estudiante.modificar(id, nombre, apellido, edad)
            print("Estudiante modificado con éxito.")
        
        elif opcion == '3':  # Eliminar Estudiante
            id = int(input("ID del Estudiante a eliminar: "))
            Estudiante.eliminar(id)
            print("Estudiante eliminado con éxito.")
        
        elif opcion == '4':  # Consultar Estudiantes
            estudiantes = Estudiante.consultar()
            for est in estudiantes:
                print(f"ID: {est[0]}, Nombre: {est[1]}, Apellido: {est[2]}, Edad: {est[3]}")
        
        elif opcion == '5':  # Volver al menú principal
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_profesores():
    print("\n--- Gestión de Profesores ---")
    print("1. Agregar Profesor")
    print("2. Modificar Profesor")
    print("3. Eliminar Profesor")
    print("4. Consultar Profesores")
    print("5. Volver al menú principal")
    return input("Elige una opción: ")

def gestionar_profesores():
    while True:
        opcion = menu_profesores()

        if opcion == '1':  # Agregar Profesor
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            asignatura = input("Asignatura: ")
            profesor = Profesor(nombre, apellido, asignatura)
            profesor.guardar()
            print("Profesor agregado con éxito.")
        
        elif opcion == '2':  # Modificar Profesor
            id = int(input("ID del Profesor a modificar: "))
            nombre = input("Nuevo Nombre: ")
            apellido = input("Nuevo Apellido: ")
            asignatura = input("Nueva Asignatura: ")
            Profesor.modificar(id, nombre, apellido, asignatura)
            print("Profesor modificado con éxito.")
        
        elif opcion == '3':  # Eliminar Profesor
            id = int(input("ID del Profesor a eliminar: "))
            Profesor.eliminar(id)
            print("Profesor eliminado con éxito.")
        
        elif opcion == '4':  # Consultar Profesores
            profesores = Profesor.consultar()
            for prof in profesores:
                print(f"ID: {prof[0]}, Nombre: {prof[1]}, Apellido: {prof[2]}, Asignatura: {prof[3]}")
        
        elif opcion == '5':  # Volver al menú principal
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_materias():
    print("\n--- Gestión de Materias ---")
    print("1. Agregar Materia")
    print("2. Modificar Materia")
    print("3. Eliminar Materia")
    print("4. Consultar Materias")
    print("5. Volver al menú principal")
    return input("Elige una opción: ")

def gestionar_materias():
    while True:
        opcion = menu_materias()

        if opcion == '1':  # Agregar Materia
            nombre = input("Nombre de la Materia: ")
            materia = Materia(nombre)
            materia.guardar()
            print("Materia agregada con éxito.")
        
        elif opcion == '2':  # Modificar Materia
            id = int(input("ID de la Materia a modificar: "))
            nombre = input("Nuevo Nombre: ")
            Materia.modificar(id, nombre)
            print("Materia modificada con éxito.")
        
        elif opcion == '3':  # Eliminar Materia
            id = int(input("ID de la Materia a eliminar: "))
            Materia.eliminar(id)
            print("Materia eliminada con éxito.")
        
        elif opcion == '4':  # Consultar Materias
            materias = Materia.consultar()
            for mat in materias:
                print(f"ID: {mat[0]}, Nombre: {mat[1]}")
        
        elif opcion == '5':  # Volver al menú principal
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

def menu_calificaciones():
    print("\n--- Gestión de Calificaciones ---")
    print("1. Agregar Calificación")
    print("2. Modificar Calificación")
    print("3. Eliminar Calificación")
    print("4. Consultar Calificaciones")
    print("5. Volver al menú principal")
    return input("Elige una opción: ")

def gestionar_calificaciones():
    while True:
        opcion = menu_calificaciones()

        if opcion == '1':  # Agregar Calificación
            estudiante_id = int(input("ID del Estudiante: "))
            materia_id = int(input("ID de la Materia: "))
            nota = int(input("Nota: "))
            calificacion = Calificacion(estudiante_id, materia_id, nota)
            calificacion.guardar()
            print("Calificación agregada con éxito.")
        
        elif opcion == '2':  # Modificar Calificación
            id = int(input("ID de la Calificación a modificar: "))
            nota = int(input("Nueva Nota: "))
            Calificacion.modificar(id, nota)
            print("Calificación modificada con éxito.")
        
        elif opcion == '3':  # Eliminar Calificación
            id = int(input("ID de la Calificación a eliminar: "))
            Calificacion.eliminar(id)
            print("Calificación eliminada con éxito.")
        
        elif opcion == '4':  # Consultar Calificaciones
            calificaciones = Calificacion.consultar()
            for cal in calificaciones:
                print(f"ID: {cal[0]}, Estudiante ID: {cal[1]}, Materia ID: {cal[2]}, Nota: {cal[3]}")
        
        elif opcion == '5':  # Volver al menú principal
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            gestionar_estudiantes()
        elif opcion == '2':
            gestionar_profesores()
        elif opcion == '3':
            gestionar_materias()
        elif opcion == '4':
            gestionar_calificaciones()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")
