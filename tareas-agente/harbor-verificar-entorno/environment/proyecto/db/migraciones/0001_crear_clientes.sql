CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    razon_social TEXT NOT NULL,
    creado_en TIMESTAMP NOT NULL DEFAULT now()
);
