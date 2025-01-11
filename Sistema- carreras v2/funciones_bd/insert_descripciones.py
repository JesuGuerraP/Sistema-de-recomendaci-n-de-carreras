import sqlite3

# Datos de las descripciones de las carreras
datos_descripciones = [
    'El Programa de Ingeniería de Alimentos de la Universidad de Cartagena forma profesionales en procesamiento, conservación y control de calidad de alimentos. Los graduados podrán trabajar en la industria alimentaria, laboratorios de control de calidad e instituciones de investigación y desarrollo, contribuyendo a la innovación y seguridad alimentaria.',
    'El programa presencial de Contaduría Pública de la Universidad de Cartagena forma profesionales en áreas contables, financieras y de control, combinando teoría y práctica. Prepara a los estudiantes para roles como contador, auditor, asesor financiero, consultor tributario y analista contable. Además, les brinda competencias para emprender, con un enfoque humanista y ético que promueve el desarrollo sostenible y el compromiso social.',
    'El programa de Medicina de la Universidad de Cartagena forma médicos con conocimientos en ciencias de la salud, habilidades clínicas y ética profesional. Los graduados pueden diagnosticar, tratar y prevenir enfermedades, y trabajar en hospitales, clínicas, consultorios y centros de investigación, brindando atención integral y contribuyendo al bienestar de la sociedad.',
    'La carrera de Administración de Empresas a distancia de la Universidad de Cartagena ofrece formación en planificación estratégica, gestión de operaciones, finanzas, mercadotecnia, recursos humanos y emprendimiento. Los egresados pueden ser gerentes, directores de proyectos, consultores, emprendedores y analistas de negocios. La modalidad a distancia permite estudiar de forma flexible con tutorías presenciales en varios centros tutoriales.',
    # Agrega más descripciones de carreras
]

# Conexión a la base de datos "descripciones.db"
conn_descripciones = sqlite3.connect('descripciones.db')
cursor_descripciones = conn_descripciones.cursor()

# Insertar descripciones de las carreras en la tabla "Descripciones"
for descripcion in datos_descripciones:
    cursor_descripciones.execute('''
        INSERT INTO Descripciones (descripcion)
        VALUES (?)
    ''', (descripcion,))

# Guardar cambios y cerrar conexión
conn_descripciones.commit()
conn_descripciones.close()
