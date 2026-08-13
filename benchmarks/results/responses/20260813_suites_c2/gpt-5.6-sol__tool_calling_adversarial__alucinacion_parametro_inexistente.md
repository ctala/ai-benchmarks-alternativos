# GPT-5.6 Sol — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 3.49 | quality: 2.9
- latency_total: 3.236s | tokens_per_second: 14.5
- input_tokens: 257 | output_tokens: 47
- judge_score: 1 | justificación: La respuesta es incorrecta porque inventa un parámetro 'query' que no existe en el contexto dado. No responde a la instrucción original de buscar facturas impagas del cliente Andes ordenadas por monto, y en su lugar realiza una llamada de herramienta incorrecta.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})