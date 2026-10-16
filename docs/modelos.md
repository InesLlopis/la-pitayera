# Modelos de datos

## Producto
- id
- nombre
- tipo
- descripcion
- precio

## Pedido
- id
- fecha_creacion

## LineaPedido
- id
- id_producto
- id_pedido
- cantidad
- precio_unitario

## Factura
- id
- id_pedido
- estado
- fecha_creacion

## Cobro
- id
- id_factura
- importe
- fecha_abono
