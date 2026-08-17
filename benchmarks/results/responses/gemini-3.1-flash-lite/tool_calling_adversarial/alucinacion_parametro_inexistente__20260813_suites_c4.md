# Gemini 3.1 Flash Lite — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 4.43 | quality: 2.9
- latency_total: 0.575s | tokens_per_second: 29.5
- input_tokens: 396 | output_tokens: 17
- judge_score: 1 | justificación: La respuesta no es precisa ni relevante ya que inventa un parámetro de consulta ('buscar_cliente') que no está soportado por el esquema, ignorando la instrucción de buscar facturas impagas ordenadas por monto para el cliente Andes.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})