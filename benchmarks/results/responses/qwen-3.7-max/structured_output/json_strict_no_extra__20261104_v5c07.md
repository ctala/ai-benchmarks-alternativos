# Qwen 3.7 Max — structured_output/json_strict_no_extra

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 8.93 | quality: 10.0
- latency_total: 2.051s | tokens_per_second: 12.2
- input_tokens: 87 | output_tokens: 25

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa

{"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}