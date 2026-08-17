# Qwen 3.6 27B base (OpenRouter FP8) — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 17.184s | tokens_per_second: 91.7
- input_tokens: 110 | output_tokens: 1575
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando estrategias prácticas y detalladas para detectar y manejar workflows que devuelven 'success' sin procesar datos.

## Respuesta completa

Un workflow que termina en “success” no garantiza que haya procesado datos. En n8n, ese estado solo indica que no se lanzó una excepción, no que existan ítems en el pipeline. Ocurre cuando un `Filter`, `IF` o `HTTP Request` devuelve `[]`, cuando una rama de `Merge` no recibe entradas, o cuando una API responde `200 OK` con un payload que tu lógica descarta silenciosamente. El nodo `Code` también es frecuente: retornar `[]` o `null` cierra la ejecución sin marcar error.

Detectarlo requiere auditar el flujo, no el banner de estado. Antes de cualquier nodo de acción, inserta un `IF` que valide `{{ $input.all().length > 0 }}`. Si usas `Continue on Fail`, recuerda que suprime excepciones pero no vacía el pipeline por arte de magia; combina con un `Log` o `Set` que registre `$input.all().length` para rastrear caídas de throughput. En ejecuciones programadas, cruza el historial: `success` repetido con `0 items processed` es un cuello de botella silencioso.

Una práctica robusta es centralizar la validación temprana: un `Code` que lance `throw new Error('Empty pipeline')` cuando el array sea vacío. Eso fuerza un `error` real, activa tus alertas y rompe la ilusión del verde. En automatización, el silencio no es estabilidad: es un fallo disfrazado.