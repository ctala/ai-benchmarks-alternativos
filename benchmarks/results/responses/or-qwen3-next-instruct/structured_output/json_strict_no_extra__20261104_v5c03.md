# Qwen 3-Next 80B Instruct — structured_output/json_strict_no_extra

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.85 | quality: 10.0
- latency_total: 0.488s | tokens_per_second: 53.2
- input_tokens: 85 | output_tokens: 26

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa

{"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}