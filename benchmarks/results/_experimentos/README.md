# Experimentos — fuera del índice

Runs que **no rinden el examen del benchmark** y por eso no pueden vivir en
`results/benchmark_*.json`, que es lo que leen el export y casi todos los auditores.

| Archivo | Qué midió | Por qué no cuenta |
|---|---|---|
| `effort_medium_piloto_20260902.json` | 27 runs con `medium` forzado: GPT-5.6 Luna, Qwen 3.7 Flash y Gemma 4 31B, en `deep_reasoning` y `reasoning` | Effort distinto del default. Estuvo en lo publicado desde la regeneración del 3-sep hasta el 14-sep |
| `effort_por_tarea_20260904_{low,medium,high}.json` | 4 modelos × 4 suites × 3 niveles de effort | Effort forzado. Además, en `medium` 43 de 68 runs son `Connection error` y de `high` corrió 1 de 68: no sirve para concluir nada |
| `control_anthropic_20261106/{claude-opus-5.5,claude-sonnet-5.5}/` | `string_precision` (6 tests) de Opus 5.5 y Sonnet 5.5 por el proveedor **Anthropic** de OpenRouter, en vez de su declarado (Claude Platform on AWS). Declaración cambiada solo en memoria del proceso | Control: separa la negativa del modelo de la del filtro de la plataforma. Opus 5.5: 0 negativas de 6 (en AWS, 5 de 6). Sonnet 5.5: 2 de 6 (en AWS, 2 de 6). Costo ~$0,02 |
| `v5_claude55_fuera_del_indice_20261106.json` (+ `responses_v5_fuera_del_indice/`) | 12 runs de `tool_calling` de Opus, Sonnet y Haiku 5.5 en Anthropic, del lanzamiento del 6-nov que corrió sin `--tests` y planificó las 213 pruebas en vez de las 143 del índice | Suite fuera del índice v5: el lanzamiento se cortó a los ~10 min ($1,82) y se relanzó con las 29 suites. Origen del freno del runner (tarea 3 del 6-nov) |

**La regla:** todo experimento escribe acá
(`--resume benchmarks/results/_experimentos/<nombre>.json`). Si uno cae en la carpeta del
índice, `check_effort.py` falla (E5 por la etiqueta `pedido:` del run, E6 por el nombre) y
el export descarta sus runs igual.

Por qué el examen es el default de cada modelo: `DECISIONES.md`, fila del 14-sep-2026.
