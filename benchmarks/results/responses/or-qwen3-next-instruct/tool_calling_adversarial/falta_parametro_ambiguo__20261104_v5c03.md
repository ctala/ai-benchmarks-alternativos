# Qwen 3-Next 80B Instruct — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 6.54 | quality: 5.7
- latency_total: 0.51s | tokens_per_second: 45.1
- input_tokens: 542 | output_tokens: 23
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al buscar información sobre el cliente, pero no proporciona una solución directa o desambigua entre los clientes posibles, lo que limita su profundidad y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})