# Qwen3-Coder-Next (OpenRouter FP8) — tool_calling_adversarial/confundible_verbo_enganoso

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.52 | quality: 7.1
- latency_total: 0.671s | tokens_per_second: 46.2
- input_tokens: 731 | output_tokens: 31
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, identificando correctamente la acción de buscar la factura específica. Aunque no ofrece profundidad adicional o insights, está claramente estructurada y es directamente útil para un emprendedor que necesita acceder a información de facturación.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0398"})