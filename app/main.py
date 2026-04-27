from fastapi import FastAPI
from app.routes.routes import router

# 🔹 Configuración avanzada de la aplicación
app = FastAPI(
    title="BEAUTY BRATZ – Sistema de Inventario",
    description="""
    ### 💅 API de Gestión de Inventario Profesional
    
    Este sistema permite administrar productos, categorías y proveedores con persistencia real.
    
    **Características principales:**
    * ✅ **CRUD Completo:** Gestión de todas las entidades.
    * ✅ **Persistencia:** Almacenamiento directo en archivos CSV (Sin SQL).
    * ✅ **Sistema de Histórico:** Borrado lógico mediante estados (Punto 5 del proyecto).
    * ✅ **Búsqueda y Filtros:** Endpoints específicos para localización de datos por atributos.
    """,
    version="1.1.0"
)

# 🔹 Conectar las rutas (Esto activa automáticamente el Mapa de Endpoints en /docs)
app.include_router(router)


# 🔹 Ruta principal de bienvenida
@app.get("/", tags=["Inicio"])
def home():
    return {
        "mensaje": "¡Bienvenida a la API de Beauty Bratz!",
        "estado": "Servidor en línea",
        "documentacion": "/docs",
        "desarrollado_por": "Erika Tatiana Vega Joya"
    }