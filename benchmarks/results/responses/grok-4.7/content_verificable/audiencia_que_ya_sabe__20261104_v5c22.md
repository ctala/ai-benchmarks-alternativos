# Grok 4.7 — content_verificable/audiencia_que_ya_sabe

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.36 | quality: 10.0
- latency_total: 17.633s | tokens_per_second: 36.5
- input_tokens: 1337 | output_tokens: 644

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Un execution en verde no demuestra que el side effect ocurrió. Solo dice que ningún nodo lanzó un error no capturado. El grafo puede terminar en `success` con cero ítems, con la rama falsa de un IF que no hace nada, o con un HTTP que respondió 200 y un body de error de negocio.

El caso más frecuente es la cadena vacía. Un nodo filtra, un Merge no encuentra match, o el trigger no trae payload útil. Sin ítems, los nodos de abajo no corren. n8n no lo trata como fallo: no había nada que fallar. Igual de silencioso es Continue On Fail, o un nodo que traga el error y sigue. El workflow “terminó bien” y el CRM, la cola o la hoja quedaron igual.

El webhook empeora la ilusión. Si respondes al caller antes de las escrituras —o con Respond to Webhook en el primer nodo— el cliente ya tiene su 200 mientras el resto puede no-opear. Un cron no tiene ni ese testigo externo: si no escribes un resultado comprobable, el verde del historial es la única señal, y miente.

Detección: no midas el status de la execution. Mide el contrato. Al final, un nodo que exija lo que debía pasar: `items.length` mayor que cero, un id devuelto por la API, un row count, un flag `wrote: true` puesto solo después del side effect. Si la aserción falla, tira error a propósito. Revisa el body, no solo el status code. Y alerta cuando una ejecución recurrente produce cero ítems o cero escrituras: ese es el `success` vacío, y sin esa comprobación no lo vas a ver.