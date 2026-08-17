# Claude Fable 5 — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 3.13 | quality: 2.9
- latency_total: 7.56s | tokens_per_second: 18.9
- input_tokens: 912 | output_tokens: 143
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro 'query' que no está soportado por el esquema, lo cual es una alucinación. No responde a la instrucción original de buscar facturas impagas ordenadas por monto para el cliente 'Andes'. La respuesta carece de profundidad y utilidad práctica, ya que no proporciona información relevante o útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})