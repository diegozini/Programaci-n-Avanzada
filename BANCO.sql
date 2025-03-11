SHOW ENGINES;

SHOW VARIABLES;

SET default_storage_engine = 'InnoDB';

-- CREACIÓN DE LA BD
CREATE DATABASE banco CHARACTER SET UTF8MB4
COLLATE UTF8MB4_UNICODE_CI;

SHOW DATABASES;

-- SELECCIÓN DE LA BD
USE banco;

-- CREACIÓN DE LAS TABLAS
CREATE TABLE cliente(
    id_cliente INT AUTO_INCREMENT,
    nombre_cliente VARCHAR(60) NOT NULL,
    apellidos_cliente VARCHAR(120) NOT NULL,
    direccion VARCHAR(200),
    telefono CHAR(10),
    PRIMARY KEY(id_cliente)
);

CREATE TABLE cuenta(
    id_cuenta INT AUTO_INCREMENT,
    tipo_cuenta VARCHAR(20) NOT NULL,
    saldo DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    id_cliente INT NOT NULL,
    fecha_apertura DATE,
    PRIMARY KEY(id_cuenta),
    CONSTRAINT fk_cliente_cuenta FOREIGN KEY (id_cliente) 
    REFERENCES cliente(id_cliente) 
    ON DELETE CASCADE;
);

CREATE TABLE empleado(
    id_empleado INT AUTO_INCREMENT,
    nombre_empleado VARCHAR(60) NOT NULL,
    apellidos_empleado VARCHAR(120) NOT NULL,
    puesto VARCHAR(50),
    telefono CHAR(10),
    PRIMARY KEY(id_empleado)
);

CREATE TABLE transaccion(
    id_transaccion INT AUTO_INCREMENT,
    fecha_transaccion DATETIME DEFAULT CURRENT_TIMESTAMP,
    tipo_transaccion VARCHAR(20) NOT NULL, -- Ej: depósito, retiro
    monto DECIMAL(15,2) NOT NULL,
    id_cuenta INT NOT NULL,
    id_empleado INT NOT NULL,
    PRIMARY KEY(id_transaccion),
    CONSTRAINT fk_cuenta_transaccion FOREIGN KEY (id_cuenta) REFERENCES cuenta(id_cuenta),
    CONSTRAINT fk_empleado_transaccion FOREIGN KEY (id_empleado) REFERENCES empleado(id_empleado)
);

SHOW TABLES;

-- Insertar clientes
INSERT INTO cliente (nombre_cliente, apellidos_cliente, direccion, telefono) VALUES
('Juan', 'Pérez Gómez', 'Calle 123, Ciudad', '5551234567'),
('María', 'López Ramírez', 'Avenida 456, Ciudad', '5557654321'),
('Carlos', 'Sánchez Díaz', 'Boulevard 789, Ciudad', '5559876543'),
('Ana', 'García Torres', 'Callejón 321, Ciudad', '5553456789'),
('Luis', 'Martínez Herrera', 'Plaza 654, Ciudad', '5558765432');

-- Insertar cuentas
INSERT INTO cuenta (tipo_cuenta, saldo, id_cliente, fecha_apertura) VALUES
('Ahorros', 1500.50, 1, '2024-01-15'),
('Corriente', 3200.75, 2, '2024-01-20'),
('Ahorros', 5000.00, 3, '2024-02-01'),
('Corriente', 2800.00, 4, '2024-02-10'),
('Ahorros', 10000.25, 5, '2024-02-15');

SELECT * FROM cuenta;

-- Insertar empleados
INSERT INTO empleado (nombre_empleado, apellidos_empleado, puesto, telefono) VALUES
('Roberto', 'Fernández Soto', 'Cajero', '5551122334'),
('Laura', 'Gómez Vázquez', 'Gerente', '5552233445'),
('Miguel', 'Hernández Rojas', 'Asesor Financiero', '5553344556'),
('Andrea', 'Ruiz Morales', 'Cajero', '5554455667'),
('Sergio', 'Navarro Jiménez', 'Ejecutivo de Cuenta', '5555566778');

SELECT * FROM empleado;

-- Insertar transacciones
INSERT INTO transaccion (tipo_transaccion, monto, id_cuenta, id_empleado) VALUES
('Depósito', 500.00, 1, 1),
('Retiro', 200.00, 2, 2),
('Depósito', 1000.00, 3, 3),
('Retiro', 300.00, 4, 4),
('Depósito', 1500.00, 5, 5),
('Retiro', 250.00, 1, 1),
('Depósito', 2000.00, 2, 2),
('Retiro', 400.00, 3, 3),
('Depósito', 1200.00, 4, 4),
('Retiro', 500.00, 5, 5);

SELECT * FROM transaccion;
