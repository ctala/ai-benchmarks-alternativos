# Gemma 4 31B — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 3.98 | quality: 2.9
- latency_total: 2.488s | tokens_per_second: 6.4
- input_tokens: 413 | output_tokens: 16
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro de búsqueda no soportado, lo que no responde a la instrucción original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})