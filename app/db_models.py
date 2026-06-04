from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass


class CategoriaDB(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    descripcion = Column(String)
    activo = Column(Boolean, default=True)


class ProveedorDB(Base):
    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    telefono = Column(String)
    email = Column(String)
    activo = Column(Boolean, default=True)


class ProductoDB(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    precio = Column(Float)
    cantidad = Column(Integer)

    categoria_id = Column(Integer)
    proveedor_id = Column(Integer)

    activo = Column(Boolean, default=True)