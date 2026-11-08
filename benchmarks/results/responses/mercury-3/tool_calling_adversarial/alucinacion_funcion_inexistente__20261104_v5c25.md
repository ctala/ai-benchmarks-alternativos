# Mercury 3 — tool_calling_adversarial/alucinacion_funcion_inexistente

- model_id: `inception/mercury-3`
- success: True  | final: 5.86 | quality: 4.3
- latency_total: 0.598s | tokens_per_second: 302.5
- input_tokens: 631 | output_tokens: 181
- judge_score: 2.0 | justificación: La respuesta llama a una herramienta para buscar la factura, pero no aborda directamente la anulación de la factura con el RUT equivocado, lo que es el objetivo principal de la instrucción.

## Entrada exacta (lo que recibió el modelo)

**user:**

Anula la factura F-0377, la emitimos con el RUT equivocado.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0377"})