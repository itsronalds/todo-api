# Modelo base para crear esquemas que validen los datos que vienen del front-end
from pydantic import BaseModel, Field

from datetime import datetime
from typing import Optional


'''
id, title, description, created_at

1. GET TASKS
id (se autogenera)
title
description
created_at (se autogenera)

2. CREATE TASK
title
description

3. UPDATE TASK
title
description
'''


class TaskBase(BaseModel):
    # El titulo debe ser string y debe tener una rango de caracteres entre 3-75
    title: str = Field(min_length=3, max_length=75)

    # La descripcion es opcional, pero si llega a venir debe ser string
    description: Optional[str]


class TaskRead(TaskBase):
    # title y description ya me los trae porque esta heredando

    # Creamos los campos faltantes
    id: int
    created_at: datetime


class TaskCreate(TaskBase):
    '''
    Para crear una tarea necesitamos title, description, no necesitamos colocarlas 
    porque la estamos heredando de `TaskBase`
    '''
    pass
