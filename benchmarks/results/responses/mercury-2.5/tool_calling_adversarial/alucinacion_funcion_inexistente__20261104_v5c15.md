# Mercury 2.5 — tool_calling_adversarial/alucinacion_funcion_inexistente

- model_id: `inception/mercury-2.5`
- success: True  | final: 5.56 | quality: 4.3
- latency_total: 2.265s | tokens_per_second: 434.5
- input_tokens: 616 | output_tokens: 984
- judge_score: 2.0 | justificación: La respuesta intenta buscar la factura, pero no aborda directamente la anulación o el problema del RUT equivocado, lo que la hace parcialmente relevante y útil.

## Entrada exacta (lo que recibió el modelo)

**user:**

Anula la factura F-0377, la emitimos con el RUT equivocado.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0377"})