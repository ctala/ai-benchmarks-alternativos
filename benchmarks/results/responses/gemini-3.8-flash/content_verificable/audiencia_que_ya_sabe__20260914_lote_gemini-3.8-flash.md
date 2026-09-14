# Gemini 3.8 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 13.042s | tokens_per_second: 109.8
- input_tokens: 93 | output_tokens: 1432

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**El falso verde en n8n: cuando «Success» significa «no hice nada»**

Todos conocemos esa falsa paz: entras al historial de ejecuciones, ves una columna impecable de checks verdes y asumes que todo va como la seda. Spoiler: tu base de datos lleva doce horas sin actualizarse.

En n8n, una ejecución termina en *Success* simplemente si ningún nodo lanzó una excepción no controlada. Esto abre la puerta a fallos silenciosos típicos:

1. **El bucle fantasma (0 items):** Si un nodo previo filtra o devuelve un array vacío (`[]`), los nodos downstream que iteran por ítem simplemente no se ejecutan. El flujo llega al final sin tocar la API de destino y marca éxito.
2. **APIs que devuelven 200 con errores:** GraphQL, Slack o pasarelas legacy te devuelven un `status: 200` con un `{"ok": false, "error": "..."}` en el body. Para el nodo HTTP Request básico, eso es un éxito rotundo.
3. **Ramas huérfanas:** Un nodo *IF* o *Switch* donde el 100% del tráfico cae en la salida falsa, la cual no tiene nada conectado. 

**Cómo blindarlo:**

* **Fuerza excepciones:** Si esperas datos sí o sí, mete un nodo *Code* o *IF* que evalúe `$input.all().length === 0` y lanza un `throw new Error("Payload vacío inesperado")`. Rompe el flujo adrede.
* **Usa nodos *Stop and Error*:** Deja de abandonar ramas muertas. Conecta los caminos residuales a un *Stop and Error* para que el canvas pinte el fallo real y salte tu *Error Trigger*.
* **Inspecciona el JSON, no el HTTP Status:** Tras llamadas críticas, valida propiedades semánticas (`data`, `id`, `success: true`) antes de continuar.

Un workflow que revienta ruidosamente se arregla en cinco minutos; el que falla en silencio te cuesta clientes.