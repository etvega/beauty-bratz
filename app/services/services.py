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

CAMPOS_PRODUCTO = [
    "id",
    "nombre",
    "precio",
    "cantidad",
    "categoria_id",
    "proveedor_id",
    "activo"
]


def obtener_productos():
    return leer_csv("productos.csv")


def crear_producto(producto: Producto):
    productos = leer_csv("productos.csv")

    nuevo_prod = producto.dict()

    if nuevo_prod["id"] is None:
        nuevo_prod["id"] = 1 if not productos else int(productos[-1]["id"]) + 1

    productos.append(nuevo_prod)

    escribir_csv(
        "productos.csv",
        productos,
        CAMPOS_PRODUCTO
    )

    return nuevo_prod


def actualizar_producto(id_producto: int, producto: Producto):
    productos = leer_csv("productos.csv")

    for p in productos:
        if int(p["id"]) == id_producto:
            p["nombre"] = producto.nombre
            p["precio"] = producto.precio
            p["cantidad"] = producto.cantidad
            p["categoria_id"] = producto.categoria_id
            p["proveedor_id"] = producto.proveedor_id
            p["activo"] = producto.activo

            escribir_csv(
                "productos.csv",
                productos,
                CAMPOS_PRODUCTO
            )

            return {"mensaje": "Producto actualizado"}

    return {"error": "Producto no encontrado"}


def eliminar_producto(id_producto: int):
    productos = leer_csv("productos.csv")

    for p in productos:
        if int(p["id"]) == id_producto:
            p["activo"] = "False"

            escribir_csv(
                "productos.csv",
                productos,
                CAMPOS_PRODUCTO
            )

            return {"mensaje": "Producto marcado como inactivo"}

    return {"error": "Producto no encontrado"}


def buscar_producto_por_nombre(nombre: str):
    productos = leer_csv("productos.csv")

    return [
        p
        for p in productos
        if nombre.lower() in p["nombre"].lower()
    ]


def filtrar_productos_por_categoria(id_cat: int):
    productos = leer_csv("productos.csv")

    return [
        p
        for p in productos
        if int(p["categoria_id"]) == id_cat
    ]


# =========================
# 🔹 CATEGORÍAS
# =========================

CAMPOS_CATEGORIA = [
    "id",
    "nombre",
    "descripcion",
    "activo"
]


def obtener_categorias():
    return leer_csv("categorias.csv")


def crear_categoria(categoria: Categoria):
    categorias = leer_csv("categorias.csv")

    nueva_cat = categoria.dict()

    if nueva_cat["id"] is None:
        nueva_cat["id"] = (
            1 if not categorias
            else int(categorias[-1]["id"]) + 1
        )

    categorias.append(nueva_cat)

    escribir_csv(
        "categorias.csv",
        categorias,
        CAMPOS_CATEGORIA
    )

    return nueva_cat


def actualizar_categoria(id_categoria: int, categoria: Categoria):
    categorias = leer_csv("categorias.csv")

    for c in categorias:
        if int(c["id"]) == id_categoria:
            c["nombre"] = categoria.nombre
            c["descripcion"] = categoria.descripcion
            c["activo"] = categoria.activo

            escribir_csv(
                "categorias.csv",
                categorias,
                CAMPOS_CATEGORIA
            )

            return {"mensaje": "Categoría actualizada"}

    return {"error": "Categoría no encontrada"}


def eliminar_categoria(id_categoria: int):
    categorias = leer_csv("categorias.csv")

    for c in categorias:
        if int(c["id"]) == id_categoria:
            c["activo"] = "False"

            escribir_csv(
                "categorias.csv",
                categorias,
                CAMPOS_CATEGORIA
            )

            return {"mensaje": "Categoría desactivada"}

    return {"error": "Categoría no encontrada"}


# =========================
# 🔹 PROVEEDORES
# =========================

CAMPOS_PROVEEDOR = [
    "id",
    "nombre",
    "telefono",
    "email",
    "activo"
]


def obtener_proveedores():
    return leer_csv("proveedores.csv")


def crear_proveedor(proveedor: Proveedor):
    proveedores = leer_csv("proveedores.csv")

    nuevo_prov = proveedor.dict()

    if nuevo_prov["id"] is None:
        nuevo_prov["id"] = (
            1 if not proveedores
            else int(proveedores[-1]["id"]) + 1
        )

    proveedores.append(nuevo_prov)

    escribir_csv(
        "proveedores.csv",
        proveedores,
        CAMPOS_PROVEEDOR
    )

    return nuevo_prov


def actualizar_proveedor(id_proveedor: int, proveedor: Proveedor):
    proveedores = leer_csv("proveedores.csv")

    for p in proveedores:
        if int(p["id"]) == id_proveedor:
            p["nombre"] = proveedor.nombre
            p["telefono"] = proveedor.telefono
            p["email"] = proveedor.email
            p["activo"] = proveedor.activo

            escribir_csv(
                "proveedores.csv",
                proveedores,
                CAMPOS_PROVEEDOR
            )

            return {"mensaje": "Proveedor actualizado"}

    return {"error": "Proveedor no encontrado"}


def eliminar_proveedor(id_proveedor: int):
    proveedores = leer_csv("proveedores.csv")

    for p in proveedores:
        if int(p["id"]) == id_proveedor:
            p["activo"] = "False"

            escribir_csv(
                "proveedores.csv",
                proveedores,
                CAMPOS_PROVEEDOR
            )

            return {"mensaje": "Proveedor desactivado"}

    return {"error": "Proveedor no encontrado"}