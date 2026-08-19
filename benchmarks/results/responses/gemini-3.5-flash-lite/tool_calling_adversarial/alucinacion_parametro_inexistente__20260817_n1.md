# Gemini 3.5 Flash Lite — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 4.43 | quality: 2.9
- latency_total: 0.612s | tokens_per_second: 27.8
- input_tokens: 396 | output_tokens: 17
- judge_score: 1 | justificación: La respuesta inventa un parámetro 'query' que no existe en el esquema, lo que la hace incorrecta y no relevante para la instrucción dada.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})