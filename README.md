# La Pitayera

**Tienda online de pitahayas — proyecto de 2.º de DAW**

## 1. Datos del proyecto

- **Autora:** Inés Llopis Martínez
- **Centro educativo:** IES Severo Ochoa — Elche
- **Ciclo formativo:** Desarrollo de Aplicaciones Web (DAW)
- **Curso académico:** 2026/2027

## 2. Descripción

La Pitayera es un proyecto de aplicación web para una tienda especializada en pitahayas, también conocidas como frutas del dragón. La propuesta contempla un catálogo, cuentas de cliente, carrito de compra y gestión de pedidos. La zona de administración permitirá gestionar productos, categorías, inventario, clientes y pedidos. Estas funcionalidades se irán incorporando durante el desarrollo.

## 3. Objetivos

- Desarrollar una aplicación web de comercio electrónico especializada en pitahayas.
- Ofrecer un catálogo para consultar productos y sus características.
- Facilitar la gestión de compras y pedidos.
- Incorporar una zona de administración para gestionar los datos de la tienda.
- Restringir las operaciones administrativas a usuarios autorizados.
- Diseñar una interfaz clara, adaptable a ordenadores, tablets y móviles.

## 4. Temática

La temática es el comercio electrónico de productos alimentarios, concretamente la venta de pitahayas. La identidad visual se inspira en la naturaleza y en las características de esta fruta, con una estética fresca y moderna.

## 5. Tecnologías

- **Backend:** Python y Django 5.2.
- **Base de datos:** MariaDB en Docker Compose. Para la ejecución local sin `MARIADB_HOST`, la configuración utiliza SQLite.
- **Frontend:** React, Vite, JavaScript, HTML5 y CSS3.
- **Contenedores:** Docker y Docker Compose.
- **API REST:** Django REST Framework está previsto para una fase posterior.

## 6. Modelos actuales

El backend contiene nueve modelos en las apps `billing` y `core`. Sus campos, restricciones y relaciones están descritos en [docs/modelos.md](docs/modelos.md).

### Relaciones principales

- Cada factura pertenece a un cliente; un cliente puede tener varias facturas.
- Cada cobro pertenece a una factura; una factura puede tener varios cobros.
- Cada pedido pertenece a un cliente; un cliente puede tener varios pedidos.
- Cada producto pertenece a una categoría; una categoría puede tener varios productos.
- Los detalles relacionan pedidos y productos.
- Cada movimiento de inventario pertenece a un producto y a un tipo de movimiento.
- Un tipo de movimiento puede clasificarse en varios movimientos de inventario.

El diagrama E/R está en [docs/DiagramaER.png](docs/DiagramaER.png) y su fuente en [docs/diagramaER.md](docs/diagramaER.md).

## 7. Ejecutar con Docker Compose

Se necesita Docker Desktop en ejecución. Desde PowerShell, en la raíz del repositorio, crea la configuración local a partir de la plantilla:

```powershell
Copy-Item .env.example .env
```

Edita `.env` y establece contraseñas y una clave secreta propias. Después inicia los servicios:

```powershell
docker compose up --build -d
```

El contenedor del backend aplica las migraciones al arrancar. Django estará disponible en <http://localhost:8000/> y el frontend en <http://localhost:3000/>. Para crear un superusuario la primera vez:

```powershell
docker compose exec backend python manage.py createsuperuser
```

El administrador de Django está en <http://localhost:8000/admin/>. Para detener los servicios:

```powershell
docker compose down
```

## 8. Estructura principal

- `backend/`: proyecto Django y apps `common`, `core` y `billing`.
- `backend/templates/`: plantillas compartidas y de cada app.
- `frontend/`: aplicación React/Vite servida mediante Nginx en Docker.
- `docs/`: documentación y diagramas del proyecto.

## 9. Enlace a ClickUp

<https://app.clickup.com/1500510000002045/v/dc/1ampjurgczx-512/1ampjurgczx-72>
