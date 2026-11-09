# facturador-roble

Scripts internos de Ferretería El Roble SpA: reportes de ventas, sincronización con el
ERP y la base de facturación.

## Entorno

- **Python:** la versión exacta del proyecto la fija `.python-version`.
  `requires-python` de `pyproject.toml` es solo el mínimo compatible, y `runtime.txt`
  quedó del hosting anterior (Heroku) y ya no se usa.
- **Dependencias:** `requirements.txt`. Toda dependencia se fija con `==` a la versión
  instalada, una por línea.
- **Herramientas de desarrollo:** `requirements-dev.txt` (las mismas versiones que corre
  `pre-commit`).
- **Variables del entorno:** `.env`. Si existe `.env.local`, sus valores mandan sobre los
  de `.env`. `.env.example` y `config/app.example.toml` son plantillas con valores de
  ejemplo, no los del entorno.

## Estructura

- `scripts/` — scripts que se corren a mano o por cron.
- `datos/` — exportaciones del ERP.
- `reportes/` — reportes mensuales generados por `scripts/exportar.py`.
- `db/migraciones/` — migraciones SQL, numeradas en orden y aplicadas en ese orden.
- `legacy/` — código del sistema anterior. No se usa ni se modifica.
