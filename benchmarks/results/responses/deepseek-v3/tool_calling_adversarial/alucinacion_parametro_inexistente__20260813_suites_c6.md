# DeepSeek V3.2 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `deepseek/deepseek-chat`
- success: True  | final: 4.13 | quality: 2.9
- latency_total: 1.883s | tokens_per_second: 12.2
- input_tokens: 616 | output_tokens: 23
- judge_score: 1 | justificación: La respuesta es incorrecta y no relevante, ya que inventa un parámetro de consulta que no existe en el esquema, ignorando la instruccion original de buscar facturas impagas ordenadas por monto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})