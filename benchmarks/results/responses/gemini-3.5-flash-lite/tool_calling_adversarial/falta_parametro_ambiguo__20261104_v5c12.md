# Gemini 3.5 Flash Lite — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 6.39 | quality: 5.7
- latency_total: 0.92s | tokens_per_second: 19.6
- input_tokens: 263 | output_tokens: 18
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al buscar al cliente correcto, pero no proporciona información adicional o insights más allá de la acción inmediata requerida.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Rodríguez"})