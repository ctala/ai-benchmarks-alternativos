# Gemini 3.5 Flash Lite — tool_calling_adversarial/confundible_recordar_vs_emitir

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 5.26 | quality: 4.3
- latency_total: 1.07s | tokens_per_second: 23.4
- input_tokens: 275 | output_tokens: 25
- judge_score: 2.0 | justificación: La respuesta busca información sobre la factura, pero no aborda directamente la instrucción de recordar el pago al cliente de manera no agresiva.

## Entrada exacta (lo que recibió el modelo)

**user:**

La factura F-0412 está vencida hace tres semanas. Mándale algo al cliente, pero sin ser agresivo que es un cliente antiguo.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura":"F-0412"})