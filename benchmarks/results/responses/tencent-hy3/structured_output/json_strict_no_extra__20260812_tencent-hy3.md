# Tencent Hy3 — structured_output/json_strict_no_extra

- model_id: `tencent/hy3`
- success: True  | final: 8.95 | quality: 10.0
- latency_total: 6.851s | tokens_per_second: 22.0
- input_tokens: 91 | output_tokens: 151

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa

{"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}