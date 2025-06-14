from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from database import get_db

# Modelo de base de datos
from models.task import Task

# Schema de validacion de los datos que vienen del front-end
from schemas.task import TaskRead, TaskCreate



# Variable a la que le agregaremos todas las rutas de `tasks`
router = APIRouter()


# Endpoint para obtener todas las tareas
@router.get('/tasks')
def get_tasks(db: Session = Depends(get_db)) -> list[TaskRead]:
    tasks = db.query(Task).all()
    return tasks


# Endpoint para crear tareas
@router.post('/tasks/create')
def create_task(task: TaskCreate, db: Session = Depends(get_db)) -> TaskRead:
    # Crear tarea a registrar en base de datos
    new_task = Task(
        title=task.title,
        description=task.description,
    )

    # Registrar nueva tarea en base de datos
    db.add(new_task)

    # Guardar nueva tarea en la tabla
    db.commit()

    # El id y created_at generado se le agregaran a la variable new_task
    db.refresh(new_task)

    return new_task
