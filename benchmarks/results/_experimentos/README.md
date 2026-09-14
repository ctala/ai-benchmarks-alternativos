# Experimentos — fuera del índice

Runs que **no rinden el examen del benchmark** y por eso no pueden vivir en
`results/benchmark_*.json`, que es lo que leen el export y casi todos los auditores.

| Archivo | Qué midió | Por qué no cuenta |
|---|---|---|
| `effort_medium_piloto_20260902.json` | 27 runs con `medium` forzado: GPT-5.6 Luna, Qwen 3.7 Flash y Gemma 4 31B, en `deep_reasoning` y `reasoning` | Effort distinto del default. Estuvo en lo publicado desde la regeneración del 3-sep hasta el 14-sep |
| `effort_por_tarea_20260904_{low,medium,high}.json` | 4 modelos × 4 suites × 3 niveles de effort | Effort forzado. Además, en `medium` 43 de 68 runs son `Connection error` y de `high` corrió 1 de 68: no sirve para concluir nada |

**La regla:** todo experimento escribe acá
(`--resume benchmarks/results/_experimentos/<nombre>.json`). Si uno cae en la carpeta del
índice, `check_effort.py` falla (E5 por la etiqueta `pedido:` del run, E6 por el nombre) y
el export descarta sus runs igual.

Por qué el examen es el default de cada modelo: `DECISIONES.md`, fila del 14-sep-2026.
