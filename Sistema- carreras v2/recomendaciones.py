import sqlite3
import numpy as np
from scipy.spatial.distance import cosine
import tkinter as tk

# Cargar los intereses y habilidades únicos desde los archivos
with open('txt_generados/intereses_unicos.txt', 'r') as file:
    intereses_unicos = file.read().splitlines()

with open('txt_generados/habilidades_unicas.txt', 'r') as file:
    habilidades_unicas = file.read().splitlines()

# Cargar el vector de características normalizado
with open('txt_generados/vector_caracteristicas_normalizado.txt', 'r') as file:
    vector_caracteristicas = []
    for line in file:
        nombre, vector_str = line.strip().split(': ')
        vector = [float(x) for x in vector_str.split(', ')]
        vector_caracteristicas.append((nombre, vector))

# Calcular la matriz de similitud entre carreras
similitud_carreras = np.zeros((len(vector_caracteristicas), len(vector_caracteristicas)))
for i in range(len(vector_caracteristicas)):
    for j in range(len(vector_caracteristicas)):
        similitud_carreras[i][j] = 1 - cosine(vector_caracteristicas[i][1], vector_caracteristicas[j][1])

# Función para recomendar carreras a un usuario
def recomendar_carreras(intereses, habilidades, n_recomendaciones=5):
    usuario_vector = [0] * (len(intereses_unicos) + len(habilidades_unicas))
    
    for interes in intereses:
        if interes in intereses_unicos:
            usuario_vector[intereses_unicos.index(interes)] = 1
    
    for habilidad in habilidades:
        if habilidad in habilidades_unicas:
            usuario_vector[len(intereses_unicos) + habilidades_unicas.index(habilidad)] = 1
    
    similitudes = [1 - cosine(usuario_vector, vector) for _, vector in vector_caracteristicas]
    indices_similares = np.argsort(similitudes)[::-1]
    
    recomendaciones = []
    salidas_profesionales = []
    for i in indices_similares:
        recomendaciones.append(vector_caracteristicas[i][0])
        
        # Obtener las salidas profesionales de la carrera
        conn = sqlite3.connect('base_datos/carreras.db')
        c = conn.cursor()
        c.execute("SELECT salidas_profesionales FROM carreras WHERE nombre = ?", (vector_caracteristicas[i][0],))
        salida_profesional = c.fetchone()[0]
        conn.close()
        
        salidas_profesionales.append(salida_profesional)
        
        if len(recomendaciones) >= n_recomendaciones:
            break
    
    return recomendaciones, salidas_profesionales

# Función para actualizar el campo de texto con las selecciones
def actualizar_selecciones(event, listbox, entry):
    seleccion = [listbox.get(idx) for idx in listbox.curselection()]
    contenido_actual = entry.get('1.0', tk.END).strip().split(', ')
    contenido_actual = [item for item in contenido_actual if item]  # Filtrar elementos vacíos
    seleccion_completa = list(set(contenido_actual + seleccion))
    seleccion_completa.sort(key=lambda x: (contenido_actual + seleccion).index(x))  # Mantener el orden de selección
    nuevas_selecciones = ', '.join(seleccion_completa)
    entry.delete('1.0', tk.END)
    entry.insert('1.0', nuevas_selecciones)
    ajustar_altura_entry(entry)

# Función para ajustar la altura del campo de entrada
def ajustar_altura_entry(entry):
    contenido = entry.get('1.0', tk.END).strip()
    lineas = contenido.count('\n') + 1
    entry.config(height=lineas)

# Función para mostrar/ocultar las listas desplegables
def toggle_listbox(frame, button, entry, entry_frame=None, shift_frame=None):
    if frame.winfo_viewable():
        frame.pack_forget()
        button.config(text="▼")
        if shift_frame is not None:
            shift_frame.pack_forget()  # Ocultar el frame desplazado
            entry_frame.pack(anchor='w', pady=5, fill='x')
    else:
        frame.place(x=entry.winfo_x(), y=entry.winfo_y() + entry.winfo_height() + 5)
        frame.lift()
        frame.pack(side='top', fill='both', expand=True)
        button.config(text="▲")
        if shift_frame is not None:
            entry_frame.pack_forget()  # Ocultar el frame original
            shift_frame.pack(anchor='w', pady=5, fill='x')  # Mostrar el frame desplazado

