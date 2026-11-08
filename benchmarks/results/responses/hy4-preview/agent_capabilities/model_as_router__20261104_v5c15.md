# Tencent Hy4 preview — agent_capabilities/model_as_router

- model_id: `tencent/hy4-preview`
- success: True  | final: 6.47 | quality: 7.5
- latency_total: 161.887s | tokens_per_second: 68.2
- input_tokens: 302 | output_tokens: 11040

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
    "razon": "Requiere razonamiento para analizar un gran volumen de texto, identificar patrones y resumir los problemas clave; deepseek-v3 es el mejor para razonamiento y muy económico para procesar muchos tokens."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "El email debe transmitir empatía y honestidad a los clientes afectados; claude-sonnet es el mejor para contenido que requiere estas cualidades."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Es una tarea de programación; deepseek-v3 es el mejor para coding y razonamiento lógico, asegurando un script correcto y eficiente."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "devstral",
    "razon": "Es una tarea de generación de contenido general y creativo; devstral es el mejor modelo general, rápido y versátil para crear múltiples publicaciones atractivas."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "gemini-flash-lite",
    "razon": "Verificar 100 respuestas JSON es una tarea estructurada, repetitiva y simple (validar esquema/campos); gemini-flash-lite es ultra rápido y bueno para tareas simples, ideal para procesarlas velozmente."
  }
]