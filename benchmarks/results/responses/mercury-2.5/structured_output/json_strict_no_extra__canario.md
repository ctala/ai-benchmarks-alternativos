# Mercury 2.5 — structured_output/json_strict_no_extra

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.7 | quality: 10.0
- latency_total: 1.143s | tokens_per_second: 349.1
- input_tokens: 95 | output_tokens: 399

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa



{"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}