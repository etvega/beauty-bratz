from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from main import app
from app.database import get_db

# Cliente de prueba
client = TestClient(app)


# =====================
# 🔹 PRODUCTOS
# =====================

def test_get_productos():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    with patch("app.services.services.obtener_productos", return_value=[]):
        response = client.get("/productos")
        assert response.status_code == 200
        assert response.json() == []
    app.dependency_overrides.clear()


def test_add_producto_valido():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    mock_producto = MagicMock()
    mock_producto.id = 1
    mock_producto.nombre = "Labial rojo"
    mock_producto.precio = 15000.0
    mock_producto.cantidad = 10
    mock_producto.categoria_id = 1
    mock_producto.proveedor_id = 1
    mock_producto.activo = True
    with patch("app.services.services.crear_producto", return_value=mock_producto):
        response = client.post("/productos", json={
            "nombre": "Labial rojo",
            "precio": 15000,
            "cantidad": 10,
            "categoria_id": 1,
            "proveedor_id": 1
        })
        assert response.status_code == 200
    app.dependency_overrides.clear()


def test_add_producto_precio_invalido():
    response = client.post("/productos", json={
        "nombre": "Labial rojo",
        "precio": -5,
        "cantidad": 10,
        "categoria_id": 1,
        "proveedor_id": 1
    })
    assert response.status_code == 422


def test_add_producto_nombre_muy_corto():
    response = client.post("/productos", json={
        "nombre": "A",
        "precio": 5000,
        "cantidad": 10,
        "categoria_id": 1,
        "proveedor_id": 1
    })
    assert response.status_code == 422


def test_update_producto_existente():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    with patch("app.services.services.actualizar_producto", return_value={"mensaje": "Producto actualizado"}):
        response = client.put("/productos/1", json={
            "nombre": "Labial rosa",
            "precio": 12000,
            "cantidad": 5,
            "categoria_id": 1,
            "proveedor_id": 1
        })
        assert response.status_code == 200
        assert response.json()["mensaje"] == "Producto actualizado"
    app.dependency_overrides.clear()


def test_update_producto_no_existente():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    with patch("app.services.services.actualizar_producto", return_value={"error": "Producto no encontrado"}):
        response = client.put("/productos/999", json={
            "nombre": "Labial rosa",
            "precio": 12000,
            "cantidad": 5,
            "categoria_id": 1,
            "proveedor_id": 1
        })
        assert response.status_code == 404
    app.dependency_overrides.clear()


def test_delete_producto_existente():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    with patch("app.services.services.eliminar_producto", return_value={"mensaje": "Producto marcado como inactivo"}):
        response = client.delete("/productos/1")
        assert response.status_code == 200
        assert response.json()["mensaje"] == "Producto marcado como inactivo"
    app.dependency_overrides.clear()


def test_delete_producto_no_existente():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    with patch("app.services.services.eliminar_producto", return_value={"error": "Producto no encontrado"}):
        response = client.delete("/productos/999")
        assert response.status_code == 404
    app.dependency_overrides.clear()


def test_buscar_producto_por_nombre():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    with patch("app.services.services.buscar_producto_por_nombre", return_value=[]):
        response = client.get("/productos/buscar/labial")
        assert response.status_code == 200
    app.dependency_overrides.clear()


def test_filtrar_productos_por_categoria():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    with patch("app.services.services.filtrar_productos_por_categoria", return_value=[]):
        response = client.get("/productos/filtrar/categoria/1")
        assert response.status_code == 200
    app.dependency_overrides.clear()


# =====================
# 🔹 CATEGORÍAS
# =====================

def test_get_categorias():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    with patch("app.services.services.obtener_categorias", return_value=[]):
        response = client.get("/categorias")
        assert response.status_code == 200
    app.dependency_overrides.clear()


def test_add_categoria_valida():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    mock_cat = MagicMock()
    mock_cat.id = 1
    mock_cat.nombre = "Labios"
    with patch("app.services.services.crear_categoria", return_value=mock_cat):
        response = client.post("/categorias", json={"nombre": "Labios"})
        assert response.status_code == 200
    app.dependency_overrides.clear()


def test_add_categoria_nombre_muy_corto():
    response = client.post("/categorias", json={"nombre": "A"})
    assert response.status_code == 422


def test_update_categoria_no_existente():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    with patch("app.services.services.actualizar_categoria", return_value={"error": "Categoría no encontrada"}):
        response = client.put("/categorias/999", json={"nombre": "Ojos"})
        assert response.status_code == 404
    app.dependency_overrides.clear()


def test_delete_categoria_existente():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    with patch("app.services.services.eliminar_categoria", return_value={"mensaje": "Categoría desactivada"}):
        response = client.delete("/categorias/1")
        assert response.status_code == 200
    app.dependency_overrides.clear()


# =====================
# 🔹 PROVEEDORES
# =====================

def test_get_proveedores():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    with patch("app.services.services.obtener_proveedores", return_value=[]):
        response = client.get("/proveedores")
        assert response.status_code == 200
    app.dependency_overrides.clear()


def test_add_proveedor_valido():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    mock_prov = MagicMock()
    mock_prov.id = 1
    mock_prov.nombre = "Distribuidora XYZ"
    with patch("app.services.services.crear_proveedor", return_value=mock_prov):
        response = client.post("/proveedores", json={
            "nombre": "Distribuidora XYZ",
            "telefono": "3001234567",
            "email": "contacto@xyz.com"
        })
        assert response.status_code == 200
    app.dependency_overrides.clear()


def test_add_proveedor_email_invalido():
    response = client.post("/proveedores", json={
        "nombre": "Distribuidora XYZ",
        "telefono": "3001234567",
        "email": "no-es-un-email"
    })
    assert response.status_code == 422


def test_add_proveedor_telefono_invalido():
    response = client.post("/proveedores", json={
        "nombre": "Distribuidora XYZ",
        "telefono": "abc",
        "email": "contacto@xyz.com"
    })
    assert response.status_code == 422


def test_delete_proveedor_no_existente():
    mock_db = MagicMock()
    app.dependency_overrides[get_db] = lambda: mock_db
    with patch("app.services.services.eliminar_proveedor", return_value={"error": "Proveedor no encontrado"}):
        response = client.delete("/proveedores/999")
        assert response.status_code == 404
    app.dependency_overrides.clear()