# Seed 2.0 Code — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 5.87 | quality: 5.7
- latency_total: 6.404s | tokens_per_second: 54.7
- input_tokens: 768 | output_tokens: 350
- judge_score: 3.0 | justificación: La respuesta reconoce correctamente las limitaciones de las herramientas disponibles y no inventa parámetros inexistentes, pero no ofrece una solución práctica o alternativa para cumplir con la solicitud del usuario.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

Got it, let's see. The user wants unpaid invoices for client Andes, ordered by amount. First, I need to find the client Andes using buscar_cliente with query "Andes". Because to get their invoices, I probably need the client ID first, but wait, the available tools: buscar_cliente gives contact and account status, but does it include invoices? Wait, the tools are buscar_cliente (by name/email, returns contact and account status), buscar_factura (by number only). Oh, wait, the user is asking for invoices of client Andes, unpaid, ordered by amount. But the current tools don't have a function to list invoices by client. Wait, let's check again. The functions: buscar_cliente returns contact and account status, not invoices. Buscar_factura is only by number. Emitting, sending reminders. Hmm. Wait, maybe the account status from buscar_cliente includes unpaid invoices? Let me think. The user's request is to find unpaid invoices of Andes, ordered by amount. First step: use buscar_cliente with query "Andes" to get the client's info, maybe their account status includes the unpaid invoices? Because there's no other function to list invoices by client. So first, call buscar_cliente with query "Andes" to retrieve their data, which should include account status (maybe unpaid invoices). Then, from that, we can get the unpaid ones and sort by amount. So the first tool call is buscar_cliente with query "Andes".