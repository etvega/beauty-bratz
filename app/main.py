from fastapi import FastAPI
from app.routes.routes import router

# 🔹 Crear la aplicación
app = FastAPI(
    title="Beauty Bratz API",
    description="Sistema de inventario para productos, categorias y proveedores",
    version="1.0.0"
)

# 🔹 Conectar las rutas
app.include_router(router)


# 🔹 Ruta principal
@app.get("/")
def home():
    return {
        "mensaje": "¡Bienvenida a la API de Beauty Bratz!",
        "documentacion": "/docs"
    }