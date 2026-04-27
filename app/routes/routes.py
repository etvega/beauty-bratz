from fastapi import APIRouter
from app.models.models import Producto, Categoria, Proveedor
from app.services.services import (
    # Productos
    obtener_productos,
    crear_producto,
    eliminar_producto,

    # Categorías
    obtener_categorias,
    crear_categoria,
    eliminar_categoria,

    # Proveedores
    obtener_proveedores,
    crear_proveedor,
    eliminar_proveedor
)

router = APIRouter()


# =========================
# 🔹 PRODUCTOS
# =========================

@router.get("/productos")
def get_productos():
    return obtener_productos()


@router.post("/productos")
def add_producto(producto: Producto):
    return crear_producto(producto)


@router.delete("/productos/{id_producto}")
def delete_producto(id_producto: int):
    return eliminar_producto(id_producto)


# =========================
# 🔹 CATEGORÍAS
# =========================

@router.get("/categorias")
def get_categorias():
    return obtener_categorias()


@router.post("/categorias")
def add_categoria(categoria: Categoria):
    return crear_categoria(categoria)


@router.delete("/categorias/{id_categoria}")
def delete_categoria(id_categoria: int):
    return eliminar_categoria(id_categoria)


# =========================
# 🔹 PROVEEDORES
# =========================

@router.get("/proveedores")
def get_proveedores():
    return obtener_proveedores()


@router.post("/proveedores")
def add_proveedor(proveedor: Proveedor):
    return crear_proveedor(proveedor)


@router.delete("/proveedores/{id_proveedor}")
def delete_proveedor(id_proveedor: int):
    return eliminar_proveedor(id_proveedor)

@router.put("/productos/{id_producto}")
def update_producto(id_producto: int, producto: Producto):
    return actualizar_producto(id_producto, producto)