from pydantic import BaseModel, Field, field_validator
from typing import Optional
import re


# 🔹 MODELO: Categoría
class Categoria(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(min_length=2, max_length=100)
    descripcion: Optional[str] = Field(default=None, max_length=200)
    activo: bool = True

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v):
        if not v.strip():
            raise ValueError("El nombre no puede estar vacío")
        return v.strip()


# 🔹 MODELO: Proveedor
class Proveedor(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(min_length=2, max_length=100)
    telefono: str = Field(min_length=7, max_length=15)
    email: str = Field(max_length=100)
    activo: bool = True

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v):
        if not v.strip():
            raise ValueError("El nombre no puede estar vacío")
        return v.strip()

    @field_validator("email")
    @classmethod
    def email_valido(cls, v):
        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", v):
            raise ValueError("El email no tiene un formato válido")
        return v.lower().strip()

    @field_validator("telefono")
    @classmethod
    def telefono_valido(cls, v):
        if not re.match(r"^[\d\+\-\s]{7,15}$", v):
            raise ValueError("El teléfono solo puede contener números, +, - y espacios")
        return v.strip()


# 🔹 MODELO: Producto
class Producto(BaseModel):
    id: Optional[int] = None
    nombre: str = Field(min_length=2, max_length=100)
    precio: float = Field(gt=0)
    cantidad: int = Field(ge=0)
    categoria_id: int = Field(gt=0)
    proveedor_id: int = Field(gt=0)
    activo: bool = True

    @field_validator("nombre")
    @classmethod
    def nombre_no_vacio(cls, v):
        if not v.strip():
            raise ValueError("El nombre no puede estar vacío")
        return v.strip()

    @field_validator("precio")
    @classmethod
    def precio_positivo(cls, v):
        if v <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        return round(v, 2)