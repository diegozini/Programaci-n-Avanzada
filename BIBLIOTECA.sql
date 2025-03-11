SHOW ENGINES;

SHOW VARIABLES;

SET default_storage_engine = 'InnoDB';

-- CREACIÓN DE LA BD
CREATE DATABASE biblioteca CHARACTER SET UTF8MB4
COLLATE UTF8MB4_UNICODE_CI;

SHOW DATABASES;

-- SELECCIÓN DE LA BD
USE biblioteca;

-- CREACIÓN DE LAS TABLAS
CREATE TABLE autor(
    id_autor INT AUTO_INCREMENT,
    nombre_autor VARCHAR(70) NOT NULL UNIQUE,
    nacionalidad VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_autor)
);

CREATE TABLE libro(
    id_libro INT AUTO_INCREMENT,
    titulo VARCHAR(100) NOT NULL,
    genero VARCHAR(30) NOT NULL,information_schemainformation_schemainformation_schemagangclass
    id_autor INT,
    fecha_publicacion DATE,
    PRIMARY KEY(id_libro)
);

CREATE TABLE lector(
    id_lector INT AUTO_INCREMENT,
    nombre_lector VARCHAR(60) NOT NULL,
    apellidos VARCHAR(120) NOT NULL,
    correo VARCHAR(80),
    telefono VARCHAR(10),
    PRIMARY KEY(id_lector)
);

CREATE TABLE prestamo(
    id_prestamo INT AUTO_INCREMENT,
    fecha_prestamo DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_libro INT,
    id_lector INT,
    fecha_devolucion DATE,
    PRIMARY KEY(id_prestamo)
);

SHOW TABLES;

-- RELACIONES Y RESTRICCIONES
ALTER TABLE libro ADD CONSTRAINT fk_autor_libro
FOREIGN KEY(id_autor) REFERENCES autor(id_autor);

ALTER TABLE prestamo ADD CONSTRAINT fk_libro_prestamo
FOREIGN KEY(id_libro) REFERENCES libro(id_libro);

ALTER TABLE prestamo ADD CONSTRAINT fk_lector_prestamo
FOREIGN KEY(id_lector) REFERENCES lector(id_lector);



