class Personaje:
    def __init__(self, nombre, altura, velocidad, resistencia, fuerza):
        self.nombre = nombre
        self.altura = altura
        self.velocidad = velocidad
        self.resistencia = resistencia
        self.fuerza = fuerza
        self.estado = True 

    def atacar(self, otro_personaje):
        
        if self.estado and otro_personaje.estado:
            dano = self.fuerza - otro_personaje.resistencia
            dano = max(dano, 0)  
            print(f"{self.nombre} ataca a {otro_personaje.nombre} y le inflige {dano} de daño.")
            otro_personaje.recibir_dano(dano)
        else:
            print(f"{self.nombre} no puede atacar porque está fuera de juego.")

    def recibirDano(self, cantidad):
       
        self.resistencia = cantidad
        if self.resistencia <= 0:
            self.estado = False
            self.resistencia = 0
            print(f"{self.nombre} ha muerto.")
        else:
            print(f"{self.nombre} ha recibido {cantidad} de daño y ahora tiene {self.resistencia} de resistencia.")

    def mostrarInfo(self):
  
        estado_texto = "vivo" if self.estado else "muerto"
        print(f"Nombre: {self.nombre}")
        print(f"Altura: {self.altura}")
        print(f"Velocidad: {self.velocidad}")
        print(f"Resistencia: {self.resistencia}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Estado: {estado_texto}")