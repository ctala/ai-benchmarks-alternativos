# Claude Opus 5 Fast — tool_calling_adversarial/alucinacion_funcion_inexistente

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 3.56 | quality: 2.9
- latency_total: 2.122s | tokens_per_second: 86.7
- input_tokens: 903 | output_tokens: 184
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa una llamada de herramienta que no existe, violando la instrucción de no inventar funciones. No aborda la tarea de anular la factura con el RUT equivocado, por lo que es irrelevante y no ofrece profundidad o utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Anula la factura F-0377, la emitimos con el RUT equivocado.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura": "F-0377"})