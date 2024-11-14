import sqlite3
class Calificacion:
    def __init__(self, id_estudiante, id_materia, nota, fecha):
        self.id_estudiante = id_estudiante
        self.id_materia = id_materia
        self.nota = nota
        self.fecha = fecha

    def agregar(self):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO calificacion (id_estudiante, id_materia, nota, fecha)
            VALUES (?, ?, ?, ?)
        ''', (self.id_estudiante, self.id_materia, self.nota, self.fecha))
        conexion.commit()
        conexion.close()

    def modificar(self, nueva_nota):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE calificacion SET nota = ?, fecha = ?
            WHERE id_estudiante = ? AND id_materia = ?
        ''', (nueva_nota, self.fecha, self.id_estudiante, self.id_materia))
        conexion.commit()
        conexion.close()

    def eliminar(self):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute('''
            DELETE FROM calificacion WHERE id_estudiante = ? AND id_materia = ?
        ''', (self.id_estudiante, self.id_materia))
        conexion.commit()
        conexion.close()
