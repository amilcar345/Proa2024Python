from Personaje_clase import Personaje
def crear_personaje():
    nombre = input("Ingrese el nombre del personaje: ")
    altura = float(input("Ingrese la altura del personaje (en metros): "))
    velocidad = float(input("Ingrese la velocidad del personaje (en m/s): "))
    resistencia = int(input("Ingrese la resistencia del personaje (1-100): "))
    fuerza = int(input("Ingrese la fuerza del personaje (1-100): "))
    return Personaje(nombre, altura, velocidad, resistencia, fuerza)


def mostrar_menu():
    print("\nMenú:")
    print("1. Crear primer personaje")
    print("2. Crear segundo personaje")
    print("3. Mostrar información del primer personaje")
    print("4. Mostrar información del segundo personaje")
    print("5. Salir")

personaje1 = None
personaje2 = None

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        personaje1 = crear_personaje()
        print("Primer personaje creado con éxito.")
    elif opcion == "2":
        personaje2 = crear_personaje()
        print("Segundo personaje creado con éxito.")
    elif opcion == "3":
        if personaje1:
            print("\nInformación del primer personaje:")
            print(personaje1.mostrar_info())
        else:
            print("El primer personaje no ha sido creado.")
    elif opcion == "4":
        if personaje2:
            print("\nInformación del segundo personaje:")
            print(personaje2.mostrar_info())
        else:
            print("El segundo personaje no ha sido creado.")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
 