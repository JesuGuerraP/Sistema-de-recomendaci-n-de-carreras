import sqlite3
import numpy as np

# Ruta del archivo "vector_caracteristicas.txt"
ruta_archivo = 'C:/Users/JESUS GUERRA/Desktop/Sistema- carreras/vector_caracteristicas.txt'

# Cargar el vector de características desde el archivo
with open(ruta_archivo, 'r') as file:
    vector_caracteristicas = []
    for line in file:
        nombre, vector_str = line.strip().split(': ')
        vector = [int(x) for x in vector_str.split(', ')]
        vector_caracteristicas.append((nombre, vector))

# Normalizar los valores
for i in range(len(vector_caracteristicas[0][1])):
    valores_columna = [vector[i] for _, vector in vector_caracteristicas]
    media = np.mean(valores_columna)
    desviacion_estandar = np.std(valores_columna)
    
    for j in range(len(vector_caracteristicas)):
        vector_caracteristicas[j][1][i] = (vector_caracteristicas[j][1][i] - media) / desviacion_estandar

# Ruta del archivo para guardar el vector de características normalizado
ruta_archivo_normalizado = 'C:/Users/JESUS GUERRA/Desktop/Sistema- carreras/vector_caracteristicas_normalizado.txt'

# Guardar el vector de características normalizado
with open(ruta_archivo_normalizado, 'w') as file:
    for nombre, vector in vector_caracteristicas:
        file.write(f"{nombre}: {', '.join(map(str, vector))}\n")