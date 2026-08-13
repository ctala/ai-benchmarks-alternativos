# Qwen3 Coder — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `qwen/qwen3-coder`
- success: True  | final: 4.94 | quality: 4.3
- latency_total: 4.715s | tokens_per_second: 5.1
- input_tokens: 721 | output_tokens: 24
- judge_score: 2.0 | justificación: La respuesta es aceptablemente precisa al buscar al cliente Rodríguez, pero no resuelve la ambigüedad inicial de múltiples clientes posibles, lo que la hace menos relevante. No ofrece profundidad o insights adicionales, y aunque está clara, su utilidad práctica es limitada ya que no resuelve el problema de desambiguación.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodr\u00edguez"})