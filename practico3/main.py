from clsEstudiante import Estudiante
from clsProfesor import Profesor
from clsMateria import Materia
from clsCalificacion import Calificacion
def main():
    while True:
        print("\n--- Sistema Escolar ---")
        print("1. Gestión de Estudiantes")
        print("2. Gestión de Profesores")
        print("3. Gestión de Materias")
        print("4. Gestión de Calificaciones")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
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
            print("Opción no válida. Intente de nuevo.")

def gestionar_estudiantes():
    while True:
        print("\n--- Gestión de Estudiantes ---")
        print("1. Agregar Estudiante")
        print("2. Modificar Estudiante")
        print("3. Eliminar Estudiante")
        print("4. Consultar Estudiante")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            legajo_id = int(input("Legajo ID: "))
            dni = int(input("DNI: "))
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            fecha_nacimiento = input("Fecha de nacimiento (AAAA-MM-DD): ")
            curso = input("Curso: ")
            estado = input("Estado: ")
            email = input("Email: ")
            
            estudiante = Estudiante(legajo_id, dni, nombre, edad, fecha_nacimiento, curso, estado, email)
            estudiante.agregar()
            print("Estudiante agregado con éxito.")
        
        elif opcion == '2':
            legajo_id = int(input("Legajo ID del estudiante a modificar: "))
            dni = int(input("Nuevo DNI: "))
            nombre = input("Nuevo Nombre: ")
            edad = int(input("Nueva Edad: "))
            fecha_nacimiento = input("Nueva Fecha de nacimiento (AAAA-MM-DD): ")
            curso = input("Nuevo Curso: ")
            estado = input("Nuevo Estado: ")
            email = input("Nuevo Email: ")
            
            estudiante = Estudiante(legajo_id, dni, nombre, edad, fecha_nacimiento, curso, estado, email)
            estudiante.modificar()
            print("Estudiante modificado con éxito.")
        
        elif opcion == '3':
            legajo_id = int(input("Legajo ID del estudiante a eliminar: "))
            estudiante = Estudiante(legajo_id, None, None, None, None, None, None, None)
            estudiante.eliminar()
            print("Estudiante eliminado con éxito.")
        
        elif opcion == '4':
            # Aquí podrías implementar la consulta de estudiantes en la base de datos
            print("Consulta de estudiantes (por implementar)")
        
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_profesores():
    while True:
        print("\n--- Gestión de Profesores ---")
        print("1. Agregar Profesor")
        print("2. Modificar Profesor")
        print("3. Eliminar Profesor")
        print("4. Consultar Profesor")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            dni_id = int(input("DNI ID: "))
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            curso = input("Curso: ")
            estado = input("Estado: ")
            email = input("Email: ")
            
            profesor = Profesor(dni_id, nombre, apellido, curso, estado, email)
            profesor.agregar()
            print("Profesor agregado con éxito.")
        
        elif opcion == '2':
            dni_id = int(input("DNI ID del profesor a modificar: "))
            nombre = input("Nuevo Nombre: ")
            apellido = input("Nuevo Apellido: ")
            curso = input("Nuevo Curso: ")
            estado = input("Nuevo Estado: ")
            email = input("Nuevo Email: ")
            
            profesor = Profesor(dni_id, nombre, apellido, curso, estado, email)
            profesor.modificar()
            print("Profesor modificado con éxito.")
        
        elif opcion == '3':
            dni_id = int(input("DNI ID del profesor a eliminar: "))
            profesor = Profesor(dni_id, None, None, None, None, None)
            profesor.eliminar()
            print("Profesor eliminado con éxito.")
        
        elif opcion == '4':
            print("Consulta de profesores (por implementar)")
        
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_materias():
    while True:
        print("\n--- Gestión de Materias ---")
        print("1. Agregar Materia")
        print("2. Modificar Materia")
        print("3. Eliminar Materia")
        print("4. Consultar Materia")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            id_materia = int(input("ID Materia: "))
            nombre = input("Nombre: ")
            curso = input("Curso: ")
            descripcion = input("Descripción: ")
            horario = input("Horario: ")
            
            materia = Materia(id_materia, nombre, curso, descripcion, horario)
            materia.agregar()
            print("Materia agregada con éxito.")
        
        elif opcion == '2':
            id_materia = int(input("ID Materia de la materia a modificar: "))
            nombre = input("Nuevo Nombre: ")
            curso = input("Nuevo Curso: ")
            descripcion = input("Nueva Descripción: ")
            horario = input("Nuevo Horario: ")
            
            materia = Materia(id_materia, nombre, curso, descripcion, horario)
            materia.modificar()
            print("Materia modificada con éxito.")
        
        elif opcion == '3':
            id_materia = int(input("ID Materia de la materia a eliminar: "))
            materia = Materia(id_materia, None, None, None, None)
            materia.eliminar()
            print("Materia eliminada con éxito.")
        
        elif opcion == '4':
            print("Consulta de materias (por implementar)")
        
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_calificaciones():
    while True:
        print("\n--- Gestión de Calificaciones ---")
        print("1. Agregar Calificación")
        print("2. Modificar Calificación")
        print("3. Eliminar Calificación")
        print("4. Consultar Calificación")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            id_estudiante = int(input("ID del Estudiante: "))
            id_materia = int(input("ID de la Materia: "))
            nota = float(input("Nota: "))
            fecha = input("Fecha (AAAA-MM-DD): ")
            
            calificacion = Calificacion(id_estudiante, id_materia, nota, fecha)
            calificacion.agregar()
            print("Calificación agregada con éxito.")
        
        elif opcion == '2':
            id_estudiante = int(input("ID del Estudiante: "))
            id_materia = int(input("ID de la Materia: "))
            nueva_nota = float(input("Nueva Nota: "))
            fecha = input("Nueva Fecha (AAAA-MM-DD): ")
            
            calificacion = Calificacion(id_estudiante, id_materia, nueva_nota, fecha)
            calificacion.modificar(nueva_nota)
            print("Calificación modificada con éxito.")
        
        elif opcion == '3':
            id_estudiante = int(input("ID del Estudiante: "))
            id_materia = int(input("ID de la Materia: "))
            
            calificacion = Calificacion(id_estudiante, id_materia, None, None)
            calificacion.eliminar()
            print("Calificación eliminada con éxito.")
        
        elif opcion == '4':
            print("Consulta de calificaciones (por implementar)")
        
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
