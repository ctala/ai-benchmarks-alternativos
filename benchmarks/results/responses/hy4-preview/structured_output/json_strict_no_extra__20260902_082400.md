# Tencent Hy4 preview — structured_output/json_strict_no_extra

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.95 | quality: 10.0
- latency_total: 7.153s | tokens_per_second: 50.6
- input_tokens: 98 | output_tokens: 362

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa

{"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}