# Nex-N2-Mini — structured_output/json_strict_no_extra

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 0.607s | tokens_per_second: 36.2
- input_tokens: 84 | output_tokens: 22

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa

{"status":"ok","count":42,"items":["alpha","beta","gamma"]}