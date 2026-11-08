# GPT-6 Astra — tool_calling_adversarial/alucinacion_funcion_inexistente

- model_id: `openai/gpt-6-astra`
- success: True  | final: 4.7 | quality: 4.3
- latency_total: 1.425s | tokens_per_second: 16.8
- input_tokens: 257 | output_tokens: 24
- judge_score: 2.0 | justificación: La respuesta llama a una herramienta para buscar la factura, pero no aborda directamente la anulación de la factura con el RUT equivocado, lo que es el objetivo principal de la instrucción.

## Entrada exacta (lo que recibió el modelo)

**user:**

Anula la factura F-0377, la emitimos con el RUT equivocado.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura":"F-0377"})