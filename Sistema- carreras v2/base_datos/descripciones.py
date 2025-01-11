import sqlite3

# Crear conexión a la base de datos "descripciones.db"
conn_descripciones = sqlite3.connect('descripciones.db')
cursor_descripciones = conn_descripciones.cursor()

# Crear tabla "Descripciones" en la base de datos "descripciones.db"
cursor_descripciones.execute('''
    CREATE TABLE Descripciones (
        id INTEGER PRIMARY KEY,
        descripcion TEXT
    )
''')

# Guardar cambios y cerrar conexión
conn_descripciones.commit()
conn_descripciones.close()