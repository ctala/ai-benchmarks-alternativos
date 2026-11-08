# Qwen 3.6 35B base (OpenRouter FP8) — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 78.272s | tokens_per_second: 44.3
- input_tokens: 110 | output_tokens: 3467

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa



Un workflow en n8n marca “éxito” (verde) siempre que todos los nodos ejecuten sin lanzar excepciones. Eso no garantiza que se haya procesado datos, enviado un payload o disparado una acción externa. Es el clásico “silent success”.

Las causas más comunes:
- Nodos condicionales (`If`/`Switch`) que enrutan a ramas vacías o saltan ejecución por filtros estrictos.
- `HTTP Request` que responde 2xx/3xx aunque el cuerpo esté vacío o la URL se construyó con variables `null`.
- Mapeo de datos que produce `undefined` sin romper el flujo (ej. `{{ $json.missingField }}`).
- `Continue On Fail` habilitado en nodos críticos.

¿Cómo detectarlo antes de que se convierta en deuda operativa?
1. **Audita el historial de ejecuciones**: los nodos grises indican saltos. Si el trigger dispara pero los nodos de acción están inactivos, la lógica filtró los datos.
2. **Valida explícitamente**: añade un nodo `Code` al final que lance error si `const items = $input.all(); if (items.length === 0) throw new Error("Sin datos");`. n8n marcará fallo y detendrá el flujo.
3. **Log de rutas**: usa `If` con `console.log` o escribe a un canal de Slack/Notion con el `executionId` y el `node.name` que se ejecutó. Así confirmas si el flujo tomó la rama esperada.
4. **Compara payloads**: un nodo `Code` que verifique que el output coincida con el schema esperado antes de enviarlo a destinos externos.

El éxito de n8n es binario: ¿lanzó error? No → verde. Tu responsabilidad es añadir visibilidad a la lógica de negocio. Sin validaciones explícitas, un workflow “verde” puede ser solo un espejismo operativo.