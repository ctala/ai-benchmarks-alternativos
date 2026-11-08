# GPT-6 Astra — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `openai/gpt-6-astra`
- success: True  | final: 3.58 | quality: 2.9
- latency_total: 1.595s | tokens_per_second: 11.9
- input_tokens: 257 | output_tokens: 19
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro de herramienta no soportado y no aborda la solicitud de filtrar facturas impagas ordenadas por monto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})