from pydantic import BaseModel, Field
from typing import Optional

# 🔹 MODELO: Categoría
class Categoria(BaseModel):
    id: Optional[int] = None
    nombre: str
    descripcion: Optional[str] = None
    activo: bool = True  # <--- REQUISITO PUNTO 5: Para el histórico

# 🔹 MODELO: Proveedor
class Proveedor(BaseModel):
    id: Optional[int] = None
    nombre: str
    telefono: str
    email: str
    activo: bool = True  # <--- REQUISITO PUNTO 5: Para el histórico

# 🔹 MODELO: Producto
class Producto(BaseModel):
    id: Optional[int] = None
    nombre: str
    precio: float
    cantidad: int
    categoria_id: int
    proveedor_id: int
    activo: bool = True  # <--- REQUISITO PUNTO 5: Para el histórico