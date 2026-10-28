# Modelos de datos

Este documento describe los modelos que existen actualmente en las apps `billing` y `core` del backend.

## App `billing`

### Cliente

- `nombre`: texto de hasta 256 caracteres.
- `apellidos`: texto de hasta 512 caracteres.
- `nif`: texto de hasta 20 caracteres, único.
- `email`: dirección de correo electrónico, única.

### Factura

- `cliente`: clave foránea a `Cliente` (`on_delete=PROTECT`).
- `n_factura`: texto de hasta 20 caracteres, único.
- `concepto`: texto.
- `fecha`: fecha, con la fecha actual como valor predeterminado.
- `total`: decimal de hasta 10 dígitos y 2 decimales, con valor predeterminado `0`.

### Cobro

- `factura`: clave foránea a `Factura` (`on_delete=PROTECT`). Una factura puede tener varios cobros.
- `fecha`: fecha, con la fecha actual como valor predeterminado.
- `importe`: decimal de hasta 10 dígitos y 2 decimales, con valor predeterminado `0`.

## App `core`

### Categoria

- `nombre`: texto de hasta 256 caracteres.
- `descripcion`: texto.

### Producto

- `nombre`: texto de hasta 256 caracteres.
- `sku`: texto de hasta 20 caracteres, único.
- `categoria`: clave foránea a `Categoria` (`on_delete=PROTECT`).
- `descripcion`: texto.
- `precio`: decimal de hasta 10 dígitos y 2 decimales, con valor predeterminado `0`.

### Pedido

- `cliente`: clave foránea a `billing.Cliente` (`on_delete=PROTECT`).
- `n_pedido`: texto de hasta 20 caracteres, único.
- `fecha`: fecha, con la fecha actual como valor predeterminado.
- `total`: decimal de hasta 10 dígitos y 2 decimales, con valor predeterminado `0`.

### DetallePedido

- `pedido`: clave foránea a `Pedido` (`on_delete=PROTECT`).
- `producto`: clave foránea a `Producto` (`on_delete=PROTECT`).
- `cantidad`: entero positivo.
- `precio_unitario`: decimal de hasta 10 dígitos y 2 decimales, con valor predeterminado `0`.
- La combinación de `pedido` y `producto` es única.

### MovimientoInventario

- `producto`: clave foránea a `Producto` (`on_delete=PROTECT`).
- `tipo`: clave foránea a `TipoMovimiento` (`on_delete=PROTECT`).
- `fecha`: fecha, con la fecha actual como valor predeterminado.
- `cantidad`: entero positivo.

### TipoMovimiento

- `nombre`: texto de hasta 256 caracteres.
- `motivo`: texto de hasta 256 caracteres.

## Relaciones

- Un cliente puede tener varias facturas; cada factura pertenece a un cliente.
- Una factura puede tener varios cobros; cada cobro pertenece a una factura.
- Un cliente puede tener varios pedidos; cada pedido pertenece a un cliente.
- Una categoría puede tener varios productos; cada producto pertenece a una categoría.
- Un pedido puede tener varios detalles; cada detalle pertenece a un pedido.
- Un producto puede aparecer en varios detalles; cada detalle corresponde a un producto.
- Un producto puede tener varios movimientos de inventario; cada movimiento corresponde a un producto.
- Un tipo de movimiento puede clasificarse en varios movimientos de inventario; cada movimiento tiene un tipo.

Los modelos usan la clave primaria automática de Django (`id`), que no se repite en las listas de campos anteriores.
