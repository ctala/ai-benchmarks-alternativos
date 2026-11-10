# Gemini 3.1 Flash Lite (GA) — tool_calling_adversarial/confundible_recordar_vs_emitir

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 5.26 | quality: 4.3
- latency_total: 1.073s | tokens_per_second: 23.3
- input_tokens: 275 | output_tokens: 25
- judge_score: 2.0 | justificación: La respuesta no aborda directamente la tarea de recordar el pago al cliente, sino que realiza una llamada de herramienta para buscar la factura, lo cual es un paso preliminar y no responde a la instrucción de comunicación con el cliente.

## Entrada exacta (lo que recibió el modelo)

**user:**

La factura F-0412 está vencida hace tres semanas. Mándale algo al cliente, pero sin ser agresivo que es un cliente antiguo.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura":"F-0412"})