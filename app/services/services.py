from sqlalchemy.orm import Session
from app.db_models import ProductoDB, CategoriaDB, ProveedorDB
from app.models.models import Producto, Categoria, Proveedor


# =========================
# 🔹 PRODUCTOS
# =========================

def obtener_productos(db: Session):
    return db.query(ProductoDB).filter(ProductoDB.activo == True).all()


def crear_producto(db: Session, producto: Producto):
    nuevo = ProductoDB(
        nombre=producto.nombre,
        precio=producto.precio,
        cantidad=producto.cantidad,
        categoria_id=producto.categoria_id,
        proveedor_id=producto.proveedor_id,
        activo=True
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def actualizar_producto(db: Session, id_producto: int, producto: Producto):
    p = db.query(ProductoDB).filter(ProductoDB.id == id_producto).first()
    if not p:
        return {"error": "Producto no encontrado"}
    p.nombre = producto.nombre
    p.precio = producto.precio
    p.cantidad = producto.cantidad
    p.categoria_id = producto.categoria_id
    p.proveedor_id = producto.proveedor_id
    p.activo = producto.activo
    db.commit()
    return {"mensaje": "Producto actualizado"}


def eliminar_producto(db: Session, id_producto: int):
    p = db.query(ProductoDB).filter(ProductoDB.id == id_producto).first()
    if not p:
        return {"error": "Producto no encontrado"}
    p.activo = False
    db.commit()
    return {"mensaje": "Producto marcado como inactivo"}


def buscar_producto_por_nombre(db: Session, nombre: str):
    return db.query(ProductoDB).filter(
        ProductoDB.nombre.ilike(f"%{nombre}%"),
        ProductoDB.activo == True
    ).all()


def filtrar_productos_por_categoria(db: Session, id_cat: int):
    return db.query(ProductoDB).filter(
        ProductoDB.categoria_id == id_cat,
        ProductoDB.activo == True
    ).all()


# =========================
# 🔹 CATEGORÍAS
# =========================

def obtener_categorias(db: Session):
    return db.query(CategoriaDB).filter(CategoriaDB.activo == True).all()


def crear_categoria(db: Session, categoria: Categoria):
    nueva = CategoriaDB(
        nombre=categoria.nombre,
        descripcion=categoria.descripcion,
        activo=True
    )
    db.add(nueva)
    db.commit()
    db.refresh(nueva)
    return nueva


def actualizar_categoria(db: Session, id_categoria: int, categoria: Categoria):
    c = db.query(CategoriaDB).filter(CategoriaDB.id == id_categoria).first()
    if not c:
        return {"error": "Categoría no encontrada"}
    c.nombre = categoria.nombre
    c.descripcion = categoria.descripcion
    c.activo = categoria.activo
    db.commit()
    return {"mensaje": "Categoría actualizada"}


def eliminar_categoria(db: Session, id_categoria: int):
    c = db.query(CategoriaDB).filter(CategoriaDB.id == id_categoria).first()
    if not c:
        return {"error": "Categoría no encontrada"}
    c.activo = False
    db.commit()
    return {"mensaje": "Categoría desactivada"}


# =========================
# 🔹 PROVEEDORES
# =========================

def obtener_proveedores(db: Session):
    return db.query(ProveedorDB).filter(ProveedorDB.activo == True).all()


def crear_proveedor(db: Session, proveedor: Proveedor):
    nuevo = ProveedorDB(
        nombre=proveedor.nombre,
        telefono=proveedor.telefono,
        email=proveedor.email,
        activo=True
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


def actualizar_proveedor(db: Session, id_proveedor: int, proveedor: Proveedor):
    p = db.query(ProveedorDB).filter(ProveedorDB.id == id_proveedor).first()
    if not p:
        return {"error": "Proveedor no encontrado"}
    p.nombre = proveedor.nombre
    p.telefono = proveedor.telefono
    p.email = proveedor.email
    p.activo = proveedor.activo
    db.commit()
    return {"mensaje": "Proveedor actualizado"}


def eliminar_proveedor(db: Session, id_proveedor: int):
    p = db.query(ProveedorDB).filter(ProveedorDB.id == id_proveedor).first()
    if not p:
        return {"error": "Proveedor no encontrado"}
    p.activo = False
    db.commit()
    return {"mensaje": "Proveedor desactivado"}