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

def obtener_productos():
    return leer_csv("productos.csv")


def crear_producto(producto: Producto):
    productos = leer_csv("productos.csv")

    productos.append(producto.dict())

    campos = ["id", "nombre", "precio", "cantidad", "categoria_id", "proveedor_id"]
    escribir_csv("productos.csv", productos, campos)

    return producto


def eliminar_producto(id_producto: int):
    productos = leer_csv("productos.csv")

    productos = [p for p in productos if int(p["id"]) != id_producto]

    campos = ["id", "nombre", "precio", "cantidad", "categoria_id", "proveedor_id"]
    escribir_csv("productos.csv", productos, campos)

    return {"mensaje": "Producto eliminado"}


# =========================
# 🔹 CATEGORÍAS
# =========================

def obtener_categorias():
    return leer_csv("categorias.csv")


def crear_categoria(categoria: Categoria):
    categorias = leer_csv("categorias.csv")

    categorias.append(categoria.dict())

    campos = ["id", "nombre", "descripcion"]
    escribir_csv("categorias.csv", categorias, campos)

    return categoria


def eliminar_categoria(id_categoria: int):
    categorias = leer_csv("categorias.csv")

    categorias = [c for c in categorias if int(c["id"]) != id_categoria]

    campos = ["id", "nombre", "descripcion"]
    escribir_csv("categorias.csv", categorias, campos)

    return {"mensaje": "Categoria eliminada"}


# =========================
# 🔹 PROVEEDORES
# =========================

def obtener_proveedores():
    return leer_csv("proveedores.csv")


def crear_proveedor(proveedor: Proveedor):
    proveedores = leer_csv("proveedores.csv")

    proveedores.append(proveedor.dict())

    campos = ["id", "nombre", "telefono", "email"]
    escribir_csv("proveedores.csv", proveedores, campos)

    return proveedor


def eliminar_proveedor(id_proveedor: int):
    proveedores = leer_csv("proveedores.csv")

    proveedores = [p for p in proveedores if int(p["id"]) != id_proveedor]

    campos = ["id", "nombre", "telefono", "email"]
    escribir_csv("proveedores.csv", proveedores, campos)

    return {"mensaje": "Proveedor eliminado"}