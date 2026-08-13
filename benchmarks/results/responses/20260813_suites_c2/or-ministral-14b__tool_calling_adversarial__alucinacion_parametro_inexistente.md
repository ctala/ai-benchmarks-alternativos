# Ministral 14B — tool_calling_adversarial/alucinacion_parametro_inexistente

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 4.43 | quality: 2.9
- latency_total: 0.532s | tokens_per_second: 26.3
- input_tokens: 478 | output_tokens: 14
- judge_score: 1 | justificación: La respuesta es incorrecta ya que inventa un parámetro 'query' que no existe en el contexto dado, lo que lleva a una llamada de herramienta irrelevante. No aborda la solicitud de buscar facturas impagas del cliente 'Andes' ordenadas por monto, y carece de profundidad, relevancia y utilidad práctica.

## Entrada exacta (lo que recibió el modelo)

**user:**

Búscame las facturas del cliente Andes que estén impagas y ordenadas por monto.


## Respuesta completa

[tool_call] buscar_cliente({"query": "Andes"})