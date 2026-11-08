# Gemini 3.1 Pro — agent_capabilities/model_as_router

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 4.67 | quality: 5.0
- latency_total: 31.62s | tokens_per_second: 97.4
- input_tokens: 266 | output_tokens: 3081

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
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere buena capacidad de razonamiento para sintetizar insights. Además, al tratarse de un volumen alto de texto (500 reviews), su costo muy barato ($0.14/M) lo hace la opción más eficiente."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Manejar quejas y disculpas requiere tacto humano. Este modelo es el mejor para contenido que necesita transmitir empatía y honestidad, cuidando la relación con el cliente."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Es el mejor modelo de uso general, rápido y muy bueno para tareas de programación (coding), ideal para crear scripts de procesamiento de datos sin demoras."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Es una tarea creativa relativamente simple pero de volumen. Su velocidad ultra rápida (200+ tok/s) es perfecta para generar múltiples variaciones de texto casi al instante."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Al implicar interacción con una API y validación de datos estructurados, es una tarea perfecta para un enfoque de agente inteligente que aproveche sus fortalezas en tool calling."
  }
]
```