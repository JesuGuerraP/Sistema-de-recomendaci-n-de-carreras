import sqlite3

# Conexión a la base de datos "carreras.db"
conn_carreras = sqlite3.connect('base_datos/carreras.db')
cursor_carreras = conn_carreras.cursor()

# Consulta SQL para obtener los datos de las carreras 
cursor_carreras.execute('SELECT * FROM carreras')
carreras = cursor_carreras.fetchall()

#mostrar los datos de la carreras 
for datos_carrera in carreras:
    print(datos_carrera)

#cerrar conexion
conn_carreras.close()