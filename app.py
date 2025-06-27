# Importamos FastAPI
from fastapi import FastAPI

# Importar modelo base y motor de base de datos
from database import Base, engine

# Importar rutas de nuestra app
from routes.task import router as tasks_router
from routes.user import router as users_router

# Crear tablas en base a los modelos de forma automatica
# Base.metadata.create_all(engine)

# Variable que contendra nuestra aplicacion de FastAPI
app = FastAPI()

# Informacion para nuestra aplicacion
app.title = 'ToDo API'
app.description = 'REST API for ToDo App'
app.version = '1.0.0'

# Incluir las rutas de nuestra app
app.include_router(tasks_router)
app.include_router(users_router)
