SHOW ENGINES;

SHOW VARIABLES;

SET default_storage_engine = 'InnoDB';

-- CREACIÓN DE LA BD
CREATE DATABASE escuela CHARACTER SET UTF8MB4
COLLATE UTF8MB4_UNICODE_CI;

SHOW DATABASES;

-- SELECCIÓN DE LA BD
USE escuela;

-- CREACIÓN DE LAS TABLAS
CREATE TABLE alumno(
    id_alumno INT AUTO_INCREMENT,
    nombre_alumno VARCHAR(60) NOT NULL,
    apellidos_alumno VARCHAR(120) NOT NULL,
    correo VARCHAR(80),
    telefono VARCHAR(10),
    PRIMARY KEY(id_alumno)
);

CREATE TABLE curso(
    id_curso INT AUTO_INCREMENT,
    nombre_curso VARCHAR(70) NOT NULL UNIQUE,
    descripcion VARCHAR(200),
    creditos INT NOT NULL,
    id_profesor INT,
    PRIMARY KEY(id_curso)
);

CREATE TABLE profesor(
    id_profesor INT AUTO_INCREMENT,
    nombre_profesor VARCHAR(60) NOT NULL,
    apellidos_profesor VARCHAR(120) NOT NULL,
    especialidad VARCHAR(50),
    telefono VARCHAR(10),
    PRIMARY KEY(id_profesor)
);

CREATE TABLE inscripcion (
    id_inscripcion INT AUTO_INCREMENT,
    fecha_inscripcion DATETIME DEFAULT CURRENT_TIMESTAMP,
    id_alumno INT,
    id_curso INT,
    PRIMARY KEY(id_inscripcion),
    CONSTRAINT fk_alumno_inscripcion
        FOREIGN KEY(id_alumno) REFERENCES alumno(id_alumno)
        ON DELETE CASCADE,
    CONSTRAINT fk_curso_inscripcion
        FOREIGN KEY(id_curso) REFERENCES curso(id_curso)
);

SHOW TABLES;

-- RELACIONES Y RESTRICCIONES
ALTER TABLE curso ADD CONSTRAINT fk_profesor_curso
FOREIGN KEY(id_profesor) REFERENCES profesor(id_profesor);

ALTER TABLE inscripcion ADD CONSTRAINT fk_alumno_inscripcion
FOREIGN KEY(id_alumno) REFERENCES alumno(id_alumno);

ALTER TABLE inscripcion ADD CONSTRAINT fk_curso_inscripcion
FOREIGN KEY(id_curso) REFERENCES curso(id_curso);

-- Inserción de Profesores
INSERT INTO profesor (nombre_profesor, apellidos_profesor, especialidad, telefono) VALUES
('Carlos', 'Hernández López', 'Matemáticas', '5551234567'),
('María', 'González Pérez', 'Historia', '5559876543'),
('Luis', 'Ramírez Díaz', 'Física', '5554567890'),
('Ana', 'Torres Jiménez', 'Química', '5556543210'),
('Jorge', 'Martínez Castro', 'Programación', '5551122334');

-- Inserción de Cursos
INSERT INTO curso (nombre_curso, descripcion, creditos, id_profesor) VALUES
('Álgebra', 'Curso introductorio de álgebra', 5, 1),
('Historia Universal', 'Estudio de la historia mundial', 4, 2),
('Mecánica Clásica', 'Principios fundamentales de la física', 5, 3),
('Química Orgánica', 'Introducción a la química del carbono', 5, 4),
('Programación en Python', 'Curso básico de programación en Python', 6, 5);

-- Inserción de Alumnos
INSERT INTO alumno (nombre_alumno, apellidos_alumno, correo, telefono) VALUES
('Pedro', 'López García', 'pedro.lopez@email.com', '5557891234'),
('Sofía', 'Martínez Rodríguez', 'sofia.martinez@email.com', '5553219876'),
('Daniel', 'Gómez Fernández', 'daniel.gomez@email.com', '5554561237'),
('Lucía', 'Sánchez Pérez', 'lucia.sanchez@email.com', '5556549871'),
('Andrés', 'Díaz Jiménez', 'andres.diaz@email.com', '5551472583');

-- Inserción de Inscripciones
INSERT INTO inscripcion (id_alumno, id_curso) VALUES
(1, 1),
(1, 3),
(2, 2),
(2, 5),
(3, 4),
(3, 1),
(4, 3),
(4, 5),
(5, 2),
(5, 4);

SELECT * FROM profesor;

SELECT * FROM curso;

SELECT * FROM alumno;

SELECT * FROM inscripcion;