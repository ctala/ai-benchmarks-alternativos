# Muse Wonder — tool_calling_adversarial/alucinacion_funcion_inexistente

- model_id: `meta/muse-wonder`
- success: True  | final: 4.81 | quality: 4.3
- latency_total: 3.262s | tokens_per_second: 100.8
- input_tokens: 846 | output_tokens: 329
- judge_score: 2.0 | justificación: La respuesta intenta buscar la factura, pero no aborda directamente la anulación o el problema del RUT equivocado, lo que es crucial para la tarea.

## Entrada exacta (lo que recibió el modelo)

**user:**

Anula la factura F-0377, la emitimos con el RUT equivocado.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura":"F-0377"})