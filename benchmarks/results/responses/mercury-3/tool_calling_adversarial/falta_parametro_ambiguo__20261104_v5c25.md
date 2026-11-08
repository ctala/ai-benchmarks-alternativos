# Mercury 3 — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `inception/mercury-3`
- success: True  | final: 6.99 | quality: 5.7
- latency_total: 0.456s | tokens_per_second: 258.8
- input_tokens: 647 | output_tokens: 118
- judge_score: 3.0 | justificación: La respuesta es relevante y precisa al buscar el cliente correcto, pero no proporciona información adicional o insights más allá de la acción básica de búsqueda.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})