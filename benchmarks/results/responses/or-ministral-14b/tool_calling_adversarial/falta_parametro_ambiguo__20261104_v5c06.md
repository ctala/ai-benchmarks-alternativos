# Ministral 14B — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 6.39 | quality: 5.7
- latency_total: 0.675s | tokens_per_second: 22.2
- input_tokens: 478 | output_tokens: 15
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al buscar información sobre el cliente, pero no proporciona una solución directa o desambigua entre clientes posibles, lo que limita su profundidad y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})