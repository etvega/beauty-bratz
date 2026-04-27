from pydantic import BaseModel
from typing import Optional


# 🔹 MODELO: Categoría
class Categoria(BaseModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None


# 🔹 MODELO: Proveedor
class Proveedor(BaseModel):
    id: int
    nombre: str
    telefono: str
    email: str


# 🔹 MODELO: Producto
class Producto(BaseModel):
    id: int
    nombre: str
    precio: float
    cantidad: int
    categoria_id: int
    proveedor_id: int