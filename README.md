# ToDo API

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)

---

## Descripción

**ToDo API** es una API RESTful desarrollada con **FastAPI** que permite gestionar tareas de manera sencilla y eficiente. Su objetivo principal es proporcionar un backend robusto para aplicaciones de listas de tareas (to-do lists), permitiendo operaciones de creación, consulta y gestión de tareas mediante peticiones HTTP.

## Características

- Crear tareas con título y descripción.
- Consultar todas las tareas creadas.
- Almacenar las tareas en una base de datos PostgreSQL.
- Validación de datos usando Pydantic.
- Arquitectura modular para facilitar la escalabilidad y el mantenimiento.

## Alembic

1. **Instalar Alembic**

   ```bash
   pip install alembic
   ```

2. **Inicializar Alembic**

   ```bash
   alembic init
   ```

   Ahora, debemos modificar el archivo `alembic/env.py` y agregarle la URL de nuestra conexión de base de datos. [Puedes leer más en este enlace](https://www.nashruddinamin.com/blog/how-to-use-alembic-for-database-migrations-in-your-fastapi-application)

2. **Nuestro primer Revision: Generar tablas**

   - Generar registro de cambio
   ```bash
   alembic revision --autogenerate -m "Nombre del cambio"
   ```

   - Aplicar cambios
   ```bash
   alembic upgrade head
   ```

## Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/itsronalds/todo-api.git
   cd todo-api
   ```

2. **Crea un entorno virtual e instala las dependencias:**

   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Unix/Mac:
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configura la base de datos PostgreSQL:**
   - Crea una base de datos (por ejemplo, `todo_db`).
   - Configura las variables de entorno o el archivo `.env` con tus credenciales de conexión.

4. **Ejecuta las migraciones con Alembic:**

   ```bash
   alembic upgrade head
   ```

5. **Inicia la aplicación:**

   ```bash
   uvicorn app:app --reload
   ```

6. **Accede a la documentación interactiva:**
   - [Swagger UI](http://localhost:8000/docs)

---

## Uso Básico de la API

### Crear una tarea

```bash
curl -X POST "http://localhost:8000/tasks/create" -H "Content-Type: application/json" -d '{"title": "Comprar leche", "description": "Ir al supermercado"}'
```

### Obtener todas las tareas

```bash
curl -X GET "http://localhost:8000/tasks"
```

---

## Migraciones con Alembic

1. **Instalar Alembic**

   ```bash
   pip install alembic
   ```

2. **Generar una nueva migración:**

   ```bash
   alembic revision --autogenerate -m "Descripción del cambio"
   ```

3. **Aplicar migraciones:**

   ```bash
   alembic upgrade head
   ```

---

## Tecnologías y Herramientas

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [PostgreSQL](https://www.postgresql.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)
- [Psycopg2](https://pypi.org/project/psycopg2/)
- [JSON Web Token](https://pypi.org/project/jsonwebtoken/)