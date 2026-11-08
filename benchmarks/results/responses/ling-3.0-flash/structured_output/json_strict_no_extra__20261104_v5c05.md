# Ling 3.0 Flash — structured_output/json_strict_no_extra

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.25 | quality: 10.0
- latency_total: 1.776s | tokens_per_second: 15.2
- input_tokens: 101 | output_tokens: 27

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa

{"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}