# BEAUTY BRATZ – API de Gestión de Inventario

¡Bienvenida a **Beauty Bratz**! Este proyecto es un sistema de gestión de inventarios desarrollado con **FastAPI**. Está diseñado específicamente para administrar productos de belleza, categorías y proveedores de forma eficiente y segura.


---

##  Mapa de Endpoints 
| Entidad | Método | Endpoint | Descripción |
| :--- | :---: | :--- | :--- |
| **Productos** | `GET` | `/productos` | Obtiene la lista completa de productos (Activos/Inactivos). |
| **Productos** | `POST` | `/productos` | Registra un nuevo producto en el sistema. |
| **Productos** | `PUT` | `/productos/{id}` | Actualiza la información de un producto existente. |
| **Productos** | `DELETE` | `/productos/{id}` | Realiza un borrado lógico (cambia estado a inactivo). |
| **Productos** | `GET` | `/productos/buscar/{n}` | **Busca** productos por su nombre (Punto 7). |
| **Productos** | `GET` | `/productos/filtrar/c/{id}` | **Filtra** productos por ID de categoría (Punto 6). |
| **Categorías** | `GET` | `/categorias` | Lista todas las categorías de belleza. |
| **Categorías** | `POST` | `/categorias` | Crea una nueva categoría (Rostro, Labios, etc.). |
| **Proveedores** | `GET` | `/proveedores` | Lista los proveedores registrados. |
| **Proveedores** | `POST` | `/proveedores` | Registra un nuevo proveedor o distribuidora. |

---

##  Instalación y Ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone <tu-url-de-github>