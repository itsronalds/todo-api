# Importar librerias necesarias para establecer conexion FastAPI + PostgreSQL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# String que conecta SQLAlchemy con PostgreSQL
DATABASE_URL = 'postgresql+psycopg2://postgres:1234@localhost/todo_db'

# Crear motor de conexion de PostgreSQL
engine = create_engine(DATABASE_URL)

# Crear tienda de sesiones de conexion con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Clase base para todos nuestros modelos (tablas) de base de datos 
Base = declarative_base()


# Funcion que retorna una instancia de conexion con la base de datos
def get_db():
    db = SessionLocal()
    try:
        # Generamos una sesion de conexion con base de datos
        yield db
    finally:
        # Cerramos la conexion con bases de datos para liberar memoria
        db.close()