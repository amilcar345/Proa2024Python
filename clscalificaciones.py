import sqlite3

class Calificacion:
    def __init__(self, estudiante_id, materia_id, nota):
        self.estudiante_id = estudiante_id
        self.materia_id = materia_id
        self.nota = nota

    def guardar(self):
        conexion = sqlite3.connect('sistema_escolar.db')
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO Calificacion (estudiante_id, materia_id, nota) VALUES (?, ?, ?)', 
                       (self.estudiante_id, self.materia_id, self.nota))
        conexion.commit()
        conexion.close()

    @staticmethod
    def modificar(id, nota):
        conexion = sqlite3.connect('sistema_escolar.db')
        cursor = conexion.cursor()
        cursor.execute('UPDATE Calificacion SET nota = ? WHERE id = ?', (nota, id))
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id):
        conexion = sqlite3.connect('sistema_escolar.db')
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM Calificacion WHERE id = ?', (id,))
        conexion.commit()
        conexion.close()

    @staticmethod
    def consultar():
        conexion = sqlite3.connect('sistema_escolar.db')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM Calificacion')
        calificaciones = cursor.fetchall()
        conexion.close()
        return calificaciones
