from PersonajeClase import Personaje

def crearPersonaje():
    nombre = input("Ingresa el nombre del personaje: ")
    altura = float(input(f"Ingresa la altura de {nombre}: "))
    velocidad = float(input(f"Ingresa la velocidad de {nombre}: "))
    resistencia = int(input(f"Ingresa la resistencia de {nombre}: "))
    fuerza = int(input(f"Ingresa la fuerza de {nombre}: "))
    
    return Personaje(nombre, altura, velocidad, resistencia, fuerza)
print("Creando el primer personaje:")
personaje1 = crearPersonaje()

print("Creando el segundo personaje:")
personaje2 = crearPersonaje()
print("Información de los personajes antes del ataque:")
personaje1.mostrarInfo()
print()
personaje2.mostrarInfo()
print("Simulando el ataque del primer personaje al segundo:")
personaje1.atacar(personaje2)

print("Información de los personajes después del ataque:")
personaje1.mostrarInfo()
print()
personaje2.mostrarInfo()
