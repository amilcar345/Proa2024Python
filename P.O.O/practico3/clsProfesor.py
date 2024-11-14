import sqlite3
class Profesor:
    def __init__(self, dni_id, nombre, apellido, curso, estado, email):
        self.dni_id = dni_id
        self.nombre = nombre
        self.apellido = apellido
        self.curso = curso
        self.estado = estado
        self.email = email

    def agregar(self):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO profesor (dni_id, nombre, apellido, curso, estado, email)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.dni_id, self.nombre, self.apellido, self.curso, self.estado, self.email))
        conexion.commit()
        conexion.close()

    def modificar(self):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute('''
            UPDATE profesor SET nombre = ?, apellido = ?, curso = ?, estado = ?, email = ?
            WHERE dni_id = ?
        ''', (self.nombre, self.apellido, self.curso, self.estado, self.email, self.dni_id))
        conexion.commit()
        conexion.close()

    def eliminar(self):
        conexion = sqlite3.connect('escuela.db')
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM profesor WHERE dni_id = ?', (self.dni_id,))
        conexion.commit()
        conexion.close()
