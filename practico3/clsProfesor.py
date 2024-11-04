import sqlite3

class Profesor:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def guardar(self):
        conexion = sqlite3.connect('sistema_escolar.db')
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO Estudiante (nombre, apellido, edad) VALUES (?, ?, ?)', 
                       (self.nombre, self.apellido, self.edad))
        conexion.commit()
        conexion.close()

    @staticmethod
    def modificar(id, nombre, apellido, edad):
        conexion = sqlite3.connect('sistema_escolar.db')
        cursor = conexion.cursor()
        cursor.execute('UPDATE Estudiante SET nombre = ?, apellido = ?, edad = ? WHERE id = ?', 
                       (nombre, apellido, edad, id))
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id):
        conexion = sqlite3.connect('sistema_escolar.db')
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM Estudiante WHERE id = ?', (id,))
        conexion.commit()
        conexion.close()

    @staticmethod
    def consultar():
        conexion = sqlite3.connect('sistema_escolar.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Estudiante')
        estudiantes = cursor.fetchall()
        conexion.close()
        return estudiantes
