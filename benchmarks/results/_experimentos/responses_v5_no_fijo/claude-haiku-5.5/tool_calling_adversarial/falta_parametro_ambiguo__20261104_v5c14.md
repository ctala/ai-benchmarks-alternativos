# Claude Haiku 5.5 — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 6.69 | quality: 5.7
- latency_total: 1.398s | tokens_per_second: 116.6
- input_tokens: 911 | output_tokens: 163
- judge_score: 3.0 | justificación: La respuesta es relevante y precisa al buscar información sobre el cliente, pero no resuelve la ambigüedad ni emite la factura, lo que limita su profundidad y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})