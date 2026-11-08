# Nemotron 3 Super — structured_output/json_strict_no_extra

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 9.85 | quality: 10.0
- latency_total: 0.397s | tokens_per_second: 67.9
- input_tokens: 89 | output_tokens: 27

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa

{"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}