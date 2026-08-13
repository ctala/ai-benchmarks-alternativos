# Grok 4.20 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `x-ai/grok-4.20`
- success: True  | final: 4.17 | quality: 2.9
- latency_total: 0.535s | tokens_per_second: 24.3
- input_tokens: 633 | output_tokens: 13
- judge_score: 1 | justificación: La respuesta es incorrecta y no relevante porque inventa un comando de herramienta que no existe en el esquema dado, ignorando la instruccion de buscar facturas impagas ordenadas por monto para el cliente Andes.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query":"Andes"})