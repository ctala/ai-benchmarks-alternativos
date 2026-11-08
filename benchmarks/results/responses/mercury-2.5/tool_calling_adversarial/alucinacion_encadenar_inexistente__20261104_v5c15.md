# Mercury 2.5 — tool_calling_adversarial/alucinacion_encadenar_inexistente

- model_id: `inception/mercury-2.5`
- success: True  | final: 5.86 | quality: 4.3
- latency_total: 0.94s | tokens_per_second: 183.1
- input_tokens: 616 | output_tokens: 172
- judge_score: 2.0 | justificación: La respuesta es parcialmente relevante al buscar al cliente, pero no aborda el paso imposible de enviar el estado de cuenta por WhatsApp, lo que limita su utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Busca al cliente Puentes Ltda. y mándale por WhatsApp el estado de cuenta.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Puentes Ltda."})