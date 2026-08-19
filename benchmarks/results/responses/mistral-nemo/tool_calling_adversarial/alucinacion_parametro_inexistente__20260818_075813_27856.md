# Mistral Nemo — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `mistralai/mistral-nemo`
- success: True  | final: 4.58 | quality: 2.9
- latency_total: 0.701s | tokens_per_second: 31.4
- input_tokens: 478 | output_tokens: 22
- judge_score: 1 | justificación: La respuesta inventa un parámetro 'query' que no está soportado, lo que la hace incorrecta y no relevante para la instrucción original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "andes"})