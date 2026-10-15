# Database.py
# Gestión de la conexión a la DB -> Ahora usando SQLModel (reemplaza a SQLAlchemy puro)
#
# IMPORTANTE: las tablas ya NO se crean con metadata.create_all() en el arranque
# de la app. Ahora las creamos y versionamos con Alembic (ver carpeta /alembic).

from sqlmodel import Session, create_engine

url = "sqlite:///./base_de_datos.db"  # Sqlite: DB LOCAL (no en un servidor/nube)

# Fastapi es asíncrono, entonces le hace falta args especiales (check_same_thread)
# Motor de conexión -> Prepara internamente la DB
engine = create_engine(url, connect_args={"check_same_thread": False})


# Dependencia a introducir en los Path Operations
def get_db():
    with Session(engine) as session:
        yield session  # Return que no termina la función
