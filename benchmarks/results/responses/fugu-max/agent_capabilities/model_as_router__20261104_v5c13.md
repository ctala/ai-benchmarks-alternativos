# Fugu Max — agent_capabilities/model_as_router

- model_id: `sakana/fugu-max`
- success: True  | final: 5.18 | quality: 5.0
- latency_total: 6.068s | tokens_per_second: 89.2
- input_tokens: 347 | output_tokens: 541

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
    "subtarea": "Analizar 500 reseñas y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Es adecuado para analizar grandes volúmenes de texto y sintetizar patrones."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Destaca en contenido empático y honesto."
  },
  {
    "subtarea": "Generar un script Python para procesar los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Es rápido y sólido para tareas generales de programación."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre el nuevo feature",
    "modelo": "claude-sonnet",
    "razon": "Puede producir contenido atractivo y adaptar el tono para redes sociales."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de la API sean correctas",
    "modelo": "deepseek-v3",
    "razon": "Su capacidad de razonamiento y programación encaja con la validación de estructura y contenido."
  }
]