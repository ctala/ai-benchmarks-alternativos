# Qwen 3.8 Max — agent_capabilities/model_as_router

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 3.11 | quality: 2.5
- latency_total: 23.537s | tokens_per_second: 42.1
- input_tokens: 315 | output_tokens: 991

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
    "razon": "Es una tarea de análisis y síntesis de texto con posible volumen alto; deepseek-v3 ofrece buen razonamiento a bajo costo."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Requiere empatía, tono cuidadoso y comunicación honesta; claude-sonnet es el mejor para contenido sensible."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Es una tarea de coding y procesamiento de datos; deepseek-v3 es fuerte en programación y es muy barato."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "devstral",
    "razon": "Es una tarea de generación de contenido variado y práctico; devstral es bueno como modelo general, rápido y versátil."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Implica validación estructurada y posiblemente uso de herramientas o flujo agente; minimax-m2.7 es bueno para tool calling y agentes."
  }
]