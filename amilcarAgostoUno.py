def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1: Añadir una tarea")
    print("2: Ver todas las tareas")
    print("3: Marcar una tarea como completada")
    print("4: Salir")

def gestionar_tareas():
    tareas = [] 
    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")
        if opcion == "1":
            tarea = input("Escribe la nueva tarea: ")
            tareas.append(tarea)
            print(f"Tarea '{tarea}' añadida.\n")
        elif opcion == "2":
            if len(tareas) > 0:
                print("\nTareas pendientes:")
                for i in range(len(tareas)):
                    print(f"{i + 1}. {tareas[i]}")
            else:
                print("\nNo hay tareas pendientes.\n")
        elif opcion == "3":
            if tareas:
                numTarea = input("Introduce el número de la tarea que completaste: ")
                if numTarea.isdigit() and 1 <= int(numTarea) <= len(tareas):
                    tareaCompletada = tareas.pop(int(numTarea) - 1)
                    print(f"Tarea '{tareaCompletada}' marcada como completada.\n")
                else:
                    print("Número de tarea no válido.")
            else:
                print("\nNo hay tareas para marcar como completadas.\n")
        
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 4.")
gestionar_tareas()