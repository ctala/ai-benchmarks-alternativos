# Gemma 4 26B MoE (3.8B activos) — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 4.43 | quality: 2.9
- latency_total: 0.591s | tokens_per_second: 27.1
- input_tokens: 413 | output_tokens: 16
- judge_score: 1 | justificación: La respuesta inventa un parámetro 'query' que no es parte del esquema original, lo que la hace incorrecta y irrelevante para la instrucción dada.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})