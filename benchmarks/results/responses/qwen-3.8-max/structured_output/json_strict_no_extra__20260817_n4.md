# Qwen 3.8 Max — structured_output/json_strict_no_extra

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 8.97 | quality: 10.0
- latency_total: 3.373s | tokens_per_second: 32.0
- input_tokens: 123 | output_tokens: 108

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa

{"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}