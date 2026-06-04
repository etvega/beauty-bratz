from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.models import Producto, Categoria, Proveedor
from app.database import get_db
from app.services import services

router = APIRouter()


# --- PRODUCTOS ---
@router.get("/productos", tags=["Productos"])
def get_productos(db: Session = Depends(get_db)):
    return services.obtener_productos(db)


@router.post("/productos", tags=["Productos"])
def add_producto(producto: Producto, db: Session = Depends(get_db)):
    return services.crear_producto(db, producto)


@router.put("/productos/{id_producto}", tags=["Productos"])
def update_producto(id_producto: int, producto: Producto, db: Session = Depends(get_db)):
    resultado = services.actualizar_producto(db, id_producto, producto)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado


@router.delete("/productos/{id_producto}", tags=["Productos"])
def delete_producto(id_producto: int, db: Session = Depends(get_db)):
    resultado = services.eliminar_producto(db, id_producto)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado


@router.get("/productos/buscar/{nombre}", tags=["Productos"])
def get_producto_por_nombre(nombre: str, db: Session = Depends(get_db)):
    return services.buscar_producto_por_nombre(db, nombre)


@router.get("/productos/filtrar/categoria/{id_categoria}", tags=["Productos"])
def get_productos_por_categoria(id_categoria: int, db: Session = Depends(get_db)):
    return services.filtrar_productos_por_categoria(db, id_categoria)


# --- CATEGORÍAS ---
@router.get("/categorias", tags=["Categorías"])
def get_categorias(db: Session = Depends(get_db)):
    return services.obtener_categorias(db)


@router.post("/categorias", tags=["Categorías"])
def agregar_categoria(categoria: Categoria, db: Session = Depends(get_db)):
    return services.crear_categoria(db, categoria)


@router.put("/categorias/{id_categoria}", tags=["Categorías"])
def update_categoria(id_categoria: int, categoria: Categoria, db: Session = Depends(get_db)):
    resultado = services.actualizar_categoria(db, id_categoria, categoria)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado


@router.delete("/categorias/{id_categoria}", tags=["Categorías"])
def delete_categoria(id_categoria: int, db: Session = Depends(get_db)):
    resultado = services.eliminar_categoria(db, id_categoria)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado


# --- PROVEEDORES ---
@router.get("/proveedores", tags=["Proveedores"])
def get_proveedores(db: Session = Depends(get_db)):
    return services.obtener_proveedores(db)


@router.post("/proveedores", tags=["Proveedores"])
def add_proveedor(proveedor: Proveedor, db: Session = Depends(get_db)):
    return services.crear_proveedor(db, proveedor)


@router.put("/proveedores/{id_proveedor}", tags=["Proveedores"])
def update_proveedor(id_proveedor: int, proveedor: Proveedor, db: Session = Depends(get_db)):
    resultado = services.actualizar_proveedor(db, id_proveedor, proveedor)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado


@router.delete("/proveedores/{id_proveedor}", tags=["Proveedores"])
def delete_proveedor(id_proveedor: int, db: Session = Depends(get_db)):
    resultado = services.eliminar_proveedor(db, id_proveedor)
    if "error" in resultado:
        raise HTTPException(status_code=404, detail=resultado["error"])
    return resultado