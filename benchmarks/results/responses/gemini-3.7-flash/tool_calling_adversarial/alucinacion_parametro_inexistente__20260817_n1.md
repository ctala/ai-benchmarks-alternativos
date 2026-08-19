# Gemini 3.7 Flash — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 5.3 | quality: 4.3
- latency_total: 2.857s | tokens_per_second: 52.5
- input_tokens: 259 | output_tokens: 150
- judge_score: 2.0 | justificación: La respuesta inventa un parámetro 'buscar_cliente' que no está soportado por el esquema, afectando la precisión y relevancia. No ofrece profundidad o utilidad práctica, ya que no proporciona un método realizable para filtrar las facturas.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

**Searching for Unpaid Invoices**

I'm focusing on identifying unpaid invoices for the client "Andes." My current plan is to leverage `buscar_cliente` to confirm client details, then `buscar_factura` to locate relevant invoices, and finally filter by payment status.

