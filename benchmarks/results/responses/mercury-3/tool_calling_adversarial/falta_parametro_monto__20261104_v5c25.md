# Mercury 3 — tool_calling_adversarial/falta_parametro_monto

- model_id: `inception/mercury-3`
- success: True  | final: 5.86 | quality: 4.3
- latency_total: 0.515s | tokens_per_second: 174.9
- input_tokens: 634 | output_tokens: 90
- judge_score: 2.0 | justificación: La respuesta es relevante al buscar información sobre el cliente, pero no aborda directamente la necesidad de preguntar el monto para emitir la factura, lo que es crucial en este contexto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emítele la factura al cliente CL-2291 por la consultoría de octubre.


## Respuesta completa

[tool_call] buscar_cliente({"query": "CL-2291"})