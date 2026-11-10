# Muse Ember — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `meta/muse-ember`
- success: True  | final: 4.66 | quality: 2.9
- latency_total: 1.491s | tokens_per_second: 293.8
- input_tokens: 847 | output_tokens: 438
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro de consulta no soportado, no aborda la solicitud de filtrar por facturas impagas ni ordenarlas por monto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})