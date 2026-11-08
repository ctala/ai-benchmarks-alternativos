# Mercury 2.5 — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `inception/mercury-2.5`
- success: True  | final: 6.69 | quality: 5.7
- latency_total: 1.976s | tokens_per_second: 246.5
- input_tokens: 636 | output_tokens: 487
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al buscar el cliente correcto, pero no proporciona información adicional o insights más allá de la acción básica de búsqueda.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})