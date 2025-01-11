import sqlite3

# Conexión a la base de datos "descripciones.db"
conn_descripciones = sqlite3.connect('base_datos/descripciones.db')
cursor_descripciones = conn_descripciones.cursor()

# Consulta SQL para obtener las descripciones
cursor_descripciones.execute('SELECT * FROM Descripciones')
descripciones = cursor_descripciones.fetchall()

# Mostrar las descripciones
for descripcion in descripciones:
    print(descripcion)

# Cerrar conexión
conn_descripciones.close()