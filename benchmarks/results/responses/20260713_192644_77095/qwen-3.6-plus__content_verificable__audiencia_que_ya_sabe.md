# Qwen 3.6 Plus — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 5.91 | quality: 6.0
- latency_total: 40.263s | tokens_per_second: 53.7
- input_tokens: 110 | output_tokens: 2161
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

¿Tu workflow devuelve `success` pero en producción no ejecutó nada? Es un patrón silencioso en n8n: el runtime marca la ejecución como exitosa siempre que no se propague una excepción no capturada, aunque el pipeline de datos colapse en el camino.

Las causas son arquitectónicas, no de bug. Un `Filter` o `Switch` que evalúa `false` para todos los inputs cierra la rama sin lanzar error. Un nodo HTTP devuelve `200 OK` con un body vacío o un error estructurado que tu transformación no valida. `Continue On Fail` o `Always Output Data` enmascaran fallos downstream. El motor solo mide la ausencia de crash, no la integridad del item stream.

Para detectarlo, instrumenta validación explícita:
- Inserta un `IF` o `Code` que verifique `{{$json.items?.length > 0}}` o la presencia de campos críticos antes del cierre.
- Configura un `Error Trigger` workflow que capture ejecuciones con `0 items` o `runStatus: "success"` pero sin output real.
- En llamadas externas, no confíes en el código HTTP; valida el payload con expresiones que lancen `throw new Error()` si falta estructura esperada.
- Audita `executionData.resultData.runData` en logs para identificar nodos que devuelven `[]` o `{}` silenciosamente.

El `success` de n8n es un estado de ejecución, no una garantía de negocio. Instrumenta tus propios checkpoints. ¿Qué estrategia usas para evitar falsos positivos en tus pipelines?