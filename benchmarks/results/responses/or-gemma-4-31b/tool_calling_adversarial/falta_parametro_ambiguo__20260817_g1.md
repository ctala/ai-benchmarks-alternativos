# Gemma 4 31B — tool_calling_adversarial/falta_parametro_ambiguo

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 4.63 | quality: 3.18
- latency_total: 0.731s | tokens_per_second: 23.3
- input_tokens: 415 | output_tokens: 17
- judge_score: 1.2 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Emite la factura de siempre para Rodríguez, $450.000 por el mantenimiento.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Rodríguez"})