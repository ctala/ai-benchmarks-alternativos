# GPT-5.6 Terra — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 4.11 | quality: 2.9
- latency_total: 1.705s | tokens_per_second: 24.6
- input_tokens: 257 | output_tokens: 42
- judge_score: 1 | justificación: La respuesta no es precisa ni relevante, ya que inventa un parámetro 'query' que no existe en el contexto dado. No aborda la solicitud de buscar facturas impagas del cliente Andes, ni proporciona ninguna estructura o insight útil.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})