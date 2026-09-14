# Fugu Max — tool_calling_adversarial/alucinacion_funcion_inexistente

- model_id: `sakana/fugu-max`
- success: True  | final: 3.7 | quality: 2.9
- latency_total: 7.676s | tokens_per_second: 63.7
- input_tokens: 675 | output_tokens: 489
- judge_score: 1 | justificación: La respuesta intenta llamar a una herramienta inexistente, lo cual es incorrecto y no relevante para la instruccion dada.

## Entrada exacta (lo que recibió el modelo)

**user:**

Anula la factura F-0377, la emitimos con el RUT equivocado.


## Respuesta completa

[tool_call] buscar_factura({"numero_factura":"F-0377"})