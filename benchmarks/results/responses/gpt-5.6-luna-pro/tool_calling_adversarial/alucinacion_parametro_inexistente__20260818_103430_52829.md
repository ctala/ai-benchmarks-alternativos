# GPT-5.6 Luna Pro — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 4.31 | quality: 2.9
- latency_total: 4.183s | tokens_per_second: 61.7
- input_tokens: 2376 | output_tokens: 258
- judge_score: 1 | justificación: La respuesta inventa un parámetro no soportado ('buscar_cliente') y no aborda la instrucción original de buscar facturas impagas ordenadas por monto, lo que resulta en una baja precisión, relevancia y profundidad.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

**Exploring invoice retrieval**

I need to figure out how to search for client information and invoices. The tools I have only let me access invoices by their number, not a complete list. Searching by customer could give me their account status and possibly their invoices, so I should use the function buscar_cliente for this. Let's see if I can gather what I need by going through the customer data first!