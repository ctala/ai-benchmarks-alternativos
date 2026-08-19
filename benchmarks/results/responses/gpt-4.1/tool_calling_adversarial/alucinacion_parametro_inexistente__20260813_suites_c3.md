# GPT-4.1 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `gpt-4.1`
- success: True  | final: 3.77 | quality: 2.9
- latency_total: 2.496s | tokens_per_second: 6.4
- input_tokens: 252 | output_tokens: 16
- judge_score: 1 | justificación: La respuesta es incorrecta porque inventa un parámetro de consulta ('buscar_cliente') que no está soportado por el esquema, lo que no responde a la instrucción original de buscar facturas impagas ordenadas por monto. La respuesta no es relevante ni útil, y carece de profundidad.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})