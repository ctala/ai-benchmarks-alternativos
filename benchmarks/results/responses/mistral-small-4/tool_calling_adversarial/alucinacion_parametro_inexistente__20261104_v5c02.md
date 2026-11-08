# Mistral Small 4 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 4.73 | quality: 2.9
- latency_total: 0.452s | tokens_per_second: 30.9
- input_tokens: 490 | output_tokens: 14
- judge_score: 1 | justificación: La respuesta inventa un parámetro no soportado y no aborda la solicitud original de filtrar y ordenar las facturas.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})