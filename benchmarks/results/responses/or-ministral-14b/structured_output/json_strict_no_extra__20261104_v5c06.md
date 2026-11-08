# Ministral 14B — structured_output/json_strict_no_extra

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 6.6 | quality: 6.0
- latency_total: 1.761s | tokens_per_second: 40.3
- input_tokens: 78 | output_tokens: 71

## Entrada exacta (lo que recibió el modelo)

**system:**

IMPORTANTE: Tu respuesta debe ser UNICAMENTE JSON valido. NO incluyas ```json, NO incluyas explicaciones antes o despues, NO incluyas comentarios. Solo el JSON puro.

**user:**

Devuelve: {"status": "ok", "count": 42, "items": ["alpha", "beta", "gamma"]}


## Respuesta completa

```json
{
  "status": "ok",
  "count": 42,
  "items": [
    "alpha",
    "beta",
    "gamma"
  ]
}
```{
  "status": "ok",
  "count": 42,
  "items": ["alpha", "beta", "gamma"]
}