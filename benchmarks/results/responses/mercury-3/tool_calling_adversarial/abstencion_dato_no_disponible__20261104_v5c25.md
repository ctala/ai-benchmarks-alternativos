# Mercury 3 — tool_calling_adversarial/abstencion_dato_no_disponible

- model_id: `inception/mercury-3`
- success: True  | final: 4.73 | quality: 2.9
- latency_total: 1.06s | tokens_per_second: 373.7
- input_tokens: 643 | output_tokens: 396
- judge_score: 1 | justificación: La respuesta es incorrecta y no relevante, ya que intenta llamar a una herramienta para una tarea que no puede realizar, ignorando la instrucción de abstenerse de hacer llamadas de herramientas para datos no disponibles.

## Entrada exacta (lo que recibió el modelo)

**user:**

¿Cuánto facturé en total el trimestre pasado?


## Respuesta completa

[tool_call] buscar_cliente({"query": " "})