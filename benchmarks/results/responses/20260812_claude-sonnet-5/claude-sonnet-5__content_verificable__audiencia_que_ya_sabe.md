# Claude Sonnet 5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 13.962s | tokens_per_second: 64.7
- input_tokens: 159 | output_tokens: 904

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**El "success" que miente**

Un workflow en n8n puede terminar en verde sin haber movido una sola fila, sin haber mandado un mensaje, sin haber tocado nada. Y eso es peor que un error explícito, porque nadie lo va a revisar.

Los casos típicos:

- Un **Filter** o **IF** que descarta el 100% de los items. El workflow no falla, simplemente no tenía nada que hacer y tú interpretas silencio como "todo bien".
- Un **HTTP Request** que responde 200 pero con un body que dice `{"error": "not found"}`. n8n no distingue eso de un éxito real a menos que lo valides tú.
- Un **Split in Batches** o loop que itera sobre un array vacío. Cero ejecuciones, cero errores, cero acción.
- Credenciales o tokens vencidos que devuelven una respuesta "válida" pero vacía en lugar de un 401 claro.

El problema de fondo: el motor de ejecución de n8n solo sabe si un nodo lanzó una excepción, no si el resultado tiene sentido de negocio. Eso es responsabilidad tuya.

**Cómo detectarlo:**

1. Después de cualquier nodo que filtre o transforme, mete un **NoOp** o un **Set** que cuente items (`$items().length`) y compáralo contra lo esperado.
2. Usa un nodo de validación explícito después de cada HTTP Request: si el body no tiene la estructura que esperas, fuerza un error con un **Code** node.
3. Manda esos contadores a un log central (Airtable, Postgres, lo que uses) con el número de items procesados por ejecución, no solo el status.
4. Alerta cuando el conteo sea 0 en workflows que normalmente procesan algo — eso casi siempre es una señal, no una coincidencia.

Success sin evidencia es solo una promesa. Verifícala.