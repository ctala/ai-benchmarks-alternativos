# Tencent Hy4 — agent_capabilities/model_as_router

- model_id: `tencent/hy4`
- success: True  | final: 5.07 | quality: 5.0
- latency_total: 37.314s | tokens_per_second: 98.3
- input_tokens: 302 | output_tokens: 3668

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
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere razonamiento y síntesis para agrupar temas en mucho texto; además los 500 reviews implican alto volumen de tokens y es el modelo más barato ($0.14/M)."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Es contenido que exige empatía y honestidad para reconocer el error y recuperar la confianza, su fortaleza principal."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Es una tarea de coding directa; devstral es el mejor general, rápido y bueno para código, ideal para un script estándar sin razonamiento pesado."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Generación repetitiva y simple de variaciones cortas; su velocidad ultra rápida (200+ tok/s) resuelve los 20 posts con baja latencia."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Validar respuestas de API en bucle implica tool calling y comportamiento de agente (invocar endpoints, parsear y comprobar esquemas), su especialidad."
  }
]