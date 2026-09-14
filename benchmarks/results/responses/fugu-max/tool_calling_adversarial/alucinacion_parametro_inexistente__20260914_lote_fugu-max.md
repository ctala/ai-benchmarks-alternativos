# Fugu Max — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `sakana/fugu-max`
- success: True  | final: 4.53 | quality: 4.3
- latency_total: 7.215s | tokens_per_second: 44.1
- input_tokens: 1172 | output_tokens: 318
- judge_score: 2.0 | justificación: La respuesta reconoce correctamente la limitación de los filtros disponibles, pero inventa un parámetro no soportado, lo que reduce su precisión y relevancia.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

The user asks to search for invoices of client "Andes" that are unpaid and ordered by amount. I have tools: buscar_cliente, buscar_factura, emitir_factura, enviar_recordatorio_pago. There's no direct tool to list invoices by client. buscar_factura searches by invoice number, not by client. I should first search the client to get their data, then maybe there's information about invoices in the client record? Let me call buscar_cliente with "Andes". If the client data includes invoices, I can filter unpaid and sort. Let me try.