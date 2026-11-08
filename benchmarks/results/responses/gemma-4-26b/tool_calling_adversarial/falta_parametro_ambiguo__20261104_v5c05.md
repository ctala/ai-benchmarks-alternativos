# Gemma 4 26B MoE (3.8B activos) — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 6.24 | quality: 5.7
- latency_total: 1.115s | tokens_per_second: 15.3
- input_tokens: 415 | output_tokens: 17
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al buscar el cliente correcto, pero no proporciona información adicional o insights más allá de la acción de búsqueda.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})