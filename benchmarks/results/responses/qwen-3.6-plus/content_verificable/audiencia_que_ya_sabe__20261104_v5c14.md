# Qwen 3.6 Plus — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 80.062s | tokens_per_second: 58.0
- input_tokens: 110 | output_tokens: 4644

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Un workflow que devuelve `success` sin procesar datos no es un bug; es un síntoma de flujo vacío. En n8n, el estado de ejecución refleja el *runtime*, no la lógica de negocio. Si un webhook recibe un payload vacío, una query devuelve 0 filas o un nodo `IF` filtra todo, la ejecución termina correctamente porque no hubo fallos técnicos. El motor hizo exactamente lo que se le pidió: nada.

El problema real es la invisibilidad. Un `success` con 0 items en el output puede pasar desapercibido hasta que rompe dependencias downstream o desalinea métricas de negocio.

Para detectarlo, deja de confiar en el estado de ejecución. Implementa validaciones explícitas:
• Inserta un nodo `Code` que verifique `items.length > 0`. Si es falso, fuerza un `throw new Error('Empty execution')` o redirige a un canal de alerta.
• Desactiva `Continue on Fail` en nodos HTTP/DB críticos. Silencian errores y generan `success` falsos. Envuélvelos en bloques `Try/Catch` con logging explícito.
• Monitorea métricas, no estados. Usa la API de n8n (`GET /executions`) para filtrar ejecuciones `status: success` con `data.resultData.runData` vacío o `items: 0`. Automatiza un script que alerte cuando el ratio de ejecuciones vacías supere un umbral.
• Configura alertas basadas en conteo de items, no en `execution.finished`.

Un workflow productivo no asume datos; los valida. El `success` debe significar “procesé lo esperado”, no “no rompí nada”.