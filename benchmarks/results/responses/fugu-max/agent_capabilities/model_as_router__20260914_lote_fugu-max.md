# Fugu Max — agent_capabilities/model_as_router

- model_id: `sakana/fugu-max`
- success: True  | final: 7.25 | quality: 7.5
- latency_total: 4.858s | tokens_per_second: 100.9
- input_tokens: 329 | output_tokens: 490

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
    "razon": "Es fuerte en razonamiento y análisis de grandes volúmenes de texto, permitiendo agrupar temas y priorizar los problemas más frecuentes."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Destaca en comunicación empática, honesta y cuidadosa, ideal para gestionar una situación delicada con clientes."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Es un modelo generalista rápido y especialmente competente para tareas de programación y generación de código."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre el nuevo feature",
    "modelo": "claude-sonnet",
    "razon": "Puede producir contenido atractivo, claro y adaptado al tono de la audiencia, manteniendo consistencia entre múltiples publicaciones."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de la API sean correctas",
    "modelo": "gemini-flash-lite",
    "razon": "Es muy rápido y adecuado para tareas repetitivas y estructuradas como comprobar formatos, campos y validez básica de JSON."
  }
]