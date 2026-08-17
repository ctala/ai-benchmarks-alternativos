# Llama 3.1 8B Instant — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `meta-llama/llama-3.1-8b-instruct`
- success: True  | final: 4.73 | quality: 2.9
- latency_total: 0.665s | tokens_per_second: 91.8
- input_tokens: 668 | output_tokens: 61
- judge_score: 1 | justificación: La respuesta es incorrecta y no relevante, ya que inventa parámetros y estructuras que no existen en el esquema, como 'F-0010' y 'F-0011', y no aborda la solicitud de filtrar facturas impagas y ordenarlas por monto. La respuesta es confusa y no ofrece utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

{"name": "buscar_factura", "parameters": {"query": "F-0010; {"name": "buscar_factura", "parameters": {"query": "F-0011"}}; {"name": "buscar_cliente", "parameters": {"query": "Andes"}}