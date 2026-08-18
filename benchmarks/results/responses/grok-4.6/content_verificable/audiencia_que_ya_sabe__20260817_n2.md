# Grok 4.6 — content_verificable/audiencia_que_ya_sabe

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 25.05s | tokens_per_second: 53.7
- input_tokens: 301 | output_tokens: 1344

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**El success que no hizo nada**

En n8n, `success` solo significa que la ejecución terminó sin excepción no capturada. No implica side effects, items procesados ni que el contrato del workflow se haya cumplido. Un IF que filtra todo, un Code que devuelve `[]`, un Merge con una rama muerta, un Execute Workflow vacío o un HTTP 200 con error de negocio pintan verde igual.

Los patrones habituales: `continueOnFail` / `neverError` en escrituras (el 4xx/5xx viaja como item y el grafo sigue); Respond to Webhook al principio (el caller ya tiene 200 mientras el resto no corre o corre a cero items); Set/Code que pisan el payload y dejan el nodo de acción sin entrada; subflujos que “ok” con output vacío. El runtime no distingue “no había trabajo” de “falló en silencio”.

No mires el estado de la ejecución: mira el **item count** nodo a nodo. Si el nodo que escribe (DB, API, cola, Slack) recibió 0 items, no hizo el trabajo. Eso es el indicador, no el check verde.

Fuerza el rojo. Al final del camino crítico, un IF o un Code que haga `throw` si no hay id creado, `affected === 0`, o falta el campo que la API solo devuelve cuando de verdad persistió. Sin aserción, el invariante no existe. En nodos de escritura, no uses `continueOnFail` sin un nodo inmediatamente después que inspeccione `statusCode` / `$json.error` y falle.

Responde al webhook cuando el efecto ya es observable, no al entrar. En prod: alerta si el nodo crítico lleva N ejecuciones seguidas a 0 items o si la duración es ridículamente baja para ese grafo. Success es ausencia de crash. Completitud la afirmáis vosotros.