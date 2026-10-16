# Diagrama entidad-relacion

Este diagrama representa las entidades principales de La Pitayera y las relaciones entre ellas.

```mermaid
erDiagram
    
    PRODUCTO {
        int id_producto PK
        string nombre
        string tipo
        string descripcion
        decimal precio
    }

    PEDIDO {
        int id_pedido PK
        date fecha_creacion
    }

    LINEA_PEDIDO {
        int id_linea_pedido PK
        int id_producto FK
        int id_pedido FK
        int cantidad
        decimal precio_unitario
    }

    FACTURA {
        int id_factura PK
        int id_pedido FK
        string estado
        date fecha_creacion
    }

    COBRO {
        int id_cobro PK
        int id_factura FK
        decimal importe
        date fecha_creacion
    }

    PRODUCTO ||--o{ LINEA_PEDIDO : aparecer
    PEDIDO ||--o{ LINEA_PEDIDO : contener
    FACTURA ||--|| PEDIDO : tener
    FACTURA ||--o{ COBRO : tener
    
```