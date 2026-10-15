from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.articulos import articulos_routers
from routers.proveedores import proveedores_routers
from routers.saludar import saludar_routers

# IMPORTANTE:
# Antes acá llamábamos a Base.metadata.create_all(bind=engine) para crear las
# tablas al arrancar la app. Ahora que usamos Alembic, las tablas se crean y
# versionan con migraciones (correr "alembic upgrade head"), no en el arranque
# de la aplicación.


app = FastAPI()

app.title = "Mi primera API"  # Así cambia el nombre en /docs

# Incluimos los routers (path operations)
app.include_router(articulos_routers, tags=["Artículos"], prefix="/articulos")
app.include_router(proveedores_routers, tags=["Proveedores"], prefix="/proveedores")
app.include_router(saludar_routers, tags=["Saludos"])

# ^ Tags agrupa en la documentación
# ^ Prefix le pone prefijos a las urls de cada path operation definido en ese router


# Request -> Middleware -> Path Operation -> Middleware -> Response
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",  # entorno desarrollo
        "https://faculemo.github.io/front",  # entorno producción
        # "*", wildcard ! Cualquier origen
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
