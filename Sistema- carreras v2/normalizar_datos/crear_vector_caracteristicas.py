import sqlite3

# Cargar los intereses y habilidades únicos desde los archivos
with open('intereses_unicos.txt', 'r') as file:
    intereses_unicos = file.read().splitlines()

with open('habilidades_unicas.txt', 'r') as file:
    habilidades_unicas = file.read().splitlines()

# Conexión a la base de datos "carreras.db"
conn_carreras = sqlite3.connect('carreras.db')
cursor_carreras = conn_carreras.cursor()

# Consulta SQL para obtener los datos de los usuarios
cursor_carreras.execute('''
    SELECT nombre, intereses_relacionados, habilidades_requeridas
    FROM Carreras
''')

# Crear el vector de características para cada usuario
vector_caracteristicas = []

for row in cursor_carreras:
    nombre = row[0]
    intereses = row[1].split(', ')
    habilidades = row[2].split(', ')
    
    vector_usuario = [0] * (len(intereses_unicos) + len(habilidades_unicas))
    
    for interes in intereses:
        if interes in intereses_unicos:
            vector_usuario[intereses_unicos.index(interes)] = 1
    
    for habilidad in habilidades:
        if habilidad in habilidades_unicas:
            vector_usuario[len(intereses_unicos) + habilidades_unicas.index(habilidad)] = 1
    
    vector_caracteristicas.append((nombre, vector_usuario))

# Cerrar conexión
conn_carreras.close()

# Guardar el vector de características
with open('vector_caracteristicas.txt', 'w') as file:
    for nombre, vector in vector_caracteristicas:
        file.write(f"{nombre}: {', '.join(map(str, vector))}\n")