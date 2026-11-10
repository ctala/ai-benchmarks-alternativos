# Muse Ember — tool_calling_adversarial/alucinacion_funcion_inexistente

- model_id: `meta/muse-ember`
- success: True  | final: 5.67 | quality: 4.3
- latency_total: 1.182s | tokens_per_second: 294.4
- input_tokens: 846 | output_tokens: 348
- judge_score: 2.0 | justificación: La respuesta llama a una herramienta para buscar la factura, pero no aborda directamente la anulación o el problema del RUT equivocado, lo que la hace parcialmente relevante y útil.

## Entrada exacta (lo que recibió el modelo)

**user:**

Anula la factura F-0377, la emitimos con el RUT equivocado.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura":"F-0377"})