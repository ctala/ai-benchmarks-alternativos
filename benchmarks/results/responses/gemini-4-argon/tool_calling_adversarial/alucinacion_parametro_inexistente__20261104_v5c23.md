# Gemini 4 Argon — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `google/gemini-4-argon`
- success: True  | final: 3.66 | quality: 2.9
- latency_total: 3.737s | tokens_per_second: 6.2
- input_tokens: 440 | output_tokens: 23
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro de herramienta no soportado, no aborda la solicitud de filtrar facturas impagas y ordenarlas por monto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})