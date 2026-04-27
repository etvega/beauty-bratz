import csv
import os

# Definimos la ruta de la carpeta data
DATA_PATH = "app/data"

def resetear_datos():
    # Asegurar que la carpeta existe
    if not os.path.exists(DATA_PATH):
        os.makedirs(DATA_PATH)

    # 🔹 PRODUCTOS (10 registros para mostrar variedad)
    productos = [
        {"id": 1, "nombre": "Labial Mate Bratz Rojo", "precio": 25.5, "cantidad": 50, "categoria_id": 1, "proveedor_id": 1, "activo": True},
        {"id": 2, "nombre": "Serum Facial Vitamina C", "precio": 45.0, "cantidad": 20, "categoria_id": 2, "proveedor_id": 2, "activo": True},
        {"id": 3, "nombre": "Esponja Beauty Blender", "precio": 12.0, "cantidad": 100, "categoria_id": 3, "proveedor_id": 3, "activo": True},
        {"id": 4, "nombre": "Base Full Coverage", "precio": 35.9, "cantidad": 15, "categoria_id": 1, "proveedor_id": 1, "activo": True},
        {"id": 5, "nombre": "Paleta 'Pink Dreams'", "precio": 55.0, "cantidad": 10, "categoria_id": 1, "proveedor_id": 4, "activo": True},
        {"id": 6, "nombre": "Crema Ácido Hialurónico", "precio": 38.0, "cantidad": 25, "categoria_id": 2, "proveedor_id": 2, "activo": True},
        {"id": 7, "nombre": "Kit de Brochas Pro", "precio": 65.0, "cantidad": 8, "categoria_id": 3, "proveedor_id": 5, "activo": True},
        {"id": 8, "nombre": "Delineador Waterproof", "precio": 18.5, "cantidad": 40, "categoria_id": 1, "proveedor_id": 1, "activo": True},
        {"id": 9, "nombre": "Mascarilla Nocturna", "precio": 22.0, "cantidad": 30, "categoria_id": 2, "proveedor_id": 2, "activo": True},
        {"id": 10, "nombre": "Espejo LED Aumento", "precio": 42.0, "cantidad": 12, "categoria_id": 3, "proveedor_id": 5, "activo": True},
    ]
    
    # 🔹 CATEGORÍAS (5 registros)
    categorias = [
        {"id": 1, "nombre": "Rostro", "descripcion": "Bases y polvos", "activo": True},
        {"id": 2, "nombre": "Cuidado Facial", "descripcion": "Serums y cremas", "activo": True},
        {"id": 3, "nombre": "Accesorios", "descripcion": "Brochas y herramientas", "activo": True},
        {"id": 4, "nombre": "Labios", "descripcion": "Labiales", "activo": True},
        {"id": 5, "nombre": "Ojos", "descripcion": "Sombras y delineadores", "activo": True},
    ]

    # 🔹 PROVEEDORES (5 registros)
    proveedores = [
        {"id": 1, "nombre": "Distribuidora Glamour", "telefono": "300123", "email": "glam@mail.com", "activo": True},
        {"id": 2, "nombre": "Laboratorios BioSkin", "telefono": "310987", "email": "bio@mail.com", "activo": True},
        {"id": 3, "nombre": "Importaciones BeautyWorld", "telefono": "320111", "email": "world@mail.com", "activo": True},
        {"id": 4, "nombre": "Cosméticos Estelar", "telefono": "300555", "email": "estelar@mail.com", "activo": True},
        {"id": 5, "nombre": "Herramientas Belleza Pro", "telefono": "315444", "email": "pro@mail.com", "activo": True},
    ]

    # Configuración de campos
    campos_prod = ["id", "nombre", "precio", "cantidad", "categoria_id", "proveedor_id", "activo"]
    campos_cat = ["id", "nombre", "descripcion", "activo"]
    campos_prov = ["id", "nombre", "telefono", "email", "activo"]

    def escribir(nombre, datos, campos):
        ruta = os.path.join(DATA_PATH, nombre)
        with open(ruta, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(datos)
        print(f"✅ {nombre} reseteado con éxito.")

    escribir("productos.csv", productos, campos_prod)
    escribir("categorias.csv", categorias, campos_cat)
    escribir("proveedores.csv", proveedores, campos_prov)

if __name__ == "__main__":
    resetear_datos()