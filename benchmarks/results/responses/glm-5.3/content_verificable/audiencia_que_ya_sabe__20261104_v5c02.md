# GLM 5.3 — content_verificable/audiencia_que_ya_sabe

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 35.545s | tokens_per_second: 75.3
- input_tokens: 107 | output_tokens: 2675

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Verde no significa hecho**

En n8n, "success" significa una sola cosa: ningún nodo lanzó una excepción. No significa que tu workflow hiciera lo que debía. Y ahí vive el problema.

Los tres sospechosos habituales:

1. **Cero items en entrada.** Un Filter o un IF con una condición de fechas se come todos los items, y los nodos downstream ni se ejecutan. Es comportamiento por diseño: ejecución verde, trabajo real cero.

2. **"Never Error" / Continue On Fail.** Tu HTTP Request recibe un 500 con body de error, pero el nodo lo trata como dato normal. Y ese body acaba escrito en Sheets como si fuera una fila legítima.

3. **Ramas muertas.** La rama false del IF no conecta a nada. La ejecución termina ahí, en verde, sin tocar nada.

Cómo cazarlo:

- **Aserciones, no optimismo.** Tras el nodo crítico, un IF con `{{ $input.all().length === 0 }}` → Stop and Error con mensaje descriptivo. Si no pasó nada, que reviente.
- **Valida payloads, no status codes.** ¿Existe `{{ $json.id }}`? ¿`$json.deleted === true`? El API que responde 200 con "nope" es un clásico.
- **Usa `$('Update DB').isExecuted`** en tu nodo final para confirmar que los nodos críticos corrieron de verdad en esta ejecución.
- **Alerta sobre conteos raros**: exporta las ejecuciones por la API y vigila las runs con menos nodos ejecutados de lo esperado. Tres nodos donde esperas doce es un success mentiroso.

Regla mental: success = "no explotó". La pregunta útil es otra: ¿llegó algún item al último nodo?

Si tu alerting solo mira el estado de la ejecución, no tienes alerting. Tienes decoración.