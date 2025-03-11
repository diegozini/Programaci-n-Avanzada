SHOW ENGINES;

SHOW VARIABLES;

SET default_storage_engine = 'InnoDB';

-- CREACIÓN DE LA BD
CREATE DATABASE hospital CHARACTER SET UTF8MB4
COLLATE UTF8MB4_UNICODE_CI;

SHOW DATABASES;

-- SELECCIÓN DE LA BD
USE hospital;

-- CREACIÓN DE LAS TABLAS
CREATE TABLE paciente(
    id_paciente INT AUTO_INCREMENT,
    nombre_paciente VARCHAR(60) NOT NULL,
    apellidos_paciente VARCHAR(120) NOT NULL,
    fecha_nacimiento DATE,
    direccion VARCHAR(200),
    telefono VARCHAR(10),
    PRIMARY KEY(id_paciente)
);

CREATE TABLE doctor(
    id_doctor INT AUTO_INCREMENT,
    nombre_doctor VARCHAR(60) NOT NULL,
    apellidos_doctor VARCHAR(120) NOT NULL,
    especialidad VARCHAR(50),
    telefono VARCHAR(10),
    PRIMARY KEY(id_doctor)
);

CREATE TABLE habitacion(
    id_habitacion INT AUTO_INCREMENT,
    numero_habitacion INT NOT NULL UNIQUE,
    tipo_habitacion VARCHAR(20),
-- Ej: Individual, Compartida
    piso INT NOT NULL,
    PRIMARY KEY(id_habitacion)
);
CREATE TABLE registro_medico(
    id_registro INT AUTO_INCREMENT,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,
    descripcion TEXT,
    id_paciente INT,
    id_doctor INT,
    id_habitacion INT,
    PRIMARY KEY(id_registro)
);

SHOW TABLES;

-- RELACIONES Y RESTRICCIONES
ALTER TABLE registro_medico ADD CONSTRAINT fk_paciente_registro
FOREIGN KEY(id_paciente) REFERENCES paciente(id_paciente);

ALTER TABLE registro_medico ADD CONSTRAINT fk_doctor_registro
FOREIGN KEY(id_doctor) REFERENCES doctor(id_doctor);

ALTER TABLE registro_medico ADD CONSTRAINT fk_habitacion_registro
FOREIGN KEY(id_habitacion) REFERENCES habitacion(id_habitacion);