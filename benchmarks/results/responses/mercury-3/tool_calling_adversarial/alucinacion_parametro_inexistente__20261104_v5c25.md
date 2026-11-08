# Mercury 3 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `inception/mercury-3`
- success: True  | final: 4.88 | quality: 2.9
- latency_total: 0.64s | tokens_per_second: 306.3
- input_tokens: 634 | output_tokens: 196
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro de búsqueda no soportado, lo que no responde a la instrucción original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})