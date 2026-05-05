from fastapi import APIRouter, HTTPException
from app.models.models import Producto, Categoria, Proveedor
from app.services import services  # Importamos el módulo completo para evitar errores

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
    return services.actualizar_producto(id_producto, producto)

@router.delete("/productos/{id_producto}", tags=["Productos"])
def delete_producto(id_producto: int):
    return services.eliminar_producto(id_producto)

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
def Agregar_categoria(categoria: Categoria):
    return services.crear_categoria(categoria)

@router.delete("/categorias/{id_categoria}", tags=["Categorías"])
def delete_categoria(id_categoria: int):
    return services.eliminar_categoria(id_categoria)

# --- PROVEEDORES ---
@router.get("/proveedores", tags=["Proveedores"])
def get_proveedores():
    return services.obtener_proveedores()

@router.post("/proveedores", tags=["Proveedores"])
def add_provider(proveedor: Proveedor):
    return services.crear_proveedor(proveedor)

@router.delete("/proveedores/{id_proveedor}", tags=["Proveedores"])
def delete_provider(id_proveedor: int):
    return services.eliminar_proveedor(id_proveedor)