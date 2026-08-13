# Llama 4 Maverick — tool_calling_adversarial/confundible_verbo_enganoso

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 7.36 | quality: 7.1
- latency_total: 0.654s | tokens_per_second: 21.4
- input_tokens: 1110 | output_tokens: 14
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, identificando correctamente la herramienta para buscar la factura especificada. Aunque no ofrece profundidad adicional o insights, está claramente escrita y es prácticamente útil para un emprendedor que necesita acceder a información de facturación.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0398"})