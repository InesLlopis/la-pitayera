# Diagrama entidad-relacion

Este diagrama representa las entidades principales de La Pitayera y las relaciones entre ellas.

```mermaid
erDiagram
    
    PRODUCTO {
        int id_producto PK
        string categoria FK
        string nombre
        string descripcion
        decimal precio
    }

    CATEGORIA {
        int id_categoria PK
        string nombre
        string descripcion
    }

    PEDIDO {
        int id_pedido PK
        int id_cliente FK
        string n_pedido UK
        date fecha
        decimal total
    }

    DETALLE_PEDIDO {
        int id_linea_pedido PK
        int id_pedido FK
        int id_producto FK
        int cantidad
        decimal precio_unitario
    }

    MOVIMIENTO_INVENTARIO {
        int id_movimiento PK
        int id_producto FK
        date fecha
        int cantidad
    }

    TIPO_MOVIMIENTO {
        int id_tipo_movimiento PK
        int id_movimiento FK
        string nombre
        string motivo
    }

    CLIENTE {
        int id_cliente PK
        string nombre
        string apellido
        string nif UK
        string email UK
    }

    FACTURA {
        int id_factura PK
        int id_cliente FK
        int id_pedido FK
        string n_factura UK
        string concepto
        decimal total
        date fecha_creacion
    }

    COBRO {
        int id_cobro PK
        int id_factura FK
        date fecha_creacion
        decimal importe
    }

    CLIENTE ||--o{ FACTURA : tener
    PEDIDO ||--o| FACTURA : generar
    FACTURA ||--o| COBRO : asociar
    CLIENTE ||--o{ PEDIDO : realizar
    CATEGORIA ||--o{ PRODUCTO : pertenecer
    PEDIDO ||--o{ DETALLE_PEDIDO: tener
    PRODUCTO ||--o{ DETALLE_PEDIDO : aparecer
    PRODUCTO ||--o{ MOVIMIENTO_INVENTARIO : registrar
    MOVIMIENTO_INVENTARIO ||--o{ TIPO_MOVIMIENTO : tener
    
```