# Importar librerias necesarias para establecer conexion FastAPI + PostgreSQL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Importar libreria de conexion python + postgres
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Configuracion de la aplicacion
from config import config

# String que conecta SQLAlchemy con PostgreSQL
DATABASE_URL = f'postgresql+psycopg2://{config['DB_USER']}:{config['DB_PASSWORD']}@{config['DB_HOST']}/{config['DB_NAME']}'

print(config['DB_USER'], config['DB_PASSWORD'], config['DB_HOST'], config['DB_NAME'])

engine = None

# Crear motor de conexion de PostgreSQL, si la base de datos no existe, creala
try:
    engine = create_engine(DATABASE_URL)
except:
    # Si no existe la db, creala
    connection = psycopg2.connect(user='postgres', password='1234', database='postgres')

    connection = psycopg2.connect('dbname=postgres user=postgres password=1234')
    connection.set_client_encoding('UTF8')
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    # Crear base de datos desde comando
    cursor.execute(u'CREATE DATABASE todo_db')

    # Cerrar conexiones
    cursor.close()
    connection.close()

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
