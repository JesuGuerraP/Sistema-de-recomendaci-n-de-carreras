import sqlite3

# Crear conexión a la base de datos "carreras.db"
conn_carreras = sqlite3.connect('carreras.db')
cursor_carreras = conn_carreras.cursor()

# Crear tabla "Carreras" en la base de datos "carreras.db"
cursor_carreras.execute('''
    CREATE TABLE Carreras (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        descripcion_id INTEGER,
        modalidad TEXT,
        campus TEXT,
        areas_estudio TEXT,
        habilidades_requeridas TEXT,
        intereses_relacionados TEXT,
        salidas_profesionales TEXT,
        FOREIGN KEY (descripcion_id) REFERENCES Descripciones(id)
    )
''')

# Guardar cambios y cerrar conexión
conn_carreras.commit()
conn_carreras.close()