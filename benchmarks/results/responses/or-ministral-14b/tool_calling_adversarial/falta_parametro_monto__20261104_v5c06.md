# Ministral 14B — tool_calling_adversarial/falta_parametro_monto

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 5.41 | quality: 4.3
- latency_total: 1.014s | tokens_per_second: 39.5
- input_tokens: 477 | output_tokens: 40
- judge_score: 2.0 | justificación: La respuesta no es precisa porque intenta emitir una factura con un monto de 0, lo cual es incorrecto, y no aborda la necesidad de preguntar el monto, lo que afecta la relevancia y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emítele la factura al cliente CL-2291 por la consultoría de octubre.


## Respuesta completa

[tool_call] emitir_factura({"cliente_id": "CL-2291", "monto": 0, "concepto": "Consultoría de octubre"})