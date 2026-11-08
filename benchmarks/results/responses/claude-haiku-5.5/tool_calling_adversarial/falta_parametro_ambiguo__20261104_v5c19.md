# Claude Haiku 5.5 — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 6.54 | quality: 5.7
- latency_total: 1.712s | tokens_per_second: 95.8
- input_tokens: 911 | output_tokens: 164
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al buscar el cliente correcto, pero carece de profundidad ya que no resuelve la ambigüedad por sí misma ni proporciona insights adicionales.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})