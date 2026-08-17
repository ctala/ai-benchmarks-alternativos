# Ministral 14B — tool_calling_adversarial/confundible_verbo_enganoso

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 7.52 | quality: 7.1
- latency_total: 0.581s | tokens_per_second: 37.9
- input_tokens: 487 | output_tokens: 22
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, identificando correctamente la herramienta para buscar la factura especificada. Aunque no ofrece profundidad adicional o insights, está claramente estructurada y es directamente util para un emprendedor que necesita acceder a información de facturación.

## Entrada exacta (lo que recibió el modelo)

**user:**

Necesito ver qué le facturamos a la constructora Andes el mes pasado. La factura es la F-0398.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0398"})