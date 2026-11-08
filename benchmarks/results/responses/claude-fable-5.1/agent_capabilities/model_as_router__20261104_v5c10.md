# Claude Fable 5.1 — agent_capabilities/model_as_router

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 4.73 | quality: 5.0
- latency_total: 8.737s | tokens_per_second: 79.1
- input_tokens: 436 | output_tokens: 691

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente router inteligente. Tu trabajo es decidir que modelo de IA usar para cada subtarea basado en sus fortalezas:

Modelos disponibles:
- deepseek-v3: Mejor para razonamiento y coding, muy barato ($0.14/M)
- gemini-flash-lite: Ultra rapido (200+ tok/s), bueno para tareas simples
- claude-sonnet: Mejor para contenido que requiere empatia y honestidad
- minimax-m2.7: Bueno para tool calling y agentes
- devstral: Mejor general, rapido, bueno para coding

Para cada subtarea, responde con un JSON array:
[{"subtarea": "...", "modelo": "...", "razon": "..."}]

**user:**

Tengo estas tareas para mi startup:
1. Analizar 500 reviews de usuarios y extraer los 5 problemas principales
2. Escribir un email de disculpas a clientes afectados por un bug
3. Generar un script Python que procese los datos de ventas de Q1
4. Crear 20 posts para redes sociales sobre nuestro nuevo feature
5. Validar que 100 respuestas JSON de nuestra API sean correctas

Asigna el mejor modelo para cada una.


## Respuesta completa

[
  {
    "subtarea": "1. Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere razonamiento para sintetizar y categorizar patrones en un volumen grande de texto, y su bajo costo ($0.14/M) es ideal para procesar 500 reviews sin disparar el gasto."
  },
  {
    "subtarea": "2. Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Comunicación sensible con clientes molestos: necesita tono empático, honestidad sobre lo ocurrido y cuidado en el mensaje. Es una sola pieza, así que el costo no es un factor."
  },
  {
    "subtarea": "3. Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Modelo rápido y fuerte en coding, ideal para generar un script funcional de procesamiento de datos. deepseek-v3 sería la alternativa si el procesamiento requiere lógica más compleja."
  },
  {
    "subtarea": "4. Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Tarea creativa de baja complejidad y alto volumen: 20 variaciones cortas. La velocidad (200+ tok/s) permite iterar rápido sobre tono y formato sin costo significativo."
  },
  {
    "subtarea": "5. Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Validación repetitiva que se beneficia de tool calling (ejecutar validadores de esquema, comparar contra specs, reportar errores). Un flujo agéntico es más confiable que inspección manual de 100 JSONs."
  }
]