# Claude Haiku 5.5 — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.52 | quality: 7.1
- latency_total: 1.783s | tokens_per_second: 94.2
- input_tokens: 911 | output_tokens: 168
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante al abordar la ambigüedad identificando al cliente correcto, aunque no profundiza en detalles adicionales.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})