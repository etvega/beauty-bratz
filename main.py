from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from app.routes.routes import router
from app.database import engine

# Importar TODOS los modelos para que SQLAlchemy los registre
from app.db_models import Base, CategoriaDB, ProveedorDB, ProductoDB

import os

# Crear tablas solo si existe conexión a PostgreSQL
if engine:
    Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Beauty Bratz",
    version="1.0"
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar rutas
app.include_router(router)

# Templates HTML
templates = Jinja2Templates(
    directory="app/models/templates"
)

# Página principal
@app.get("/")
def inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

# Ejecutar aplicación
if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port
    )