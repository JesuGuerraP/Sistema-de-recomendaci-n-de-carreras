import sqlite3

# Datos de las carreras
datos_carreras = [
    ('Administración Financiera', 15, 'Distancia', 'San juan, Carmen de bolivar, Mompox, Lorica, cerete, Magangué',
    'Finanzas, Contabilidad, Gestión de recursos financieros', 
    'Planeación financiera, Análisis de inversiones, Gestión de riesgos, Toma de decisiones financieras', 
    'Gestión financiera, Análisis de mercado, Planificación estratégica',
    'Analista financiero, Planificador financiero, Gerente financiero, Gestor de riesgos financieros')
    # Agrega más datos de carreras
]

# Conexión a la base de datos "carreras.db"
conn_carreras = sqlite3.connect('carreras.db')
cursor_carreras = conn_carreras.cursor()

# Insertar datos de las carreras en la tabla "Carreras"
for datos_carrera in datos_carreras:
    cursor_carreras.execute('''
        INSERT INTO Carreras (nombre, descripcion_id, modalidad, campus, areas_estudio, habilidades_requeridas, intereses_relacionados, salidas_profesionales)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', datos_carrera)

# Guardar cambios y cerrar conexión
conn_carreras.commit()
conn_carreras.close()