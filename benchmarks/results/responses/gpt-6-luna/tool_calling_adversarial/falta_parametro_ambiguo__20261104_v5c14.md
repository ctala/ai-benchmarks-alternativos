# GPT-6 Luna — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `openai/gpt-6-luna`
- success: True  | final: 6.39 | quality: 5.7
- latency_total: 1.586s | tokens_per_second: 42.2
- input_tokens: 255 | output_tokens: 67
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al buscar el cliente correcto, pero no proporciona información adicional o insights más allá de la acción de búsqueda.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Rodríguez"})