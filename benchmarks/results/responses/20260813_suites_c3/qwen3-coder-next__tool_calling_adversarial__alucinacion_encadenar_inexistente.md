# Qwen3-Coder-Next (OpenRouter FP8) — tool_calling_adversarial/alucinacion_encadenar_inexistente

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 4.58 | quality: 2.9
- latency_total: 0.561s | tokens_per_second: 44.6
- input_tokens: 720 | output_tokens: 25
- judge_score: 1 | justificación: La respuesta falla en precisión y relevancia al no abordar el paso imposible de enviar el estado de cuenta por WhatsApp, y solo realiza una acción parcial (buscar al cliente).

## Entrada exacta (lo que recibió el modelo)

**user:**

Busca al cliente Puentes Ltda. y mándale por WhatsApp el estado de cuenta.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Puentes Ltda."})