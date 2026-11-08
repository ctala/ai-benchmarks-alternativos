# GPT-5.6 Sol — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 7.188s | tokens_per_second: 70.5
- input_tokens: 101 | output_tokens: 507

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## “Success” no significa “trabajo hecho”

En n8n, un workflow puede terminar en verde y no haber producido ningún efecto. Técnicamente, todo funcionó: ninguna operación lanzó una excepción. Semánticamente, fue un *no-op*.

Casos habituales: una consulta devuelve cero filas, un filtro elimina todos los ítems, un `IF` conduce a una rama vacía, una API responde `200` pero ignora la actualización, o un nodo de base de datos ejecuta un `UPDATE` con `affectedRows: 0`. También ocurre cuando una expresión resuelve a `undefined` sin romper el nodo o cuando la deduplicación descarta silenciosamente todo el lote.

La solución no es añadir más logs: es definir **postcondiciones verificables**.

Después de cada operación crítica, valida explícitamente el efecto esperado:

- `items.length > 0` tras una búsqueda que debería encontrar datos.
- `affectedRows >= 1` después de una escritura.
- Presencia de un ID, estado o timestamp devuelto por la API.
- Diferencia real entre el estado anterior y el posterior.
- Conteos coherentes entre entrada, procesados, descartados y fallidos.

Conviene modelar tres resultados, no dos: **éxito con efecto**, **éxito sin efecto esperado** y **error técnico**. El segundo debe tener su propia rama, métrica y alerta; no necesariamente debe tumbar la ejecución.

Añade un resumen al final del workflow: `received`, `matched`, `changed`, `skipped`, `failed`. Persístelo o envíalo a tu sistema de observabilidad. Así puedes alertar por anomalías semánticas: “ejecución correcta, pero `changed = 0` durante tres ciclos”.

Y cuidado con la idempotencia: un `affectedRows: 0` puede ser correcto si el estado ya era el deseado. La detección útil compara el resultado con la intención, no solo con la ausencia de errores.

El verde indica que n8n no se rompió. No demuestra que el negocio avanzó.