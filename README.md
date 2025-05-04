# Proyecto-Final-1r-DAM

## Elemental Esplay

### Autores:
- Jeremías, Alex, Alejandro, Brooklyn, Andrés

Este es un proyecto de entrega de final de curso para la evaluación de múltiples asignaturas como Programación, Entornos de Desarrollo y Sistemas de Información. El proyecto consiste en un Club D'Esplai orientado a los elementos de la naturaleza: agua, fuego, tierra y aire. Cada uno representa un tipo diferente de actividades.

### Tipos de actividades:
- **Fuego**: Actividades de aventura, como escalada, senderismo, etc.
- **Agua**: Actividades acuáticas, como kayak, surf, etc.
- **Tierra**: Actividades de campo, como senderismo, acampada, etc.
- **Aire**: Actividades al aire libre, como ciclismo, escalada, etc.

---

### Requisitos técnicos:
- Python 3.8 o superior
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Session

---

### Instalación:
1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/JeremiasCortes/Proyecto-Final-1r-DAM.git
   cd Proyecto-Final-1r-DAM
   ```

2. **Crear un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```   
   (Lo siento porque sea tan largo)


4. **Configurar la base de datos SQLite:**
   Ejecutar el siguiente comando para crear las tablas necesarias:
   ```bash
   python -c "from main import db; db.create_all()"
   ```

---

### Ejecución:
Para iniciar la aplicación, utiliza el siguiente comando:
```bash
flask run
```
Esto iniciará el servidor de desarrollo de Flask. Accede a la aplicación en `http://localhost:5000`.

---

### Estructura del proyecto:
- **main.py**: Archivo principal que contiene las rutas y la lógica de la aplicación.
- **templates/**: Contiene las plantillas HTML para las vistas.
- **static/**: Archivos estáticos como CSS, imágenes y JavaScript.
- **ElementalEsplay.db**: Base de datos SQLite que almacena usuarios, actividades e inscripciones.
- **requirements.txt**: Lista de dependencias del proyecto.
- **Adicional**: Aquí hay contenido adicional de la entrega, por ejemplos los diagramas
---

### Funcionalidades principales:
1. **Gestión de actividades**:
   - Crear nuevas actividades.
   - Inscribirse en actividades (con control de cupos).
   - Visualizar las actividades.

2. **Gestión de usuarios**:
   - Registro y login de usuarios.
   - Validación de credenciales.

3. **Interfaz amigable**:
   - Diseño responsivo utilizando TailwindCSS.

---

### Sin completar:
- Falta la parte de administración
  - De Usuarios
  - De Actividades
  - De Inscripciones
- Muchos endpoints y lógica no funcionan**
- Hay cosas usando CSS y no Tailwind**
- No hay pruebas unitarias
- No es Responsive todo
- No está bien estructurado, mucho uso de IA
- Enlaces a imágenes y archivos no están bien

### Adicional:
- El calendario
  - Se encuentra en /calendario

### Créditos:
Este proyecto fue desarrollado como parte del curso de DAM (Desarrollo de Aplicaciones Multiplataforma) por el equipo de Jeremías, Alex, Alejandro, Brooklyn y Andrés.
