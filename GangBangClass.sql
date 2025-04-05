SHOW ENGINES;
SET default_storage_engine = 'innoDB';

CREATE DATABASE gangclass CHARACTER SET UTF8MB4
COLLATE UTF8MB4_UNICODE_CI;

SHOW DATABASES; 

USE Gangclass;

-- Tabla de Profesores
CREATE TABLE profesores (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(70) NOT NULL,
    Correo VARCHAR(100) UNIQUE NOT NULL,
    Contraseña VARCHAR(255) NOT NULL,
    Creado_desde TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Alumnos
CREATE TABLE alumnos (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(70) NOT NULL,
    Correo VARCHAR(100) UNIQUE NOT NULL,
    Contraseña VARCHAR(255) NOT NULL,
    Creado_desde TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Profesor_id INT DEFAULT NULL,
    FOREIGN KEY (Profesor_id) REFERENCES profesores(Id) ON DELETE SET NULL
);

-- Tabla de Proyectos
CREATE TABLE proyectos (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion TEXT,
    Fecha_inicio DATE NOT NULL,
    Fecha_fin DATE,
    Creador_tipo ENUM('Profesor', 'Alumno') NOT NULL,
    Creador_id INT NOT NULL  -- Eliminamos la clave foránea para permitir más flexibilidad
);

-- Tabla de Tareas
CREATE TABLE tareas (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Descripcion TEXT NOT NULL,
    Estado ENUM('Pendiente', 'En Progreso', 'Completada') DEFAULT 'Pendiente',
    Fecha_limite DATE,
    Proyecto_id INT NOT NULL,
    Asignado_tipo ENUM('Profesor', 'Alumno') DEFAULT NULL,
    Asignado_id INT DEFAULT NULL,  -- No tiene clave foránea para permitir asignación flexible
    FOREIGN KEY (Proyecto_id) REFERENCES proyectos(Id) ON DELETE CASCADE
);

-- Tabla de Notificaciones
CREATE TABLE notificaciones (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Mensaje TEXT NOT NULL,
    Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Usuario_tipo ENUM('Profesor', 'Alumno') NOT NULL,
    Usuario_id INT NOT NULL,  -- No tiene clave foránea para que pueda ser profesor o alumno
    Leido BOOLEAN DEFAULT FALSE
);

--
SHOW TABLES;

SELECT * FROM profesores;
SELECT * FROM alumnos;
SELECT * FROM proyectos;
SELECT * FROM tareas;
SELECT * FROM notificaciones;

