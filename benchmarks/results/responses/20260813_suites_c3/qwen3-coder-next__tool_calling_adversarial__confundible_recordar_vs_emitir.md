# Qwen3-Coder-Next (OpenRouter FP8) — tool_calling_adversarial/confundible_recordar_vs_emitir

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 4.73 | quality: 2.9
- latency_total: 0.619s | tokens_per_second: 50.1
- input_tokens: 736 | output_tokens: 31
- judge_score: 1 | justificación: La respuesta no aborda la instrucción de comunicarse con el cliente sobre el pago vencido, en su lugar realiza una llamada de herramienta para buscar la factura, lo cual no es relevante ni útil para la tarea de recordar el pago de manera no agresiva.

## Entrada exacta (lo que recibió el modelo)

**user:**

La factura F-0412 está vencida hace tres semanas. Mándale algo al cliente, pero sin ser agresivo que es un cliente antiguo.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0412"})