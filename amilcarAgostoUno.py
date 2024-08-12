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
