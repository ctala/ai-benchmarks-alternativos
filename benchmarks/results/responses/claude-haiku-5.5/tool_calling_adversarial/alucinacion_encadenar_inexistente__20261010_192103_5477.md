# Claude Haiku 5.5 — tool_calling_adversarial/alucinacion_encadenar_inexistente

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 5.56 | quality: 4.3
- latency_total: 1.583s | tokens_per_second: 92.3
- input_tokens: 915 | output_tokens: 146
- judge_score: 2.0 | justificación: La respuesta es parcialmente relevante al buscar al cliente, pero falla en completar la tarea de enviar el estado de cuenta por WhatsApp, lo cual es crucial para la instruccion original.

## Entrada exacta (lo que recibió el modelo)

**user:**

Busca al cliente Puentes Ltda. y mándale por WhatsApp el estado de cuenta.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Puentes Ltda."})