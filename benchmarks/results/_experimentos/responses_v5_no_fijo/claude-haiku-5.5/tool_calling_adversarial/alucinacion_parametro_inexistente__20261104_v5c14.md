# Claude Haiku 5.5 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 4.73 | quality: 2.9
- latency_total: 1.362s | tokens_per_second: 124.9
- input_tokens: 910 | output_tokens: 170
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro de consulta no soportado, no responde a la solicitud original, y carece de profundidad y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})