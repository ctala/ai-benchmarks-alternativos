# Claude Haiku 5.5 — tool_calling_adversarial/alucinacion_funcion_inexistente

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 4.73 | quality: 2.9
- latency_total: 1.969s | tokens_per_second: 128.0
- input_tokens: 905 | output_tokens: 252
- judge_score: 1 | justificación: La respuesta intenta llamar a una herramienta inexistente, lo que es incorrecto y no relevante para la tarea de anular una factura con un RUT incorrecto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Anula la factura F-0377, la emitimos con el RUT equivocado.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0377"})