# GPT-4.1 Mini — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `gpt-4.1-mini`
- success: True  | final: 4.43 | quality: 2.9
- latency_total: 0.88s | tokens_per_second: 18.2
- input_tokens: 252 | output_tokens: 16
- judge_score: 1 | justificación: La respuesta no es precisa ni relevante ya que inventa un parámetro de consulta ('buscar_cliente') que no está soportado por el esquema, ignorando la instrucción de buscar facturas impagas ordenadas por monto para el cliente Andes.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})