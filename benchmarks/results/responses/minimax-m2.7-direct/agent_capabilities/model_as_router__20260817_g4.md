# MiniMax M2.7 (directo) — agent_capabilities/model_as_router

- model_id: `MiniMax-M2.7`
- success: True  | final: 8.92 | quality: 10.0
- latency_total: 10.63s | tokens_per_second: 55.7
- input_tokens: 264 | output_tokens: 592

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

```json
[
  {
    "subtarea": "Analizar 500 reviews y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Excelente para razonamiento y análisis de patrones en grandes volúmenes de texto. Identificará temas recurrentes eficientemente."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Requiere empatía genuina, tono apropiado y comunicación honesta. Es el mejor para contenido sensible orientado a relaciones con clientes."
  },
  {
    "subtarea": "Generar script Python para procesar datos de ventas Q1",
    "modelo": "devstral",
    "razon": "Mejor modelo general para coding: rápido, preciso y con buena comprensión de estructuras de datos y lógica de negocio."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Tarea simple y repetitiva que requiere velocidad. Generará contenido variado rápidamente a bajo costo."
  },
  {
    "subtarea": "Validar 100 respuestas JSON de la API",
    "modelo": "minimax-m2.7",
    "razon": "Especializado en tool calling y agentes. Ideal para validación estructurada de datos JSON con acciones repetitivas."
  }
]
```