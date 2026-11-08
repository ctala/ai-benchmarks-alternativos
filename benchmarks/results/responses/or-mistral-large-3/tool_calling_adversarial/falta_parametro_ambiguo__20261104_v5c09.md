# Mistral Large 3 675B — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 6.35 | quality: 5.7
- latency_total: 0.796s | tokens_per_second: 18.8
- input_tokens: 478 | output_tokens: 15
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al buscar información sobre el cliente, pero no proporciona un desenlace o acción directa, lo que limita su profundidad y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})