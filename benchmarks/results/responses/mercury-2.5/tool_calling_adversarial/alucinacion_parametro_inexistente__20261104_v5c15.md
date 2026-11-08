# Mercury 2.5 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `inception/mercury-2.5`
- success: True  | final: 4.58 | quality: 2.9
- latency_total: 2.2s | tokens_per_second: 280.0
- input_tokens: 611 | output_tokens: 616
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro de consulta no soportado, no responde a la solicitud original, y carece de profundidad y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})