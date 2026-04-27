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
# 🔹 PRODUCTOS CRUD
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