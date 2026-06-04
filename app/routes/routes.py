from fastapi import APIRouter, HTTPException
from app.models.models import Producto, Categoria, Proveedor
from app.services import services

router = APIRouter()

# --- PRODUCTOS ---
@router.get("/productos", tags=["Productos"])
def get_productos():
    return services.obtener_productos()

@router.post("/productos", tags=["Productos"])
def add_producto(producto: Producto):
    return services.crear_producto(producto)

@router.put("/productos/{id_producto}", tags=["Productos"])
def update_producto(id_producto: int, producto: Producto):
    resultado = services.actualizar_producto(id_producto, producto)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado

@router.delete("/productos/{id_producto}", tags=["Productos"])
def delete_producto(id_producto: int):
    resultado = services.eliminar_producto(id_producto)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado

@router.get("/productos/buscar/{nombre}", tags=["Productos"])
def get_producto_por_nombre(nombre: str):
    return services.buscar_producto_por_nombre(nombre)

@router.get("/productos/filtrar/categoria/{id_categoria}", tags=["Productos"])
def get_productos_por_categoria(id_categoria: int):
    return services.filtrar_productos_por_categoria(id_categoria)


# --- CATEGORÍAS ---
@router.get("/categorias", tags=["Categorías"])
def get_categorias():
    return services.obtener_categorias()

@router.post("/categorias", tags=["Categorías"])
def agregar_categoria(categoria: Categoria):
    return services.crear_categoria(categoria)

@router.put("/categorias/{id_categoria}", tags=["Categorías"])
def update_categoria(id_categoria: int, categoria: Categoria):
    resultado = services.actualizar_categoria(id_categoria, categoria)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado

@router.delete("/categorias/{id_categoria}", tags=["Categorías"])
def delete_categoria(id_categoria: int):
    resultado = services.eliminar_categoria(id_categoria)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado


# --- PROVEEDORES ---
@router.get("/proveedores", tags=["Proveedores"])
def get_proveedores():
    return services.obtener_proveedores()

@router.post("/proveedores", tags=["Proveedores"])
def add_proveedor(proveedor: Proveedor):
    return services.crear_proveedor(proveedor)

@router.put("/proveedores/{id_proveedor}", tags=["Proveedores"])
def update_proveedor(id_proveedor: int, proveedor: Proveedor):
    resultado = services.actualizar_proveedor(id_proveedor, proveedor)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado

@router.delete("/proveedores/{id_proveedor}", tags=["Proveedores"])
def delete_proveedor(id_proveedor: int):
    resultado = services.eliminar_proveedor(id_proveedor)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado