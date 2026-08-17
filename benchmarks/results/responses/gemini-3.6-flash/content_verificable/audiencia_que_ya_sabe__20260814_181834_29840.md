# Gemini 3.6 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.75 | quality: 10.0
- latency_total: 9.942s | tokens_per_second: 161.3
- input_tokens: 93 | output_tokens: 1604

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**El falso verde de n8n: cuando 'Success' significa 'no hice nada'**

Nada despierta más sospechas en producción que una ejecución en verde impecable que, en realidad, no ha procesado un solo registro. El estado **Success** solo garantiza que el motor de n8n llegó al final del grafo sin lanzar un error no capturado, no que tu lógica de negocio se haya ejecutado.

Los culpables habituales de este "falso verde" son tres:

1. **Arrays vacíos (0 items):** Si un *Filter*, *Loop* o una llamada API previa devuelve `[]`, los nodos posteriores no se ejecutan. Para n8n, procesar cero elementos correctamente sigue siendo un éxito.
2. **APIs con "Soft Errors":** Servicios como GraphQL, Shopify o Slack suelen responder con un `HTTP 200 OK`, pero con un payload tipo `{ "ok": false, "error": "invalid_auth" }`. Si solo confías en el HTTP Status Code, el flujo continuará a ciegas.
3. **"Continue on Fail" mal gestionado:** Silenciar errores en un nodo HTTP sin validar el output resultante genera *payloads* vacíos o corruptos que mueren en silencio más adelante.

**Cómo detectarlo y forzar el fallo:**

* **Assertions en Code Nodes:** Valida la longitud del input antes de proceder. Un simple `if ($input.all().length === 0) throw new Error("Payload vacío: nada que procesar");` romperá la ejecución a propósito para que aparezca en tus logs.
* **Usa el nodo *Stop and Error*:** Si una rama alternativa (un *False* en un *If*) implica que la automatización no cumplió su objetivo, no dejes que el flujo muera de forma natural. Conéctala a un *Stop and Error*.
* **Inspección de datos clave:** Configura alertas o monitoreo basándote en el consumo real de ítems al final del flujo, no solo en el estado global de la ejecución.

Un workflow que falla en silencio es peor que uno roto. Si no procesó datos, asegúrate de que n8n te lo diga en rojo.