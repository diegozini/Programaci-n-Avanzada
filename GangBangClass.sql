
CREATE DATABASE IF NOT EXISTS gangclass CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE gangclass;


CREATE TABLE profesores (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Correo VARCHAR(100) UNIQUE NOT NULL,
    Contraseña VARCHAR(255) NOT NULL 
);


CREATE TABLE alumnos (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Correo VARCHAR(100) UNIQUE NOT NULL,
    Contraseña VARCHAR(255) NOT NULL 
);


CREATE TABLE proyectos (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion TEXT, NOT NULL,
    Fecha_inicio DATE NOT NULL,
    Fecha_fin DATE,
    
    Creador_profesor_id INT NULL,
    Creador_alumno_id INT NULL
    CHECK (
      (Creador_profesor_id IS NOT NULL AND Creador_alumno_id IS NULL) OR
      (Creador_profesor_id IS NULL AND Creador_alumno_id IS NOT NULL)
    ),
    FOREIGN KEY (Creador_profesor_id) REFERENCES profesores(Id) ON DELETE SET NULL,
    FOREIGN KEY (Creador_alumno_id) REFERENCES alumnos(Id) ON DELETE SET NULL,
    INDEX (Creador_profesor_id),
    INDEX (Creador_alumno_id)
);


CREATE TABLE tareas (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Descripcion TEXT NOT NULL,
    Estado ENUM('Pendiente', 'En Progreso', 'Completada') DEFAULT 'Pendiente',
    Fecha_limite DATE,
    Proyecto_id INT,
  
    Asignado_profesor_id INT NULL,
    Asignado_alumno_id INT NULL,
    CHECK (
      (Asignado_profesor_id IS NOT NULL AND Asignado_alumno_id IS NULL) OR
      (Asignado_profesor_id IS NULL AND Asignado_alumno_id IS NOT NULL)
    ),
    FOREIGN KEY (Proyecto_id) REFERENCES proyectos(Id) ON DELETE SET NULL,
    FOREIGN KEY (Asignado_profesor_id) REFERENCES profesores(Id) ON DELETE SET NULL,
    FOREIGN KEY (Asignado_alumno_id) REFERENCES alumnos(Id) ON DELETE SET NULL,
    INDEX (Proyecto_id),
    INDEX (Asignado_profesor_id),
    INDEX (Asignado_alumno_id)
);


CREATE TABLE notificaciones (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Mensaje TEXT NOT NULL,
    Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    Leido BOOLEAN DEFAULT FALSE,
    Usuario_profesor_id INT NULL,
    Usuario_alumno_id INT NULL,
    CHECK (
      (Usuario_profesor_id IS NOT NULL AND Usuario_alumno_id IS NULL) OR
      (Usuario_profesor_id IS NULL AND Usuario_alumno_id IS NOT NULL)
    ),
    FOREIGN KEY (Usuario_profesor_id) REFERENCES profesores(Id) ON DELETE CASCADE,
    FOREIGN KEY (Usuario_alumno_id) REFERENCES alumnos(Id) ON DELETE CASCADE,
    INDEX (Usuario_profesor_id),
    INDEX (Usuario_alumno_id)
);

INSERT INTO proyectos (nombre, desacripcion, Creador_id, Fecha_de_Creacion) VALUES
("Plataforma de Tareas y Proyectos", "Enfoque de experiencia de usuario", "6, "2025-05-19");
SELECT*FROM alumnos
SELECT*FROM profesores   

ALTER TABLE proyectos ADD COLUMN Descripcion TEXT;

DESCRIBE proyectos;
      
