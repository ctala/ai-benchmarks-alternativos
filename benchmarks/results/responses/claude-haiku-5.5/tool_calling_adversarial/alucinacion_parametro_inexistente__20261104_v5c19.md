# Claude Haiku 5.5 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 4.73 | quality: 2.9
- latency_total: 1.32s | tokens_per_second: 117.4
- input_tokens: 910 | output_tokens: 155
- judge_score: 1 | justificación: La respuesta inventa un parámetro de consulta que no existe en el esquema, lo que la hace incorrecta y no relevante para la instrucción dada.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})