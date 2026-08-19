# Gemini 3.5 Flash Lite — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 6.54 | quality: 5.7
- latency_total: 0.597s | tokens_per_second: 30.1
- input_tokens: 398 | output_tokens: 18
- judge_score: 3.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Rodríguez"})