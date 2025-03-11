SHOW ENGINES;

SHOW VARIABLES;

SET default_storage_engine = 'InnoDB';

-- CREACIÓN DE LA BD
CREATE DATABASE zapateria CHARACTER SET UTF8MB4
COLLATE UTF8MB4_UNICODE_CI;

SHOW DATABASES;

-- SELECCIÓN DE LA BD
USE zapateria;

-- CREACIÓN DE LAS TABLAS
CREATE TABLE cliente(
    id_cliente INT AUTO_INCREMENT,
    nombre_cliente VARCHAR(60) NOT NULL,
    apellidos_cliente VARCHAR(120) NOT NULL,
    correo VARCHAR(80),
    telefono VARCHAR(10),
    PRIMARY KEY(id_cliente)
);

CREATE TABLE producto(
    id_producto INT AUTO_INCREMENT,
    nombre_producto VARCHAR(70) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    talla INT NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL,
    PRIMARY KEY(id_producto)
);

CREATE TABLE empleado(
    id_empleado INT AUTO_INCREMENT,
    nombre_empleado VARCHAR(60) NOT NULL,
    apellidos_empleado VARCHAR(120) NOT NULL,
    puesto VARCHAR(50),
    telefono VARCHAR(10),
    PRIMARY KEY(id_empleado)
);

CREATE TABLE venta(
    id_venta INT AUTO_INCREMENT,
    fecha_venta DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_cliente INT,
    id_producto INT,
    id_empleado INT,
    cantidad INT NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    PRIMARY KEY(id_venta)
);

SHOW TABLES;

-- RELACIONES Y RESTRICCIONES
ALTER TABLE venta ADD CONSTRAINT fk_cliente_venta
FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente);

ALTER TABLE venta ADD CONSTRAINT fk_producto_venta
FOREIGN KEY(id_producto) REFERENCES producto(id_producto);

ALTER TABLE venta ADD CONSTRAINT fk_empleado_venta
FOREIGN KEY(id_empleado) REFERENCES empleado(id_empleado);

INSERT INTO cliente (nombre_cliente, apellidos_cliente, correo, telefono) VALUES
('Juan', 'Pérez López', 'juan.perez@email.com', '5551234567'),
('María', 'González Díaz', 'maria.gonzalez@email.com', '5552345678'),
('Carlos', 'Ramírez Soto', 'carlos.ramirez@email.com', '5553456789'),
('Ana', 'Martínez Ruiz', 'ana.martinez@email.com', '5554567890'),
('Luis', 'Hernández Peña', 'luis.hernandez@email.com', '5555678901'),
('Sofía', 'Torres Vargas', 'sofia.torres@email.com', '5556789012'),
('Daniel', 'Jiménez Castro', 'daniel.jimenez@email.com', '5557890123'),
('Laura', 'Morales Navas', 'laura.morales@email.com', '5558901234'),
('Miguel', 'Díaz Salazar', 'miguel.diaz@email.com', '5559012345'),
('Fernanda', 'Castillo Orozco', 'fernanda.castillo@email.com', '5550123456');

SELECT * FROM cliente;

INSERT INTO producto (nombre_producto, marca, talla, precio, stock) VALUES
('Zapato Formal', 'Nike', 42, 899.99, 20),
('Tenis Deportivo', 'Adidas', 40, 799.99, 15),
('Botas de Cuero', 'Timberland', 43, 1299.99, 10),
('Sandalias', 'Crocs', 38, 499.99, 30),
('Zapato Casual', 'Puma', 41, 699.99, 25),
('Tacones', 'Steve Madden', 37, 1199.99, 8),
('Mocasines', 'Ferragamo', 42, 1599.99, 5),
('Tenis Urbanos', 'Reebok', 39, 649.99, 18),
('Chanclas', 'Under Armour', 40, 299.99, 40),
('Botines', 'Clarks', 42, 999.99, 12);

SELECT * FROM producto;


INSERT INTO empleado (nombre_empleado, apellidos_empleado, puesto, telefono) VALUES
('Pedro', 'Fernández Ortega', 'Cajero', '5552233445'),
('Carla', 'Mendoza Ríos', 'Vendedor', '5553344556'),
('Andrés', 'López Ramírez', 'Gerente', '5554455667'),
('Elena', 'García Torres', 'Vendedor', '5555566778'),
('Roberto', 'Santos Martínez', 'Supervisor', '5556677889'),
('Paola', 'Ruiz Chávez', 'Cajero', '5557788990'),
('Gustavo', 'Herrera Díaz', 'Almacén', '5558899001'),
('Daniela', 'Núñez Velasco', 'Vendedor', '5559900112'),
('Emilio', 'Cortez Guzmán', 'Administrador', '5550011223'),
('Verónica', 'Figueroa Paredes', 'Cajero', '5551122334');

SELECT * FROM empleado;

INSERT INTO venta (id_cliente, id_producto, id_empleado, cantidad, total) VALUES
(1, 3, 2, 1, 1299.99),
(2, 5, 1, 2, 1399.98),
(3, 2, 4, 1, 799.99),
(4, 1, 3, 3, 2699.97),
(5, 4, 5, 1, 499.99),
(6, 7, 6, 1, 1599.99),
(7, 9, 8, 2, 599.98),
(8, 6, 7, 1, 1199.99),
(9, 8, 10, 3, 1949.97),
(10, 10, 9, 1, 999.99);

SELECT * FROM venta;













