Primeramente se creó el archivo app.py
Este archivo es el centro de nuestra aplicación y contiene la lógica principal para iniciar y ejecutar la app.

Configuración de la estructura de carpetas
Se organizó la estructura de carpetas para tener todo bien clasificado:
Carpeta static
Subcarpeta css: aquí está el archivo style.css con los estilos de la interfaz.
Subcarpeta js: contiene el archivo script.js con los scripts de JavaScript.

Carpeta templates
Contiene el archivo index.html, que define la estructura de la interfaz de usuario.

Carpeta venv
Aquí se encuentra el entorno virtual de Python.

Archivo Creation.py
Contiene la lógica para crear registros de chicas mágicas en la base de datos.

Archivo magical_girls.db
Base de datos que almacena la información de las chicas mágicas.

Archivo models.py
Define las clases y modelos utilizados en la base de datos.

Creación del entorno virtual
Se creó un entorno virtual en la carpeta venv para manejar las dependencias del proyecto de forma aislada. 
Esto nos permite que las bibliotecas y paquetes utilizados en este proyecto no interfieran con otros proyectos en el mismo sistema.

Instalación de dependencias
Se instalaron las dependencias necesarias para el proyecto, como Flask para la creación de la aplicación web y SQLAlchemy para la interacción con la base de datos.

Creación del modelo de datos
En el archivo models.py, se definieron las clases y modelos que se utilizarán en la base de datos. 
Esto incluye la propiedades de cada chica mágica, como id, nombre, edad, ciudad, raza, estado actual y fecha de contrato.

Desarrollo de la interfaz de usuario
Se creó el archivo index.html en la carpeta templates, que define la estructura básica de la interfaz de usuario. 
Este archivo utiliza CSS y JavaScript para mejorar la apariencia y la funcionalidad de la interfaz.

Integración con la base de datos
En el archivo app.py, se configuró la conexión a la base de datos magical_girls.db 
y se implementaron las rutas para registrar, actualizar, eliminar y visualizar la información de las chicas mágicas.

Ejecución de la aplicación
Finalmente, se ejecutó la aplicación utilizando el archivo app.py y se verificó su funcionamiento accediendo a la interfaz de usuario a través del navegador web.
