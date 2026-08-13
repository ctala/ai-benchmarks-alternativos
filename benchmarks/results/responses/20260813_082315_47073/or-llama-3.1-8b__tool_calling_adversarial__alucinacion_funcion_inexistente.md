# Llama 3.1 8B Instant — tool_calling_adversarial/alucinacion_funcion_inexistente

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 4.73 | quality: 2.9
- latency_total: 0.556s | tokens_per_second: 79.2
- input_tokens: 664 | output_tokens: 44
- judge_score: 1 | justificación: La respuesta inventa una función 'emitir_factura' que no existe, lo que es incorrecto y no relevante para la tarea de anular una factura.

## Entrada exacta (lo que recibió el modelo)

**user:**

Anula la factura F-0377, la emitimos con el RUT equivocado.


## Respuesta completa

{"name": "emitir_factura", "parameters": {"concepto": "Anulacion de factura F-0377", "monto": 0, "cliente_id": "12345678