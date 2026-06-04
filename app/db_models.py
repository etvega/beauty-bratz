from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase):
    pass


class CategoriaDB(Base):
    _tablename_ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    activo = Column(Boolean, default=True)

    productos = relationship("ProductoDB", back_populates="categoria")


class ProveedorDB(Base):
    _tablename_ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String)
    email = Column(String)
    activo = Column(Boolean, default=True)

    productos = relationship("ProductoDB", back_populates="proveedor")


class ProductoDB(Base):
    _tablename_ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float)
    cantidad = Column(Integer)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    proveedor_id = Column(Integer, ForeignKey("proveedores.id"), nullable=False)
    activo = Column(Boolean, default=True)

    categoria = relationship("CategoriaDB", back_populates="productos")
    proveedor = relationship("ProveedorDB", back_populates="productos")