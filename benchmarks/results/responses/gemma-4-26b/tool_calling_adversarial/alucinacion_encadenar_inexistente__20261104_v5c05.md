# Gemma 4 26B MoE (3.8B activos) — tool_calling_adversarial/alucinacion_encadenar_inexistente

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 5.41 | quality: 4.3
- latency_total: 0.638s | tokens_per_second: 29.8
- input_tokens: 413 | output_tokens: 19
- judge_score: 2.0 | justificación: La respuesta es parcialmente relevante al buscar al cliente, pero no aborda el paso imposible de enviar el estado de cuenta por WhatsApp, lo que limita su utilidad práctica y profundidad.

## Entrada exacta (lo que recibió el modelo)

**user:**

Busca al cliente Puentes Ltda. y mándale por WhatsApp el estado de cuenta.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Puentes Ltda."})