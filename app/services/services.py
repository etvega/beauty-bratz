from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.db_models import ProductoDB, CategoriaDB, ProveedorDB
from app.models.models import Producto, Categoria, Proveedor


def get_db():
    db = SessionLocal()
    try:
        return db
    except Exception:
        db.close()
        raise


# =========================
# 🔹 PRODUCTOS
# =========================

def obtener_productos():
    db: Session = get_db()
    try:
        return db.query(ProductoDB).filter(ProductoDB.activo == True).all()
    finally:
        db.close()


def crear_producto(producto: Producto):
    db: Session = get_db()
    try:
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
    finally:
        db.close()


def actualizar_producto(id_producto: int, producto: Producto):
    db: Session = get_db()
    try:
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
    finally:
        db.close()


def eliminar_producto(id_producto: int):
    db: Session = get_db()
    try:
        p = db.query(ProductoDB).filter(ProductoDB.id == id_producto).first()
        if not p:
            return {"error": "Producto no encontrado"}
        p.activo = False
        db.commit()
        return {"mensaje": "Producto marcado como inactivo"}
    finally:
        db.close()


def buscar_producto_por_nombre(nombre: str):
    db: Session = get_db()
    try:
        return db.query(ProductoDB).filter(
            ProductoDB.nombre.ilike(f"%{nombre}%"),
            ProductoDB.activo == True
        ).all()
    finally:
        db.close()


def filtrar_productos_por_categoria(id_cat: int):
    db: Session = get_db()
    try:
        return db.query(ProductoDB).filter(
            ProductoDB.categoria_id == id_cat,
            ProductoDB.activo == True
        ).all()
    finally:
        db.close()


# =========================
# 🔹 CATEGORÍAS
# =========================

def obtener_categorias():
    db: Session = get_db()
    try:
        return db.query(CategoriaDB).filter(CategoriaDB.activo == True).all()
    finally:
        db.close()


def crear_categoria(categoria: Categoria):
    db: Session = get_db()
    try:
        nueva = CategoriaDB(
            nombre=categoria.nombre,
            descripcion=categoria.descripcion,
            activo=True
        )
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return nueva
    finally:
        db.close()


def actualizar_categoria(id_categoria: int, categoria: Categoria):
    db: Session = get_db()
    try:
        c = db.query(CategoriaDB).filter(CategoriaDB.id == id_categoria).first()
        if not c:
            return {"error": "Categoría no encontrada"}
        c.nombre = categoria.nombre
        c.descripcion = categoria.descripcion
        c.activo = categoria.activo
        db.commit()
        return {"mensaje": "Categoría actualizada"}
    finally:
        db.close()


def eliminar_categoria(id_categoria: int):
    db: Session = get_db()
    try:
        c = db.query(CategoriaDB).filter(CategoriaDB.id == id_categoria).first()
        if not c:
            return {"error": "Categoría no encontrada"}
        c.activo = False
        db.commit()
        return {"mensaje": "Categoría desactivada"}
    finally:
        db.close()


# =========================
# 🔹 PROVEEDORES
# =========================

def obtener_proveedores():
    db: Session = get_db()
    try:
        return db.query(ProveedorDB).filter(ProveedorDB.activo == True).all()
    finally:
        db.close()


def crear_proveedor(proveedor: Proveedor):
    db: Session = get_db()
    try:
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
    finally:
        db.close()


def actualizar_proveedor(id_proveedor: int, proveedor: Proveedor):
    db: Session = get_db()
    try:
        p = db.query(ProveedorDB).filter(ProveedorDB.id == id_proveedor).first()
        if not p:
            return {"error": "Proveedor no encontrado"}
        p.nombre = proveedor.nombre
        p.telefono = proveedor.telefono
        p.email = proveedor.email
        p.activo = proveedor.activo
        db.commit()
        return {"mensaje": "Proveedor actualizado"}
    finally:
        db.close()


def eliminar_proveedor(id_proveedor: int):
    db: Session = get_db()
    try:
        p = db.query(ProveedorDB).filter(ProveedorDB.id == id_proveedor).first()
        if not p:
            return {"error": "Proveedor no encontrado"}
        p.activo = False
        db.commit()
        return {"mensaje": "Proveedor desactivado"}
    finally:
        db.close()