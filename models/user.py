# Importar librerias necesarias para crear nuestro modelo
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

# Importar clase base para crear nuestros modelos de base de datos
from database import Base


# Modelo para la tabla users
class User(Base):
    # Nombre de la tabla a la que pertenece el modelo
    __tablename__ = 'users'

    # Columnas de la tabla
    id = Column(Integer, primary_key=True)
    name = Column(String(75), nullable=False)
    email = Column(String(127), nullable=False)
    password = Column(String(127), nullable=False)
    created_at = Column(DateTime, server_default=func.now())
