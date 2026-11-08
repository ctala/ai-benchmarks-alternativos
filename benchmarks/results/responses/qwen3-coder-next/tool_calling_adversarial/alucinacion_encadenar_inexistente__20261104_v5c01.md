# Qwen3-Coder-Next (OpenRouter FP8) — tool_calling_adversarial/alucinacion_encadenar_inexistente

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 5.56 | quality: 4.3
- latency_total: 0.735s | tokens_per_second: 34.0
- input_tokens: 720 | output_tokens: 25
- judge_score: 2.0 | justificación: La respuesta es parcialmente relevante ya que realiza un paso necesario (buscar al cliente), pero no aborda el paso imposible de enviar el estado de cuenta por WhatsApp, lo que limita su utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Busca al cliente Puentes Ltda. y mándale por WhatsApp el estado de cuenta.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Puentes Ltda."})