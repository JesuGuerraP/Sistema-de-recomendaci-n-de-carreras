import tkinter as tk
from tkinter import ttk
from tkinter import Text, Entry, Scrollbar, Frame, Listbox, Button, Label
from tkinter import messagebox
import recomendaciones as reco  # Importamos las funciones de recomendaciones desde el otro archivo

# Cargar los intereses y habilidades únicos desde los archivos
with open('txt_generados/intereses_unicos.txt', 'r') as file:
    intereses_unicos = file.read().splitlines()

with open('txt_generados/habilidades_unicas.txt', 'r') as file:
    habilidades_unicas = file.read().splitlines()

# Lógica para la interfaz gráfica
def actualizar_selecciones(event, listbox, entry):
    reco.actualizar_selecciones(event, listbox, entry)

def toggle_listbox(frame, button, entry, entry_frame=None, shift_frame=None):
    reco.toggle_listbox(frame, button, entry, entry_frame, shift_frame)

def obtener_recomendaciones():
    nombre = name_entry.get()
    intereses_seleccionados = [interes_listbox.get(idx) for idx in interes_listbox.curselection()]
    habilidades_seleccionadas = [habilidad_listbox.get(idx) for idx in habilidad_listbox.curselection()]
    
    recomendaciones, salidas_profesionales = reco.recomendar_carreras(intereses_seleccionados, habilidades_seleccionadas)
    
    resultado_label.config(text=f"Hola {nombre}, tus carreras recomendadas son:")
    for i, carrera in enumerate(recomendaciones):
        resultado_label.config(text=resultado_label.cget("text") + f"\n- {carrera}")
        resultado_label.config(text=resultado_label.cget("text") + f"\n  Salidas Profesionales: {salidas_profesionales[i]}")
    
    reiniciar_button.pack(pady=10)

def reiniciar_formulario():
    name_entry.delete(0, tk.END)
    city_combobox.set('')
    education_combobox.set('')
    interes_entry.delete('1.0', tk.END)
    habilidad_entry.delete('1.0', tk.END)
    interes_listbox.selection_clear(0, tk.END)
    habilidad_listbox.selection_clear(0, tk.END)
    resultado_label.config(text="")
    reiniciar_button.pack_forget()

# Interfaz de usuario
root = tk.Tk()
root.title("Sistema de Recomendación de Carreras")
root.configure(bg='#2e3f4f')

# Elementos de la interfaz
main_frame = tk.Frame(root, bg='#eaeaea', borderwidth=1, relief='solid')
main_frame.pack(fill='both', expand=True, padx=20, pady=20)

canvas = tk.Canvas(main_frame, bg='#eaeaea')
canvas.pack(side=tk.LEFT, fill='both', expand=True)

scrollbar = tk.Scrollbar(main_frame, orient='vertical', command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill='y')

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

content_frame = tk.Frame(canvas, bg='#ffffff', padx=40, pady=40)
canvas.create_window((0, 0), window=content_frame, anchor='nw')

title_label = tk.Label(content_frame, text="Sistema de Recomendación de Carreras", font=('Helvetica', 18, 'bold'), bg='#ffffff', fg='#34495e')
title_label.pack(pady=20)

name_label = tk.Label(content_frame, text="Nombre:", font=('Helvetica', 12), bg='#ffffff', fg='#34495e')
name_label.pack(anchor='w')

name_entry = tk.Entry(content_frame, font=('Helvetica', 12), width=30, borderwidth=2, relief='groove')
name_entry.pack(pady=5)

city_label = tk.Label(content_frame, text="Ciudad:", font=('Helvetica', 12), bg='#ffffff', fg='#34495e')
city_label.pack(anchor='w')

city_combobox = ttk.Combobox(content_frame, font=('Helvetica', 12), width=27, state='readonly')
city_combobox['values'] = ('Magangue', 'Cerete', 'San Juan', 'Lorica', 'Carmen de Bolívar', 'Mompox', 'Cartagena')
city_combobox.pack(pady=5)

education_label = tk.Label(content_frame, text="Nivel de Escolaridad:", font=('Helvetica', 12), bg='#ffffff', fg='#34495e')
education_label.pack(anchor='w')

education_combobox = ttk.Combobox(content_frame, font=('Helvetica', 12), width=27, state='readonly')
education_combobox['values'] = ('Secundaria', 'Bachillerato', 'Universidad', 'Posgrado')
education_combobox.pack(pady=5)

