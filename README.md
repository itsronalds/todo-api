# ToDo API

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

## Descripción

**ToDo API** es una API RESTful desarrollada con **FastAPI** que permite gestionar tareas de manera sencilla y eficiente. Su objetivo principal es proporcionar un backend robusto para aplicaciones de listas de tareas (to-do lists), permitiendo operaciones de creación, consulta y gestión de tareas mediante peticiones HTTP.

## Características

- Crear tareas con título y descripción.
- Consultar todas las tareas creadas.
- Almacenar las tareas en una base de datos PostgreSQL.
- Validación de datos usando Pydantic.
- Arquitectura modular para facilitar la escalabilidad y el mantenimiento.

## Endpoints Principales

- `GET /tasks`: Obtiene la lista de todas las tareas.
- `POST /tasks/create`: Crea una nueva tarea.

## Estructura de la Base de Datos

La API utiliza SQLAlchemy para definir el modelo `Task`:

| Campo       | Tipo      | Descripción                             |
|-------------|-----------|-----------------------------------------|
| id          | Integer   | Identificador único (autogenerado)      |
| title       | String    | Título de la tarea                      |
| description | Text      | Descripción de la tarea (opcional)      |
| created_at  | DateTime  | Fecha y hora de creación (autogenerada) |

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/itsronalds/todo-api.git
   cd todo-api
   ```

2. **Crea un entorno virtual e instala las dependencias:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Configura la base de datos PostgreSQL:**

   - Crea una base de datos llamada `todo_db`.
   - Modifica la URL de conexión en `database/__init__.py` si es necesario:
     ```
     DATABASE_URL = 'postgresql+psycopg2://postgres:1234@localhost/todo_db'
     ```

4. **Ejecuta las migraciones (si corresponde) o crea las tablas:**

   ```python
   # En consola interactiva de Python
   from database import Base, engine
   Base.metadata.create_all(bind=engine)
   ```

5. **Inicia la aplicación:**

   ```bash
   uvicorn app:app --reload
   ```

6. **Accede a la documentación interactiva:**
   - [Swagger UI](http://localhost:8000/docs)
   - [ReDoc](http://localhost:8000/redoc)

## Ejemplo de Uso

### Crear una tarea

```bash
curl -X POST "http://localhost:8000/tasks/create" -H "Content-Type: application/json" -d '{"title": "Comprar leche", "description": "Ir al supermercado"}'
```

### Obtener todas las tareas

```bash
curl -X GET "http://localhost:8000/tasks"
```

## Tecnologías Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [PostgreSQL](https://www.postgresql.org/)
- [Uvicorn](https://www.uvicorn.org/)
