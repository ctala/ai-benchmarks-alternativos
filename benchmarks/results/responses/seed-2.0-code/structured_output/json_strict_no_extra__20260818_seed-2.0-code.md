# Seed 2.0 Code — structured_output/json_strict_no_extra

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 1.524s | tokens_per_second: 34.1
- input_tokens: 110 | output_tokens: 52

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa

{"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}