# Claude Opus 4.8 (suscripción) — persistencia/funcion_solo_en_plan_caro

- model_id: `claude-opus-4-8`
- success: True  | final: 5.44 | quality: 6.3
- latency_total: 57.063s | tokens_per_second: 51.7
- input_tokens: 4 | output_tokens: 2952

## Respuesta completa

## El diagnóstico primero

"Reporte cruzado" es marketing para decir **JOIN**. Te están cobrando $471/mes extra por una operación que corre en tu laptop en milisegundos. Ya tienes las dos piezas que importan: los datos (CSV) y una forma de traerlos sin clicks (API paginada). El feature bloqueado no aporta data nueva, solo la une.

Así que el trabajo real no es "reemplazar el Enterprise". Es: **bajar las dos fuentes y unirlas por una llave.**

## Lo único que puede fallar: la llave

Antes de escribir una línea, abre los dos CSV y responde: **¿qué columna comparten?**

- **Hay un ID común** (`customer_id`, `order_id`) → listo, es trivial.
- **No hay ID pero hay un campo natural** (email, slug, SKU) → sirve, pero normaliza: `lower(trim(email))`. El 90% de los joins que "no matchean" es un espacio o una mayúscula.
- **No hay nada en común** → ahí sí tienes un problema real, y el Enterprise tampoco te lo iba a resolver por arte de magia. Probablemente hay una tercera tabla puente (la API suele exponerla aunque el UI no).

Dime qué columnas tienes y te armo el join exacto. Mientras tanto, la receta genérica:

## Camino A: cero código, 10 minutos (para validar que la idea funciona)

DuckDB lee CSVs directo, sin importar, sin base de datos, sin instalar servidor.

```bash
brew install duckdb   # o: pip install duckdb
```

```sql
duckdb -c "
SELECT
  a.customer_id,
  a.nombre,
  COUNT(b.id)      AS eventos,
  SUM(b.monto)     AS total
FROM read_csv_auto('fuente_a.csv') a
LEFT JOIN read_csv_auto('fuente_b.csv') b
  ON lower(trim(a.email)) = lower(trim(b.email))
GROUP BY 1,2
ORDER BY total DESC;
"
```

Ese `LEFT JOIN` **es** el feature de $500/mes. Agrega `> 'reporte.csv'` y ya lo tienes exportado.

Si te da alergia la terminal: Google Sheets con `XLOOKUP` hace lo mismo hasta ~50k filas. Funciona, pero no lo automatizas y se cae con volumen. Úsalo solo para probar la hipótesis, no como destino final.

## Camino B: el que de verdad quieres (automatizado, repetible)

El CSV manual te obliga a exportar a mano cada semana. Eso no escala y ya sabes que no es viable. Usa el endpoint de listado.

**Dos trampas de la paginación**, y las dos muerden en producción:

1. **Offset drift.** Si paginas con `?offset=0,100,200...` y alguien crea un registro mientras tú bajas la página 3, se te repiten o se te pierden filas. **Fix:** ordena por un campo inmutable (`ORDER BY id ASC`) y pagina por cursor (`?since_id=X`) si el endpoint lo permite. Si solo hay offset, ordena por `created_at asc` y acepta que la última página puede estar sucia.

2. **El CSV export miente.** Muchas herramientas cortan el export en 1.000 / 5.000 filas sin avisarte. **Antes de confiar en cualquier reporte:** compara el conteo de filas del CSV contra el `total` que devuelve la API. Si no coinciden, tu reporte está mal y nunca lo vas a notar.

Esqueleto de extracción:

```python
import requests, duckdb, pandas as pd

def bajar(endpoint):
    filas, page = [], 1
    while True:
        r = requests.get(endpoint, params={"page": page, "per_page": 100},
                         headers={"Authorization": f"Bearer {TOKEN}"}).json()
        data = r["data"]           # ajusta al shape real
        if not data: break
        filas += data
        page += 1
    return pd.DataFrame(filas)

a, b = bajar(URL_A), bajar(URL_B)

con = duckdb.connect()
reporte = con.execute("""
    SELECT a.*, COUNT(b.id) AS eventos, SUM(b.monto) AS total
    FROM a LEFT JOIN b ON a.id = b.customer_id
    GROUP BY ALL
""").df()
reporte.to_csv("reporte.csv", index=False)
```

Lo agendas con cron, con un workflow de n8n (ya lo tienes corriendo) o con GitHub Actions en el free tier. Costo marginal: $0.

## El error que te va a arruinar el número

**Fanout.** Si la fuente B tiene varias filas por cada fila de A (típico: clientes ↔ transacciones) y haces un JOIN plano, cada cliente se duplica y **cualquier suma sobre columnas de A queda inflada**. El reporte se ve perfecto y está mal.

Regla: si el lado B es "muchos", **agrega primero, une después**:

```sql
WITH b_agg AS (
  SELECT customer_id, COUNT(*) AS eventos, SUM(monto) AS total
  FROM read_csv_auto('fuente_b.csv') GROUP BY 1
)
SELECT a.*, COALESCE(b_agg.eventos,0) AS eventos, COALESCE(b_agg.total,0) AS total
FROM read_csv_auto('fuente_a.csv') a
LEFT JOIN b_agg ON a.id = b_agg.customer_id;
```

Y siempre valida contra un número que ya conozcas (un total que veas en el dashboard de la herramienta). Si tu reporte no reproduce ese número, no lo publiques.

## Resumen

| | Enterprise | Tu versión |
|---|---|---|
| Costo | $500/mes | $0 |
| Setup | 0 min | ~30 min una vez |
| Personalizable | Lo que el vendor decida | Cualquier query |
| Corre solo | Sí | Sí (cron/n8n) |

Lo único que compras con esos $471 es no tener que escribir 15 líneas.

**Pásame los headers de los dos CSV** (solo los nombres de columna, sin datos) y te devuelvo el query exacto con el join key correcto.