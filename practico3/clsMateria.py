import sqlite3

class Materia:
    def __init__(self, nombre):
        self.nombre = nombre

    def guardar(self):
        conexion = sqlite3.connect('sistema_escolar.db')
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO Materia (nombre) VALUES (?)', (self.nombre,))
        conexion.commit()
        conexion.close()

    @staticmethod
    def modificar(id, nombre):
        conexion = sqlite3.connect('sistema_escolar.db')
        cursor = conexion.cursor()
        cursor.execute('UPDATE Materia SET nombre = ? WHERE id = ?', (nombre, id))
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id):
        conexion = sqlite3.connect('sistema_escolar.db')
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM Materia WHERE id = ?', (id,))
        conexion.commit()
        conexion.close()

    @staticmethod
    def consultar():
        conexion = sqlite3.connect('sistema_escolar.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Materia')
        materias = cursor.fetchall()
        conexion.close()
        return materias
