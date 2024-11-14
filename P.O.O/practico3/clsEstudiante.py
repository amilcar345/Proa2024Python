import sqlite3

class Estudiante:
    def __init__(self, legajo_id, dni, nombre, edad, fecha_nacimiento, curso, estado, email):
        self.legajo_id = legajo_id
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.curso = curso
        self.estado = estado
        self.email = email

    def agregar(self):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO estudiante (legajo_id, dni, nombre, edad, fecha_nacimiento, curso, estado, email)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (self.legajo_id, self.dni, self.nombre, self.edad, self.fecha_nacimiento, self.curso, self.estado, self.email))
        conexion.commit()
        conexion.close()

    def modificar(self):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE estudiante SET dni = ?, nombre = ?, edad = ?, fecha_nacimiento = ?, curso = ?, estado = ?, email = ?
            WHERE legajo_id = ?
        ''', (self.dni, self.nombre, self.edad, self.fecha_nacimiento, self.curso, self.estado, self.email, self.legajo_id))
        conexion.commit()
        conexion.close()

    def eliminar(self):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM estudiante WHERE legajo_id = ?', (self.legajo_id,))
        conexion.commit()
        conexion.close()
