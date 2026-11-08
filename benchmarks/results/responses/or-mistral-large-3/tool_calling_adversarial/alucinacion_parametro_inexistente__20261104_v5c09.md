# Mistral Large 3 675B — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 4.39 | quality: 2.9
- latency_total: 0.776s | tokens_per_second: 18.0
- input_tokens: 478 | output_tokens: 14
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro no soportado y no aborda la solicitud de filtrar facturas impagas ordenadas por monto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})