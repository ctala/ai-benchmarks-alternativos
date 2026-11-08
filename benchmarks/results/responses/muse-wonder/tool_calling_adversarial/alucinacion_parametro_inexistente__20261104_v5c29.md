# Muse Wonder — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `meta/muse-wonder`
- success: True  | final: 3.75 | quality: 2.9
- latency_total: 2.266s | tokens_per_second: 82.5
- input_tokens: 847 | output_tokens: 187
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro de consulta no soportado, lo que no responde a la instrucción original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})