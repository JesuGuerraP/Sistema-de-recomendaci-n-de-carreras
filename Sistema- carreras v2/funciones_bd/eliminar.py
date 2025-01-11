import sqlite3

# Conexión a la base de datos "carreras.db"
conn_carreras = sqlite3.connect('carreras.db')
cursor_carreras = conn_carreras.cursor()

# ID de la fila que deseas eliminar
id_fila_a_eliminar = 13# Por ejemplo, si deseas eliminar la fila con ID 1

# Sentencia SQL para eliminar la fila con el ID especificado
cursor_carreras.execute('''
    DELETE FROM Carreras
    WHERE id = ?
''', (id_fila_a_eliminar,))

# Guardar cambios y cerrar conexión
conn_carreras.commit()
conn_carreras.close()