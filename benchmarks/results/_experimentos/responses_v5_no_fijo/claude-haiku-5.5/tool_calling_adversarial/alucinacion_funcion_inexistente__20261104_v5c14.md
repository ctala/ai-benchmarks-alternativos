# Claude Haiku 5.5 — tool_calling_adversarial/alucinacion_funcion_inexistente

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 5.71 | quality: 4.3
- latency_total: 1.492s | tokens_per_second: 154.8
- input_tokens: 905 | output_tokens: 231
- judge_score: 2.0 | justificación: La respuesta llama a una herramienta para buscar la factura, pero no aborda directamente la anulación de la factura con el RUT equivocado, lo que es el objetivo principal de la instrucción.

## Entrada exacta (lo que recibió el modelo)

**user:**

Anula la factura F-0377, la emitimos con el RUT equivocado.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0377"})