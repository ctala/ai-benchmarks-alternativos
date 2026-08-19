# Llama 4 Scout 17B — tool_calling_adversarial/falta_parametro_monto

- model_id: `meta-llama/llama-4-scout`
- success: True  | final: 6.69 | quality: 5.7
- latency_total: 0.927s | tokens_per_second: 61.5
- input_tokens: 1011 | output_tokens: 57
- judge_score: 3.0 | justificación: La respuesta es precisa y relevante al llamar a la herramienta con los parámetros correctos, pero no aborda la instrucción de preguntar el monto, lo que afecta la profundidad y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Emítele la factura al cliente CL-2291 por la consultoría de octubre.


## Respuesta completa

[tool_call] emitir_factura({"cliente_id":"CL-2291","concepto":"Consultoría de octubre","monto":0})