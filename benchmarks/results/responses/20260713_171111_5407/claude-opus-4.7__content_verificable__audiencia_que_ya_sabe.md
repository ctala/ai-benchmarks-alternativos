# Claude Opus 4.7 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-opus-4-7`
- success: True  | final: 8.16 | quality: 10.0
- latency_total: 15.443s | tokens_per_second: 45.7
- input_tokens: 164 | output_tokens: 706
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

# Cuando "success" es mentira: workflows fantasma en n8n

Todos hemos vivido esto: el workflow marca verde, el log dice "success", el cliente pregunta por qué su CRM está vacío. Bienvenido al reino de los ejecuciones fantasma.

El problema casi nunca está en n8n. Está en que confundimos "el nodo ejecutó sin lanzar excepción" con "el nodo hizo lo que yo esperaba". Un HTTP Request que recibe un 200 con `{"error":"quota exceeded"}` es un éxito para n8n. Un Set que procesa `items: []` termina en verde sin haber tocado un solo dato. Un IF cuya rama true nunca se cumple deja la ejecución perfecta... y vacía.

**Los sospechosos habituales:**

- **Loops sobre arrays vacíos.** Split In Batches con cero items no falla, simplemente no itera. Si tu upstream devolvió `[]`, todo lo de abajo es teatro.
- **APIs que responden 200 con error en el body.** Stripe, HubSpot y medio mundo lo hacen. El status code no te salva.
- **Merge en modo wait.** Si una rama no llega, el workflow puede terminar sin que la otra se haya combinado nunca.
- **Expresiones que resuelven a undefined silenciosamente.** `{{$json.user.email}}` cuando no hay user devuelve vacío, no error.

**Cómo detectarlo antes que el cliente:**

Añade un nodo final de "assertion" que valide invariantes: ¿cuántos items esperaba procesar? ¿el ID de retorno de la API existe? Si falla, throw explícito. Complementa con un webhook de heartbeat que registre en una tabla externa `run_id`, `items_in`, `items_out`, `records_written`. Con esos tres números puedes hacer alertas de "workflow ejecutó pero output=0" en Grafana o un simple cron de auditoría.

El verde no es verdad. La verdad son los conteos.