interes_label = tk.Label(content_frame, text="Intereses:", font=('Helvetica', 12), bg='#ffffff', fg='#34495e')
interes_label.pack(anchor='w', pady=10)

interes_frame = tk.Frame(content_frame)
interes_listbox = tk.Listbox(interes_frame, selectmode=tk.MULTIPLE, height=4, font=('Helvetica', 12), width=40, borderwidth=2, relief='groove')
for interes in intereses_unicos:
    interes_listbox.insert(tk.END, interes)

interes_scrollbar = tk.Scrollbar(interes_frame, orient='vertical', command=interes_listbox.yview)
interes_listbox.config(yscrollcommand=interes_scrollbar.set)
interes_scrollbar.pack(side=tk.RIGHT, fill='y')
interes_listbox.pack(side=tk.LEFT, fill='both', expand=True)

interes_entry_frame = tk.Frame(content_frame)
interes_entry_frame.pack(anchor='w', pady=5, fill='x')
interes_entry = tk.Text(interes_entry_frame, font=('Helvetica', 12), width=50, height=1, wrap='word', borderwidth=2, relief='groove')
interes_entry.pack(side=tk.LEFT, fill='x', expand=True)
interes_button = tk.Button(interes_entry_frame, text="▼", font=('Helvetica', 12), bg='#007bff', fg='#ffffff', command=lambda: toggle_listbox(interes_frame, interes_button, interes_entry))
interes_button.pack(side='left', padx=(5, 0))

# Frame que se desplaza cuando la lista de intereses se despliega
interes_shift_frame = tk.Frame(content_frame)
interes_shift_frame.pack_forget()

# Añadir el entry y button del campo de habilidades al frame que se desplaza
habilidad_label = tk.Label(interes_shift_frame, text="Habilidades:", font=('Helvetica', 12), bg='#ffffff', fg='#34495e')
habilidad_label.pack(anchor='w', pady=10)

habilidad_frame = tk.Frame(content_frame)
habilidad_listbox = tk.Listbox(habilidad_frame, selectmode=tk.MULTIPLE, height=4, font=('Helvetica', 12), width=40, borderwidth=2, relief='groove')
for habilidad in habilidades_unicas:
    habilidad_listbox.insert(tk.END, habilidad)

habilidad_scrollbar = tk.Scrollbar(habilidad_frame, orient='vertical', command=habilidad_listbox.yview)
habilidad_listbox.config(yscrollcommand=habilidad_scrollbar.set)
habilidad_scrollbar.pack(side=tk.RIGHT, fill='y')
habilidad_listbox.pack(side=tk.LEFT, fill='both', expand=True)

habilidad_entry_frame = tk.Frame(interes_shift_frame)
habilidad_entry_frame.pack(anchor='w', pady=5, fill='x')
habilidad_entry = tk.Text(habilidad_entry_frame, font=('Helvetica', 12), width=50, height=1, wrap='word', borderwidth=2, relief='groove')
habilidad_entry.pack(side=tk.LEFT, fill='x', expand=True)
habilidad_button = tk.Button(habilidad_entry_frame, text="▼", font=('Helvetica', 12), bg='#007bff', fg='#ffffff', command=lambda: toggle_listbox(habilidad_frame, habilidad_button, habilidad_entry))
habilidad_button.pack(side='left', padx=(5, 0))

# Actualizar el campo de entrada al seleccionar elementos de la lista de intereses
interes_listbox.bind('<<ListboxSelect>>', lambda event: actualizar_selecciones(event, interes_listbox, interes_entry))

# Actualizar el campo de entrada al seleccionar elementos de la lista de habilidades
habilidad_listbox.bind('<<ListboxSelect>>', lambda event: actualizar_selecciones(event, habilidad_listbox, habilidad_entry))

# Añadir el frame que se desplaza al content frame
interes_shift_frame.pack(anchor='w', pady=5, fill='x')

recomendar_button = tk.Button(content_frame, text="Recomendar Carreras", font=('Helvetica', 12), bg='#28a745', fg='#ffffff', command=obtener_recomendaciones)
recomendar_button.pack(pady=20)

reiniciar_button = tk.Button(content_frame, text="Reiniciar", font=('Helvetica', 12), bg='#dc3545', fg='#ffffff', command=reiniciar_formulario)

resultado_label = tk.Label(content_frame, text="", font=('Helvetica', 12), bg='#ffffff', justify='left', fg='#34495e')
resultado_label.pack()

root.mainloop()
