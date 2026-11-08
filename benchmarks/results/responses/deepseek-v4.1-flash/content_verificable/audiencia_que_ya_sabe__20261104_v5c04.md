# DeepSeek V4.1 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 9.03 | quality: 10.0
- latency_total: 15.322s | tokens_per_second: 106.3
- input_tokens: 126 | output_tokens: 1629

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Verde no es lo mismo que funcionó**

En n8n, `success` significa exactamente una cosa: nada lanzó una excepción. No significa que entraron items, que salieron, ni que el destino se escribió.

Las formas habituales de acabar en verde sin hacer nada:

- Un nodo aguas arriba devuelve `[]`. Cero items se propagan y los nodos siguientes **no se ejecutan**. No hay error porque no hay nada que falle.
- Un Filter o un IF descarta todo. La rama muerta termina ahí, sin ruido.
- Un `onError: continueRegularOutput` se come un error real y emite un item con `error`. El flujo sigue, termina verde.
- Un nodo que deshabilitaste para debug y nunca reactivaste.

Cómo cazarlo:

1. **Mira el conteo de items, no el color.** En la lista de ejecuciones. Si esperabas 500 y hay 0, ese es el bug.
2. **Assertion al final.** Un Code node que tire error si `items.length === 0` o si cae por debajo de un umbral que tú defines.
3. **`alwaysOutputData`** en los nodos propensos al vacío, para que al menos viaje un item y puedas detectarlo.
4. **Un workflow de verificación en cron que consulte el destino, no n8n.** "¿Hubo inserts hoy?" Si no, alerta. n8n nunca va a saber que no escribiste nada.
5. **Log estructurado** con `execution_id`, `items_in`, `items_out`. Alerta cuando `items_out = 0` sin motivo.

El verde es un estado del ejecutor, no un hecho sobre tus datos.