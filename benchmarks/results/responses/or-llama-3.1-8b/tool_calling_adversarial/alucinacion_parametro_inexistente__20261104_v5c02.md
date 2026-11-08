# Llama 3.1 8B Instant — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 4.73 | quality: 2.9
- latency_total: 0.723s | tokens_per_second: 84.4
- input_tokens: 668 | output_tokens: 61
- judge_score: 1 | justificación: La respuesta inventa parámetros no soportados y no responde a la instrucción original, careciendo de precisión, relevancia, profundidad, claridad y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

{"name": "buscar_factura", "parameters": {"query": "F-0001; {"name": "buscar_factura", "parameters": {"query": "F-0002"}}; {"name": "buscar_cliente", "parameters": {"query": "Andes"}}