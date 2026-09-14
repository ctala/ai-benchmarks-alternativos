# Mercury 2.5 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `inception/mercury-2.5`
- success: True  | final: 4.73 | quality: 2.9
- latency_total: 1.659s | tokens_per_second: 437.0
- input_tokens: 763 | output_tokens: 725
- judge_score: 1 | justificación: La respuesta inventa un parámetro 'query' que no existe en el contexto dado, lo que la hace incorrecta y no relevante para la instrucción original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})