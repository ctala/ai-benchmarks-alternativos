-- Esquema de /app/crm.db (ya creado). Una fila por lead.
CREATE TABLE leads (
    email          TEXT PRIMARY KEY,   -- en minúsculas
    nombre         TEXT NOT NULL,
    empresa        TEXT NOT NULL,
    pais           TEXT NOT NULL,      -- Chile | México | Colombia | Perú
    rubro          TEXT NOT NULL,
    presupuesto_usd REAL NOT NULL,     -- presupuesto mensual convertido a USD, 2 decimales
    telefono       TEXT NOT NULL,      -- formato E.164, p. ej. +56912345678
    recibido       TEXT NOT NULL       -- fecha del correo que originó los datos, AAAA-MM-DD
);
