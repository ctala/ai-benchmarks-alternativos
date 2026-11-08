# GPT-6.1 Terra — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 4.27 | quality: 2.9
- latency_total: 1.447s | tokens_per_second: 30.4
- input_tokens: 257 | output_tokens: 44
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro de filtro inexistente, lo que no cumple con la instrucción de no inventar parámetros.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})