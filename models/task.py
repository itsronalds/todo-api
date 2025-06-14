# Importar librerias necesarias para crear nuestro modelo
from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

# Importar clase base para crear nuestros modelos de base de datos
from database import Base


# Modelo para la tabla task
class Task(Base):
    # Nombre de la tabla a la que pertenece el modelo
    __tablename__ = 'tasks'

    # Columnas de la tabla
    id = Column(Integer, primary_key=True)
    title = Column(String(75), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
