CREATE DATABASE IF NOT EXISTS concerts_db;
USE concerts_db;

CREATE TABLE IF NOT EXISTS concerts (
    id_concert INT AUTO_INCREMENT PRIMARY KEY,
    grup VARCHAR(100) NOT NULL,
    ciutat VARCHAR(100) NOT NULL,
    sala VARCHAR(100) NOT NULL,
    data DATE NOT NULL,
    hora TIME NOT NULL
);

INSERT INTO concerts (grup, ciutat, sala, data, hora) VALUES
('Coldplay', 'Barcelona', 'Palau Sant Jordi', '2025-06-15', '21:00:00'),
('AC/DC', 'Madrid', 'WiZink Center', '2025-07-20', '20:30:00'),
('Estopa', 'Valencia', 'Estadio Mestalla', '2025-08-10', '22:00:00'),
('Rosalía', 'Sevilla', 'Estadio Olímpico', '2025-09-05', '21:30:00'),
('Muse', 'Barcelona', 'Estadi Olímpic', '2025-10-12', '20:00:00');
