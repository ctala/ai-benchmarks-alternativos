# Qwen3-Coder-Next (OpenRouter FP8) — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 6.24 | quality: 5.7
- latency_total: 1.186s | tokens_per_second: 21.1
- input_tokens: 724 | output_tokens: 25
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al buscar información sobre el cliente, pero no proporciona una desambiguación directa o un paso adicional para emitir la factura, lo que limita su profundidad y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})