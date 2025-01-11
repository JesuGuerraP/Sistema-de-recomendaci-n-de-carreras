# Sistema de Recomendación de Carreras

Este proyecto es un sistema de recomendación de carreras basado en los intereses y habilidades únicas del usuario. Utiliza una interfaz gráfica creada con Tkinter y funciones de recomendaciones, y se conecta a una base de datos SQLite para obtener información sobre las carreras.

## Descripción

El sistema permite a los usuarios ingresar su nombre, ciudad, nivel de escolaridad, intereses y habilidades. Basado en esta información, el sistema sugiere carreras posibles y salidas profesionales relacionadas. La aplicación tiene un diseño moderno y profesional con una interfaz intuitiva y fácil de usar.

## Requisitos

- Python 3.x
- Tkinter (incluido en la mayoría de las instalaciones de Python)
- NumPy
- SciPy
- Archivo `recomendaciones.py` con las funciones de recomendación
- Archivos `intereses_unicos.txt` y `habilidades_unicas.txt` con los datos de intereses y habilidades
- Base de datos SQLite `carreras.db` con información sobre las carreras

## Instalación

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python y las bibliotecas necesarias instaladas en tu sistema.
3. Ejecuta el archivo `main.py` para iniciar la aplicación.
   
## Uso

1. Ingresa tu nombre en el campo de texto correspondiente.
2. Selecciona tu ciudad y nivel de escolaridad de los menús desplegables.
3. Selecciona tus intereses y habilidades de las listas desplegables.
4. Haz clic en el botón "Recomendar Carreras" para obtener recomendaciones basadas en tus entradas.
5. Las recomendaciones aparecerán en la parte inferior de la interfaz.

## Funciones Principales

- `actualizar_selecciones(event, listbox, entry)`: Actualiza los campos de selección según las listas seleccionadas.
- `toggle_listbox(frame, button, entry, entry_frame=None, shift_frame=None)`: Controla la visibilidad de las listas desplegables.
- `obtener_recomendaciones()`: Obtiene las recomendaciones de carreras basadas en los intereses y habilidades seleccionados.
- `reiniciar_formulario()`: Reinicia todos los campos del formulario a su estado inicial.
- `recomendar_carreras(intereses, habilidades, n_recomendaciones=5)`: Calcula las recomendaciones de carreras utilizando la similitud de coseno.
- `ajustar_altura_entry(entry)`: Ajusta la altura del campo de entrada basado en el contenido.


## Base de Datos

El sistema se conecta a una base de datos SQLite `carreras.db` para obtener información sobre las carreras. La estructura de la tabla `Carreras` es la siguiente:
CREATE TABLE Carreras ( id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, intereses_relacionados TEXT, habilidades_requeridas TEXT, salidas_profesionales TEXT );


## Contribuciones

Las contribuciones son bienvenidas. Si tienes sugerencias o mejoras, no dudes en crear un pull request o abrir un issue.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

¡Gracias por utilizar el Sistema de Recomendación de Carreras! Esperamos que te sea de gran ayuda en tu búsqueda de la carrera ideal.



