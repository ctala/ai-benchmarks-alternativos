# GPT-5.4 Mini — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `gpt-5.4-mini`
- success: True  | final: 4.43 | quality: 2.9
- latency_total: 0.707s | tokens_per_second: 26.9
- input_tokens: 257 | output_tokens: 19
- judge_score: 1 | justificación: La respuesta es incorrecta porque inventa un comando de herramienta que no está relacionado con la instrucción original. La instrucción solicitaba filtrar y ordenar facturas impagas para un cliente específico, pero la respuesta proporciona un comando de búsqueda de cliente sin abordar el filtro de estado de pago o el ordenamiento por monto.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})