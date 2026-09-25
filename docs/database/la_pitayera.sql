
-- BASE DE DATOS: LA PITAYERA

CREATE DATABASE IF NOT EXISTS la_pitayera
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE la_pitayera;


-- 1. TABLA: USUARIO

CREATE TABLE USUARIO (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    rol ENUM('CLIENTE', 'ADMIN')
        NOT NULL DEFAULT 'CLIENTE'
);


-- 2. TABLA: CATEGORIA

CREATE TABLE CATEGORIA (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    descripcion TEXT
);


-- 3. TABLA: PRODUCTO

CREATE TABLE PRODUCTO (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    descripcion TEXT,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    id_categoria INT NOT NULL,

    CONSTRAINT chk_producto_precio
        CHECK (precio >= 0),

    CONSTRAINT chk_producto_stock
        CHECK (stock >= 0),

    CONSTRAINT fk_producto_categoria
        FOREIGN KEY (id_categoria)
        REFERENCES CATEGORIA(id_categoria)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- 4. TABLA: CARRITO
-- Un carrito por usuario

CREATE TABLE CARRITO (
    id_carrito INT AUTO_INCREMENT PRIMARY KEY,
    fecha_creacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_usuario INT NOT NULL UNIQUE,

    CONSTRAINT fk_carrito_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES USUARIO(id_usuario)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);


-- 5. TABLA: DETALLE_CARRITO
-- Productos incluidos en el carrito

CREATE TABLE DETALLE_CARRITO (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    cantidad INT NOT NULL,
    id_carrito INT NOT NULL,
    id_producto INT NOT NULL,

    CONSTRAINT chk_detalle_carrito_cantidad
        CHECK (cantidad > 0),

    CONSTRAINT fk_detalle_carrito_carrito
        FOREIGN KEY (id_carrito)
        REFERENCES CARRITO(id_carrito)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT fk_detalle_carrito_producto
        FOREIGN KEY (id_producto)
        REFERENCES PRODUCTO(id_producto)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_carrito_producto
        UNIQUE (id_carrito, id_producto)
);


-- 6. TABLA: PEDIDO

CREATE TABLE PEDIDO (
    id_pedido INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
    estado ENUM(
        'PENDIENTE',
        'CONFIRMADO',
        'ENVIADO',
        'ENTREGADO',
        'CANCELADO'
    ) NOT NULL DEFAULT 'PENDIENTE',
    id_usuario INT NOT NULL,

    CONSTRAINT chk_pedido_total
        CHECK (total >= 0),

    CONSTRAINT fk_pedido_usuario
        FOREIGN KEY (id_usuario)
        REFERENCES USUARIO(id_usuario)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- 7. TABLA: DETALLE_PEDIDO
-- Productos incluidos en cada pedido

CREATE TABLE DETALLE_PEDIDO (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10, 2) NOT NULL,
    id_pedido INT NOT NULL,
    id_producto INT NOT NULL,

    CONSTRAINT chk_detalle_pedido_cantidad
        CHECK (cantidad > 0),

    CONSTRAINT chk_detalle_pedido_precio
        CHECK (precio_unitario >= 0),

    CONSTRAINT fk_detalle_pedido_pedido
        FOREIGN KEY (id_pedido)
        REFERENCES PEDIDO(id_pedido)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    CONSTRAINT fk_detalle_pedido_producto
        FOREIGN KEY (id_producto)
        REFERENCES PRODUCTO(id_producto)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,

    CONSTRAINT uq_pedido_producto
        UNIQUE (id_pedido, id_producto)
);
