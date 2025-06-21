from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from database import get_db

# Modelo de base de datos
from models.task import Task

# Schema de validacion de los datos que vienen del front-end
from schemas.task import TaskRead, TaskCreate, TaskUpdate



# Variable a la que le agregaremos todas las rutas de `tasks`
router = APIRouter(tags=['Tareas'])


# Endpoint para obtener todas las tareas
@router.get('/tasks')
def get_tasks(db: Session = Depends(get_db)) -> list[TaskRead]:
    tasks = db.query(Task).filter(Task.is_active == 1).all()
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


# Endpoind para actualizar tareas
@router.put('/tasks/update/{id}')
def update_task(id: int, task: TaskUpdate, db: Session = Depends(get_db)) -> dict:
    # Verificar si la tarea existe
    task_exist = db.query(Task).filter(Task.id == id).first()

    # Si la tarea no existe, enviar error de tarea no encontrada
    if not task_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={ 'message': 'Tarea no encontrada' }
        )
    
    # Si la tarea existe, actualizarla
    db.query(Task).filter(Task.id == id).update({
        Task.title: task.title,
        Task.description: task.description,
    })
    
    # Guardar cambios de la tarea en base de datos
    db.commit()

    return {
        'message': f'Tarea {task.title} actualizada con exito'
    }


# Endpoint para eliminar tareas
@router.delete('/tasks/delete/{id}')
def delete_task(id: int, db: Session = Depends(get_db)):
    # Verificar si la tarea existe
    task_exist = db.query(Task).filter(Task.id == id).first()

    # Si la tarea no existe, enviar error de tarea no encontrada
    if not task_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={ 'message': 'Tarea no encontrada' }
        )
    
    # Si la tarea existe, actualizarla
    db.query(Task).filter(Task.id == id).update({
        Task.is_active: 0,
    })
    
    # Guardar cambios de la tarea en base de datos
    db.commit()

    return {
        'message': f'Tarea {task_exist.title} eliminada con exito'
    }

