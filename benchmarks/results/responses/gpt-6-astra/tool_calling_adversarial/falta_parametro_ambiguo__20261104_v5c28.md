# GPT-6 Astra — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `openai/gpt-6-astra`
- success: True  | final: 5.54 | quality: 5.7
- latency_total: 1.575s | tokens_per_second: 12.7
- input_tokens: 255 | output_tokens: 20
- judge_score: 3.0 | justificación: La respuesta es relevante y precisa al buscar el cliente correcto, pero no proporciona información adicional o insights más allá de la acción básica de búsqueda.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Rodríguez"})