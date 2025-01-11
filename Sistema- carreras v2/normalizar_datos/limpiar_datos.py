import sqlite3

# Conexión a la base de datos "carreras.db"
conn_carreras = sqlite3.connect('carreras.db')
cursor_carreras = conn_carreras.cursor()

# Consulta SQL para obtener los datos de intereses, habilidades y pasatiempos
cursor_carreras.execute('''
    SELECT intereses_relacionados, habilidades_requeridas
    FROM Carreras
''')

# Limpiar y formatear los datos
intereses_carreras = []
habilidades_carreras = []

for row in cursor_carreras:
    intereses = row[0].split(', ')
    habilidades = row[1].split(', ')
    
    intereses_carreras.extend(intereses)
    habilidades_carreras.extend(habilidades)

# Eliminar duplicados y convertir a conjuntos
intereses_unicos = set(intereses_carreras)
habilidades_unicas = set(habilidades_carreras)

# Cerrar conexión
conn_carreras.close()

# Guardar los datos limpios y formateados
with open('intereses_unicos.txt', 'w') as file:
    file.write('\n'.join(intereses_unicos))
    

with open('habilidades_unicas.txt', 'w') as file:
    file.write('\n'.join(habilidades_unicas))