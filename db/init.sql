CREATE TABLE IF NOT EXISTS preguntas (
    id SERIAL PRIMARY KEY,
    pregunta TEXT NOT NULL,
    opcion_a TEXT NOT NULL,
    opcion_b TEXT NOT NULL,
    opcion_c TEXT NOT NULL,
    opcion_d TEXT NOT NULL,
    respuesta_correcta CHAR(1) NOT NULL
);

INSERT INTO preguntas (pregunta, opcion_a, opcion_b, opcion_c, opcion_d, respuesta_correcta) VALUES
('¿Cuánto es 2 x 4?', '2', '4', '6', '8', 'D'),
('¿Cuánto es 5 x 6?', '11', '30', '56', '26', 'B'),
('¿Cuánto es 3 x 3?', '9', '2', '4', '1', 'A'),
('¿Cuánto es 2 x 2?', '2', '4', '6', '8', 'B'),
('¿Cuánto es 5 x 5?', '11', '30', '56', '25', 'D'),
('¿Cuánto es 3 x 4?', '9', '2', '12', '1', 'C'),
('¿Cuánto es 2 x 3?', '2', '4', '6', '8', 'C'),
('¿Cuánto es 5 x 4?', '11', '20', '56', '25', 'B'),
('¿Cuánto es 3 x 5?', '9', '2', '15', '1', 'C'),
('¿Cuánto es 2 x 5?', '2', '4', '6', '10', 'D')