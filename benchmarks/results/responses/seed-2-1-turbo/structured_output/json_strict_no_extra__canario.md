# Seed 2.1 Turbo — structured_output/json_strict_no_extra

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 9.07 | quality: 10.0
- latency_total: 4.343s | tokens_per_second: 17.7
- input_tokens: 110 | output_tokens: 77

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa

{"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}