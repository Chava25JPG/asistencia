SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


CREATE DATABASE IF NOT EXISTS asistencia_escuela DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;

USE asistencia_escuela;


CREATE TABLE especialidad (
id int(11) NOT NULL,
nombre varchar(255) NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE modulos (
id int(11) NOT NULL AUTO_INCREMENT,
nombre varchar(255) NOT NULL,
hora_inicio time NOT NULL,
hora_fin time NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE materia (
id int(11) NOT NULL AUTO_INCREMENT,
nombre varchar(255) NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE maestro (
id int(11) NOT NULL AUTO_INCREMENT,
nombre varchar(255) NOT NULL,
apellidoPaterno varchar(255) NOT NULL,
apellidoMaterno varchar(255) NOT NULL,
RFIDcard varchar(8) NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;



CREATE TABLE horario (
id int(11) NOT NULL,
grupo_id int(11) NOT NULL,
dia varchar(255) DEFAULT NULL,
materia_id int(11) NOT NULL,
maestro_id int(11) NOT NULL,
modulo_id int(11) NOT NULL,
PRIMARY KEY (id),
CONSTRAINT fk_horario_grupo FOREIGN KEY (grupo_id) REFERENCES grupos(id),
CONSTRAINT fk_horario_modulo FOREIGN KEY (modulo_id) REFERENCES modulos(id),
CONSTRAINT fk_horario_materia FOREIGN KEY (materia_id) REFERENCES materia(id),
CONSTRAINT fk_horario_maestro FOREIGN KEY (maestro_id) REFERENCES maestro (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;


CREATE TABLE grupos (
    id int(11) NOT NULL AUTO_INCREMENT,
    GradoYGrupo varchar(3),
    especialidad_id int(11) NOT NULL,
    horario_id int(11) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_grupos_especialidad FOREIGN KEY (especialidad_id) REFERENCES especialidad(id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE alumno (
    id int(11) NOT NULL,
    nombre varchar(255) NOT NULL,
    apellidoPaterno varchar(255) NOT NULL,
    apellidoMaterno varchar(255) NOT NULL,
    grupo_id int(11) NOT NULL,
    RFIDcard varchar(8) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT fk_alumno_grupos FOREIGN KEY (grupo_id) REFERENCES grupos(id)
    ) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

CREATE TABLE asistencia (
  id int(11) NOT NULL AUTO_INCREMENT,
  alumno_id int(11) NOT NULL,
  materia_id int(11) NOT NULL,
  maestro_id int(11) NOT NULL,
  hora_de_entrada time NOT NULL,
  fecha date NOT NULL,
  asistio tinyint(1) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT fk_asistencia_alumno FOREIGN KEY (alumno_id) REFERENCES alumno (id),
  CONSTRAINT fk_asistencia_materia FOREIGN KEY (materia_id) REFERENCES materia (id),
  CONSTRAINT fk_asistencia_maestro FOREIGN KEY (maestro_id) REFERENCES maestro (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;








INSERT INTO horario (grupo_id, dia, materia_id, maestro_id, modulo_id)
VALUES 
(1 ,'Lunes', 1, 1, 1),
(1 ,'Lunes', 1, 1, 2),
(1 ,'Lunes', 2, 2, 4),
(1 ,'Lunes', 3, 3, 5),
(1 ,'Lunes', 3, 3, 6),
(1 ,'Lunes', 3, 3, 7),
(1 ,'Lunes', 4, 4, 8),
(1, 'Martes', 4, 4, 1),
(1, 'Martes', 4, 4, 2),
(1, 'Martes', 5, 5, 4),
(1, 'Martes', 5, 5, 5),
(1, 'Martes', 6, 6, 6),
(1, 'Martes', 6, 6, 7),
(1, 'Martes', 1, 1, 8),
(1 ,'Miercoles', 1, 1, 1),
(1 ,'Miercoles', 1, 1, 2),
(1 ,'Miercoles', 2, 2, 4),
(1 ,'Miercoles', 3, 3, 5),
(1 ,'Miercoles', 3, 3, 6),
(1 ,'Miercoles', 3, 3, 7),
(1 ,'Miercoles', 4, 4, 8),
(1, 'Jueves', 4, 4, 1),
(1, 'Jueves', 4, 4, 2),
(1, 'Jueves', 5, 5, 4),
(1, 'Jueves', 5, 5, 5),
(1, 'Jueves', 6, 6, 6),
(1, 'Jueves', 6, 6, 7),
(1, 'Jueves', 1, 1, 8),
(1 ,'Viernes', 1, 1, 1),
(1 ,'Viernes', 1, 1, 2),
(1 ,'Viernes', 2, 2, 4),
(1 ,'Viernes', 3, 3, 5),
(1 ,'Viernes', 3, 3, 6),
(1 ,'Viernes', 3, 3, 7),
(1 ,'Viernes', 4, 4, 8);
