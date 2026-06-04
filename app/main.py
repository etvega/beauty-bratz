from pydantic import BaseModel, Field, EmailStr
from typing import Optional

# 🔹 MODELO: Categoría
class Categoria(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(
        min_length=3,
        max_length=100,
        description="Nombre de la categoría"
    )
    descripcion: Optional[str] = Field(
        default=None,
        max_length=255
    )
    activo: bool = True


# 🔹 MODELO: Proveedor
class Proveedor(BaseModel):
    id: Optional[int] = None

    nombre: str = Field(
        min_length=3,
        max_length=100
    )

    telefono: str = Field(
        min_length=7,
        max_length=15
    )

    email: EmailStr

    activo: bool = True


# 🔹 MODELO: Producto
class Producto(BaseModel):
    id: Optional[int] = None

    nombre: str = Field(
        min_length=3,
        max_length=150
    )

    precio: float = Field(
        gt=0,
        description="El precio debe ser mayor a cero"
    )

    cantidad: int = Field(
        ge=0,
        description="La cantidad no puede ser negativa"
    )

    categoria_id: int = Field(
        gt=0,
        description="Debe existir una categoría válida"
    )

    proveedor_id: int = Field(
        gt=0,
        description="Debe existir un proveedor válido"
    )

    activo: bool = True