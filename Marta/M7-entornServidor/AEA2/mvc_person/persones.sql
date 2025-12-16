CREATE DATABASE IF NOT EXISTS patromvc;

CREATE TABLE IF NOT EXISTS patromvc.persones (
  id TiNYINT AUTO_INCREMENT PRIMARY KEY,
  
  nom VARCHAR(30),
  edat TINYINT,
  alcada REAL

);

INSERT INTO patromvc.persones (nom, edat, alcada) VALUES 
    ('Irene',18,1.78),
    ('Nuria',22,1.70),
    ('Joan','19',1.85),
    ('Marc','45',1.80),
    ('Anna','35',1.76),
    ('Laia','38',1.72),
    ('Toni','31',1.92);
  