# Importamos FastAPI
from fastapi import FastAPI

from routes.task import router as tasks_router

# Variable que contendra nuestra aplicacion de FastAPI
app = FastAPI()

# Informacion para nuestra aplicacion
app.title = 'ToDo API'
app.description = 'REST API for ToDo App'
app.version = '1.0.0'

# Incluir rutas de tareas a nuestra app
app.include_router(tasks_router)
