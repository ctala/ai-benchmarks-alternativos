# GPT-5.4 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `gpt-5.4`
- success: True  | final: 3.74 | quality: 2.9
- latency_total: 1.35s | tokens_per_second: 14.1
- input_tokens: 257 | output_tokens: 19
- judge_score: 1 | justificación: La respuesta es incorrecta y no relevante porque el modelo generó una llamada de herramienta que busca un cliente en lugar de filtrar facturas impagas para el cliente Andes, lo cual no responde a la instrucción original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})