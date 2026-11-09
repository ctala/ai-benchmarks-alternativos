ALTER TABLE clientes ADD COLUMN rut TEXT;
CREATE UNIQUE INDEX clientes_rut_idx ON clientes (rut);
