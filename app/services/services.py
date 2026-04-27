import csv
import os
from app.models.models import Producto, Categoria, Proveedor

DATA_PATH = "app/data"

# =========================
# 🔹 UTILIDADES CSV
# =========================

def leer_csv(nombre_archivo):
    ruta = os.path.join(DATA_PATH, nombre_archivo)
    if not os.path.exists(ruta):
        return []
    with open(ruta, mode="r", newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def escribir_csv(nombre_archivo, datos, campos):
    ruta = os.path.join(DATA_PATH, nombre_archivo)
    with open(ruta, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(datos)

# =========================
# 🔹 PRODUCTOS
# =========================

CAMPOS_PRODUCTO = ["id", "nombre", "precio", "cantidad", "categoria_id", "proveedor_id", "activo"]

def obtener_productos():
    # Solo devolvemos los que están activos para la vista normal (opcional)
    # o todos para que el profesor vea el histórico.
    return leer_csv("productos.csv")

def crear_producto(producto: Producto):
    productos = leer_csv("productos.csv")
    nuevo_prod = producto.dict()
    # Si no tiene ID, le asignamos uno autoincremental
    if nuevo_prod['id'] is None:
        nuevo_prod['id'] = 1 if not productos else int(productos[-1]['id']) + 1
    
    productos.append(nuevo_prod)
    escribir_csv("productos.csv", productos, CAMPOS_PRODUCTO)
    return nuevo_prod

def eliminar_producto(id_producto: int):
    # PUNTO 5: Borrado Lógico (Histórico)
    productos = leer_csv("productos.csv")
    encontrado = False
    for p in productos:
        if int(p["id"]) == id_producto:
            p["activo"] = "False"  # Se mantiene en el CSV pero como inactivo
            encontrado = True
    
    escribir_csv("productos.csv", productos, CAMPOS_PRODUCTO)
    return {"mensaje": "Producto marcado como inactivo (histórico conservado)"} if encontrado else {"error": "No encontrado"}

# PUNTO 7: Búsqueda por atributo diferente al ID (Nombre)
def buscar_producto_por_nombre(nombre: str):
    productos = leer_csv("productos.csv")
    return [p for p in productos if nombre.lower() in p["nombre"].lower()]

# PUNTO 6: Filtrar por atributo (Categoría)
def filtrar_productos_por_categoria(id_cat: int):
    productos = leer_csv("productos.csv")
    return [p for p in productos if int(p["categoria_id"]) == id_cat]

# =========================
# 🔹 CATEGORÍAS
# =========================

CAMPOS_CATEGORIA = ["id", "nombre", "descripcion", "activo"]

def crear_categoria(categoria: Categoria):
    categorias = leer_csv("categorias.csv")
    nueva_cat = categoria.dict()
    categorias.append(nueva_cat)
    escribir_csv("categorias.csv", categorias, CAMPOS_CATEGORIA)
    return nueva_cat

def eliminar_categoria(id_categoria: int):
    categorias = leer_csv("categorias.csv")
    for c in categorias:
        if int(c["id"]) == id_categoria:
            c["activo"] = "False"
    escribir_csv("categorias.csv", categorias, CAMPOS_CATEGORIA)
    return {"mensaje": "Categoría desactivada"}

# =========================
# 🔹 PROVEEDORES
# =========================

CAMPOS_PROVEEDOR = ["id", "nombre", "telefono", "email", "activo"]

def crear_proveedor(proveedor: Proveedor):
    proveedores = leer_csv("proveedores.csv")
    nuevo_prov = proveedor.dict()
    proveedores.append(nuevo_prov)
    escribir_csv("proveedores.csv", proveedores, CAMPOS_PROVEEDOR)
    return nuevo_prov

def eliminar_proveedor(id_proveedor: int):
    proveedores = leer_csv("proveedores.csv")
    for p in proveedores:
        if int(p["id"]) == id_proveedor:
            p["activo"] = "False"
    escribir_csv("proveedores.csv", proveedores, CAMPOS_PROVEEDOR)
    return {"mensaje": "Proveedor desactivado"}