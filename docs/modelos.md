# Modelos de datos

## Producto
- id
- nombre
- categoria
- descripcion
- precio

## Categoria
- id PK
- nombre
- descripcion

## Pedido
- id
- cliente
- fecha_creacion
- total

## DetallePedido
- id
- id_pedido
- id_producto
- cantidad
- precio_unitario

## MovimientoInventario
- id
- id_producto
- fecha
- cantidad

## TipoMovimiento
- id
- id_movimiento
- nombre
- motivo

## Cliente
- id
- nombre
- apellido
- nif
- email

## Factura
- id
- id_cliente
- id_pedido
- concepto
- fecha_creacion
- total

## Cobro
- id
- id_factura
- fecha_abono
- importe
