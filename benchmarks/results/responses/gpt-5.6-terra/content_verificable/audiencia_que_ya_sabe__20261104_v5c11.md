# GPT-5.6 Terra — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 6.82s | tokens_per_second: 71.8
- input_tokens: 101 | output_tokens: 490

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Un workflow en n8n puede terminar en verde y, aun así, no haber producido ningún efecto real. No es una contradicción: *success* normalmente significa que ningún nodo lanzó un error no controlado. No significa que se cumplió el objetivo de negocio.

Los casos más comunes:

- Un nodo devuelve cero items y el resto de la rama no se ejecuta.
- Un `IF` enruta todos los items a una salida que no tiene nodos conectados.
- Una búsqueda no encuentra registros; técnicamente es una respuesta válida.
- Una API responde `200` o `202`, pero acepta la petición para procesarla después —o la deduplica por idempotencia.
- Un nodo tiene activado `Continue On Fail`, captura el problema y deja que la ejecución finalice.
- Un filtro demasiado restrictivo convierte una ejecución con 500 entradas en una ejecución con cero acciones.

La solución no es buscar más errores. Es definir qué evidencia demuestra que el workflow hizo su trabajo.

Añade señales explícitas de resultado: `items_received`, `items_matched`, `items_processed`, `items_created`, `items_failed`. Al final, valida invariantes. Por ejemplo: “si llegaron pedidos, debe haberse actualizado al menos uno”, o “el número de registros creados debe coincidir con el número enviado, salvo duplicados justificados”.

Cuando una condición sea inesperada, no dejes que el flujo muera silenciosamente: envía una alerta, registra el motivo y, si corresponde, fuerza un error. Un nodo `Code` o `IF` final puede actuar como aserción de negocio.

También conviene revisar ejecuciones exitosas con volumen cero y monitorizar ratios, no solo fallos: porcentaje de items filtrados, acciones por ejecución y tiempo desde la última acción efectiva.

El estado verde responde: “¿se rompió el workflow?”. Tus métricas deben responder: “¿pasó lo que debía pasar?”.