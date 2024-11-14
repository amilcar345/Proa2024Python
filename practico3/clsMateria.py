import sqlite3

class Materia:
    def __init__(self, id_materia, nombre, curso, descripcion, horario):
        self.id_materia = id_materia
        self.nombre = nombre
        self.curso = curso
        self.descripcion = descripcion
        self.horario = horario

    def agregar(self):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO materia (id_materia, nombre, curso, descripcion, horario)
            VALUES (?, ?, ?, ?, ?)
        ''', (self.id_materia, self.nombre, self.curso, self.descripcion, self.horario))
        conexion.commit()
        conexion.close()

    def modificar(self):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE materia SET nombre = ?, curso = ?, descripcion = ?, horario = ?
            WHERE id_materia = ?
        ''', (self.nombre, self.curso, self.descripcion, self.horario, self.id_materia))
        conexion.commit()
        conexion.close()

    def eliminar(self):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM materia WHERE id_materia = ?', (self.id_materia,))
        conexion.commit()
        conexion.close()
