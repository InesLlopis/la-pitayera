# La Pitayera

**Tienda online de pitahayas — Anteproyecto de 2.º DAW**

## 1. Datos del proyecto

- **Autora:** Inés Llopis Martínez
- **Centro educativo:** IES Severo Ochoa — Elche
- **Ciclo formativo:** Desarrollo de Aplicaciones Web (DAW)
- **Curso académico:** 2026/2027

## 2. Descripción de la aplicación

La Pitayera será una aplicación web de comercio electrónico especializada en la venta de pitahayas, también conocidas como frutas del dragón.

La aplicación permitirá a los usuarios consultar un catálogo de productos, registrarse e iniciar sesión, gestionar un carrito de compra y realizar pedidos.

También contará con una zona privada de administración desde la que los usuarios autorizados podrán gestionar los productos, las categorías, el inventario, los usuarios y los pedidos.

El proyecto busca centralizar en una misma plataforma la consulta de productos y la gestión de compras de una tienda especializada.

## 3. Objetivos

Los objetivos principales del proyecto son:

- Desarrollar una aplicación web de comercio electrónico especializada en pitahayas.
- Ofrecer un catálogo donde consultar los productos y sus características.
- Permitir el registro y la autenticación de usuarios.
- Facilitar la gestión del carrito de compra y de los pedidos.
- Incorporar una zona de administración para gestionar productos, categorías, inventario, usuarios y pedidos.
- Restringir las operaciones administrativas a los usuarios que dispongan del rol y los permisos correspondientes.
- Diseñar una interfaz clara, intuitiva y adaptable a ordenadores, tablets y móviles.
- Aplicar los conocimientos adquiridos en el ciclo de Desarrollo de Aplicaciones Web.

## 4. Temática

La temática del proyecto es el comercio electrónico de productos alimentarios, concretamente la venta de pitahayas.

La identidad visual se inspirará en la naturaleza y en las características de esta fruta, con una estética fresca y moderna. La interfaz priorizará la claridad, la usabilidad y la facilidad de navegación.

## 5. Tecnologías previstas

### Backend

- **Python:** lenguaje de programación previsto para el backend.
- **Django:** framework para desarrollar la aplicación.
- **Django REST Framework:** previsto para construir una API REST y permitir la comunicación con el frontend mediante JSON.

El backend gestionará la lógica de negocio, los datos y el control de acceso a las operaciones protegidas.

### Frontend

- **React:** desarrollo de la interfaz mediante componentes reutilizables.
- **Vite:** herramienta de desarrollo y construcción.
- **JavaScript, HTML5 y CSS3:** lógica, estructura y presentación de la interfaz.
- **React Router:** navegación entre las vistas de la aplicación.

### Base de datos

- **MariaDB:** sistema gestor de base de datos relacional previsto para almacenar la información de la tienda.

### Entorno de ejecución

- **Docker y Docker Compose:** previstos para facilitar la configuración y ejecución conjunta de los servicios de la aplicación.

Estas tecnologías constituyen la propuesta inicial y podrán concretarse durante la planificación posterior a la aprobación del anteproyecto.

## 6. Esquema entidad-relación (E/R)

El modelo de datos inicial se basa en los nueve modelos definidos actualmente en los archivos de modelos del proyecto. El esquema E/R que acompañe al anteproyecto deberá representar las entidades, sus atributos, las claves y las cardinalidades.

### 6.1. Entidades actuales

| Entidad | Atributos definidos actualmente |
|---|---|
| **Cliente** | `id` (clave primaria implícita de Django), `nombre`, `apellidos`, `nif` (único), `email` (único). |
| **Factura** | `id` (clave primaria implícita), `cliente` (FK a Cliente), `n_factura` (único), `concepto`, `fecha`, `total`. |
| **Cobro** | `id` (clave primaria implícita), `factura` (relación uno a uno con Factura), `fecha`, `importe`. |
| **Categoria** | `id` (clave primaria implícita), `nombre`, `descripcion`. |
| **Producto** | `id` (clave primaria implícita), `nombre`, `categoria` (FK a Categoria), `descripcion`, `precio`. |
| **Pedido** | `id` (clave primaria implícita), `cliente` (FK a Cliente), `n_pedido` (único), `fecha`, `total`. |
| **DetallePedido** | `id` (clave primaria implícita), `pedido` (FK a Pedido), `producto` (FK a Producto), `cantidad`, `precio_unitario`. |
| **MovimientoInventario** | `id` (clave primaria implícita), `producto` (FK a Producto), `fecha`, `cantidad`. |
| **TipoMovimiento** | `id` (clave primaria implícita), `movimiento` (FK a MovimientoInventario), `nombre`, `motivo`. |

Los campos `id` corresponden a las claves primarias que Django crea por defecto cuando no se declara una clave primaria explícita. Las relaciones `ForeignKey` corresponden a claves foráneas. `Cobro.factura` utiliza una relación `OneToOneField`.

### 6.2. Relaciones definidas en los modelos

- **Cliente — Factura:** un cliente puede tener varias facturas; cada factura está asociada a un cliente.
- **Factura — Cobro:** relación uno a uno entre Factura y Cobro.
- **Cliente — Pedido:** un cliente puede tener varios pedidos; cada pedido está asociado a un cliente.
- **Categoria — Producto:** una categoría puede tener varios productos; cada producto está asociado a una categoría.
- **Pedido — DetallePedido:** un pedido puede tener varias líneas de detalle; cada línea corresponde a un pedido.
- **Producto — DetallePedido:** un producto puede aparecer en varias líneas de detalle; cada línea corresponde a un producto.
- **Producto — MovimientoInventario:** un producto puede tener varios movimientos de inventario; cada movimiento corresponde a un producto.
- **MovimientoInventario — TipoMovimiento:** un movimiento puede tener varios registros asociados; cada registro de TipoMovimiento referencia un movimiento.

**Diagrama E/R:** pendiente de incorporar como diagrama gráfico a este documento antes de la entrega.

El modelo descrito corresponde al estado actual de los archivos. Podrán añadirse o modificarse modelos si las necesidades del desarrollo lo requieren, una vez autorizado el inicio del proyecto.

## 7. Administración y control de acceso

La aplicación incluirá una zona privada de administración, accesible únicamente a usuarios con el rol y los permisos correspondientes.

Esta zona permitirá gestionar los productos, las categorías, el inventario, los usuarios y los pedidos. Los clientes utilizarán las funcionalidades públicas de la tienda y las opciones asociadas a su cuenta y sus compras.

El control de acceso se implementará en el backend para impedir que usuarios no autorizados realicen operaciones administrativas. La solución concreta de autenticación y autorización se definirá durante el diseño técnico posterior a la aprobación.
