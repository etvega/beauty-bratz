from fastapi import FastAPI
from app.routes.routes import router

app = FastAPI(
    title="Beauty Bratz",
    description="Sistema de gestión de productos, categorías y proveedores",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def inicio():
    return {
        "mensaje": "Bienvenido a Beauty Bratz"
    }