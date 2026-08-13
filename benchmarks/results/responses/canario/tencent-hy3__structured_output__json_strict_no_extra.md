# Tencent Hy3 — structured_output/json_strict_no_extra

- model_id: `tencent/hy3`
- success: True  | final: 9.25 | quality: 10.0
- latency_total: 3.756s | tokens_per_second: 31.4
- input_tokens: 91 | output_tokens: 118

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa

{"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}