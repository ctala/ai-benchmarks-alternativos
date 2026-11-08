# Gemini 3.5 Flash Lite — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 4.43 | quality: 2.9
- latency_total: 0.941s | tokens_per_second: 18.1
- input_tokens: 261 | output_tokens: 17
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro de filtro no soportado por el esquema, lo que la hace irrelevante y de poca utilidad.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})