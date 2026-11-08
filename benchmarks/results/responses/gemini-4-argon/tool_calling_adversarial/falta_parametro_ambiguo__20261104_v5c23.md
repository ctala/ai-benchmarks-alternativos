# Gemini 4 Argon — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `google/gemini-4-argon`
- success: True  | final: 5.62 | quality: 5.7
- latency_total: 3.292s | tokens_per_second: 7.0
- input_tokens: 443 | output_tokens: 23
- judge_score: 3.0 | justificación: La respuesta es correcta y relevante al buscar al cliente 'Rodríguez', pero no resuelve la ambigüedad ni emite la factura, lo que limita su profundidad y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Rodríguez"})