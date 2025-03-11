SHOW ENGINES;

SHOW VARIABLES;

SET default_storage_engine = 'InnoDB';

-- CREACIÓN DE LA BD
CREATE DATABASE plaza_comercial CHARACTER SET UTF8MB4
COLLATE UTF8MB4_UNICODE_CI;

SHOW DATABASES;

-- SELECCIÓN DE LA BD
USE plaza_comercial;

-- CREACIÓN DE LAS TABLAS
CREATE TABLE tienda(
    id_tienda INT AUTO_INCREMENT,
    nombre_tienda VARCHAR(70) NOT NULL UNIQUE,
    sector VARCHAR(30) NOT NULL,
    dir_tienda VARCHAR(200) NOT NULL,
    PRIMARY KEY(id_tienda)
);

CREATE TABLE empleado(
    id_empleado INT AUTO_INCREMENT,
    nombre_empleado VARCHAR(60) NOT NULL,
    apellidos VARCHAR(120) NOT NULL,
    email VARCHAR(80),
    telefono VARCHAR(10),
    id_tienda INT,
    PRIMARY KEY(id_empleado)
);

CREATE TABLE producto(
    id_producto INT AUTO_INCREMENT,
    nombre_producto VARCHAR(50) NOT NULL,
    descripcion VARCHAR(200),
    precio DECIMAL(10,2),
    stock INT,
    id_tienda INT,
    PRIMARY KEY(id_producto)
);

CREATE TABLE registro_venta(
    id_venta INT AUTO_INCREMENT,
    fecha_venta DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_producto INT,
    id_empleado INT,
    cantidad INT,
    PRIMARY KEY(id_venta)
);

SHOW TABLES;

-- RELACIONES Y RESTRICCIONES
ALTER TABLE empleado ADD CONSTRAINT fk_tienda_empleado
FOREIGN KEY(id_tienda) REFERENCES tienda(id_tienda);

ALTER TABLE producto ADD CONSTRAINT fk_tienda_producto
FOREIGN KEY(id_tienda) REFERENCES tienda(id_tienda);

ALTER TABLE registro_venta ADD CONSTRAINT fk_producto_venta
FOREIGN KEY(id_producto) REFERENCES producto(id_producto);

ALTER TABLE registro_venta ADD CONSTRAINT fk_empleado_venta
FOREIGN KEY(id_empleado) REFERENCES empleado(id_empleado);

INSERT INTO tienda (nombre_tienda, sector, dir_tienda) VALUES
('Supermercado La Estrella', 'Alimentos', 'Av. Central #123'),
('ElectroMundo', 'Electrónica', 'Calle 45, Zona Industrial'),
('Moda Express', 'Ropa', 'Plaza Principal, Local 5'),
('Librería Alfa', 'Papelería', 'Av. Universidad #56'),
('Farmacia Salud Total', 'Salud', 'Calle San José #8');

SELECT * FROM tienda;

INSERT INTO empleado (nombre_empleado, apellidos, email, telefono, id_tienda) VALUES
('Carlos', 'Pérez Gómez', 'carlos.perez@email.com', '5551234567', 1),
('María', 'López Ramírez', 'maria.lopez@email.com', '5552345678', 2),
('Javier', 'Martínez Herrera', 'javier.martinez@email.com', '5553456789', 3),
('Ana', 'Torres Jiménez', 'ana.torres@email.com', '5554567890', 4),
('Sofía', 'González Díaz', 'sofia.gonzalez@email.com', '5555678901', 5);

SELECT * FROM empleado;

INSERT INTO producto (nombre_producto, descripcion, precio, stock, id_tienda) VALUES
('Arroz 1kg', 'Paquete de arroz blanco de 1kg', 20.50, 100, 1),
('Televisor 55\"', 'Smart TV UHD 4K', 7999.99, 10, 2),
('Pantalón Jeans', 'Pantalón de mezclilla azul', 499.99, 50, 3),
('Cuaderno 100 hojas', 'Cuaderno rayado de 100 hojas', 35.00, 200, 4),
('Paracetamol 500mg', 'Caja con 10 tabletas', 25.00, 500, 5);

SELECT * FROM producto;

INSERT INTO registro_venta (id_producto, id_empleado, cantidad) VALUES
(1, 1, 5),
(2, 2, 1),
(3, 3, 2),
(4, 4, 10),
(5, 5, 3);

SELECT * FROM registro_venta;







