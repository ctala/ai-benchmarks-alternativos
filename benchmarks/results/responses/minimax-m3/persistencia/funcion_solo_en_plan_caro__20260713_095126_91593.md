# MiniMax M3 — persistencia/funcion_solo_en_plan_caro

- model_id: `minimax/minimax-m3`
- success: True  | final: 6.48 | quality: 6.94
- latency_total: 28.166s | tokens_per_second: 45.2
- input_tokens: 343 | output_tokens: 1273

## Respuesta completa

Tres caminos, de menor a mayor potencia. Todos gratis.

## 1. Google Sheets (lo más fácil)

Importás los dos CSV a una planilla cada uno en su pestaña.

Supongamos que la fuente A tiene `id` y `nombre`, y la fuente B tiene `cliente_id` y `monto`. En la hoja de B, agregás una columna y ponés:

```
=XLOOKUP(B2, HojaA!A:A, HojaA!B:B, "no encontrado")
```

Eso te trae el nombre del cliente a cada fila de la hoja B. Después usás `SUMIF` o una tabla dinámica para agrupar.

**Limitación:** se pone lento con más de ~50k filas.

## 2. Google Colab + Python (cuando Sheets se queda corto)

Colab es un Jupyter gratuito en la nube, nada que instalar. Abrís [colab.research.google.com](https://colab.research.google.com), pegás esto:

```python
import pandas as pd

a = pd.read_csv('fuente_a.csv')
b = pd.read_csv('fuente_b.csv')

reporte = b.merge(a, left_on='cliente_id', right_on='id', how='left')

reporte.to_csv('reporte.csv', index=False)
reporte.head()
```

Subís los CSV con el botón de archivos de la barra lateral, ejecutás la celda, descargás `reporte.csv`.

**Para traer los datos desde la API en vez de CSV manual** (si te cansa exportar):

```python
import requests, pandas as pd

token = "TU_TOKEN"
def fetch(endpoint):
    items, page = [], 1
    while True:
        r = requests.get(f"https://api.tu-herramienta.com/v1/{endpoint}",
                         params={"page": page, "per_page": 100},
                         headers={"Authorization": f"Bearer {token}"}).json()
        items.extend(r["data"])
        if not r.get("next_page"): break
        page = r["next_page"]
    return pd.DataFrame(items)

a = fetch("clientes")
b = fetch("pedidos")
reporte = b.merge(a, left_on="cliente_id", right_on="id", how="left")
reporte.to_csv("reporte.csv", index=False)
```

Maneja la paginación solo, y pandas traga 100k+ filas sin despeinarse.

## 3. DuckDB (si te gusta SQL, archivo único)

Instalás una vez (`pip install duckdb` o bajás el CLI), y un solo archivo SQL hace todo:

```sql
SELECT a.nombre, SUM(b.monto) AS total
FROM 'fuente_a.csv' AS a
JOIN 'fuente_b.csv' AS b ON a.id = b.cliente_id
GROUP BY a.nombre
ORDER BY total DESC;
```

Corre directo sobre los CSV sin importarlos. Gratis, local, rapidísimo.

---

**Mi recomendación:** empezá por Sheets. Si se traba con volumen o necesitás automatizarlo (la API cada lunes, por ejemplo), saltá a Colab.