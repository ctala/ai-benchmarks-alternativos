# Qwen 3.8 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.9 | quality: 10.0
- latency_total: 33.571s | tokens_per_second: 116.2
- input_tokens: 148 | output_tokens: 3900

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Un workflow en n8n puede terminar en success y no haber hecho nada porque success no significa negocio completado: significa que la ejecución llegó a un nodo final sin errores no controlados. Y eso es una trampa.

Puede pasar por cosas que parecen inocentes:
- El trigger recibe un payload vacío o con campos distintos a los esperados, y el primer Set/Filter elimina los items.
- Un IF o Switch deja fuera el único ítem por un booleano, un string o una fecha en formato inesperado.
- Un Code node devuelve [] cuando la lógica no encuentra coincidencias.
- Un Loop sobre una lista vacía se completa “perfectamente”.
- Un HTTP Request devuelve success porque la petición terminó, aunque el body diga error, o porque tienes configuración de tolerancia a fallos.

El problema es que n8n te muestra una ejecución verde, pero tu sistema externo no cambió de estado.

Para detectarlo, deja de confiar en el status. Añade una aserción de negocio: después del paso crítico, usa un Code o IF que falle si no hay ítems o si falta un ID. Convierte “no output” en error explícito. Registra siempre un correlation ID al inicio y comprueba al final que existe una marca de resultado. Si algo puede fallar silenciosamente, crea un nodo final “Validación” que consulte el estado real: ¿se creó el registro? ¿se envió el mensaje? ¿se actualizó el ticket?

Success sin efectos es deuda silenciosa. Haz que tu workflow no pueda terminar felizmente sin demostrar que hizo el trabajo.