# Qwen 3.6 Max — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 5.37 | quality: 6.0
- latency_total: 67.981s | tokens_per_second: 39.1
- input_tokens: 110 | output_tokens: 2655
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

Un workflow que devuelve `success` sin haber procesado datos no es un bug: es el comportamiento nativo de n8n ante arrays vacíos. Cuando un nodo upstream filtra, transforma o enruta y el resultado es `[]`, la ejecución no falla. Simplemente propaga cero items. Los nodos downstream se ejecutan en modo *no-op* o se omiten silenciosamente, el trigger marca `success`, y tu dashboard muestra un green check que no refleja realidad operativa.

Los culpables típicos: un `IF`/`Switch` sin rama `fallback`, un `Filter` con condiciones excluyentes, o `Continue On Fail` activado sin validación posterior. n8n solo lanza error ante excepciones no capturadas o nodos configurados explícitamente para `Stop and Error`. Un `success` garantiza ausencia de crashes, no procesamiento efectivo.

Cómo detectarlo y blindar tus pipelines:
- Inyecta un nodo `Code` post-trigger: `if ($input.all().length === 0) throw new Error('Empty item array');`
- Usa `Item Lists → Limit` con `Stop execution if empty` para forzar fallo controlado sin lógica custom.
- Aprovecha el historial de ejecuciones y exporta `$execution.id` + `items.length` a tu stack de observabilidad (Prometheus, Datadog, o un endpoint de logging interno).
- En flujos críticos, añade un `IF` que valide estructura y volumen, y rutee a `Stop and Error` si no coinciden con el contrato esperado.

El `success` de n8n es un estado de runtime, no una métrica de negocio. Valida items, no solo exits.