# Nemotron 3 Super — agent_capabilities/model_as_router

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 5.7 | quality: 5.0
- latency_total: 7.062s | tokens_per_second: 89.5
- input_tokens: 282 | output_tokens: 632

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
    "razon": "Requiere razonamiento profundo y capacidad de síntesis para identificar patrones en gran volumen de texto; deepseek-v3 destaca en tareas de análisis y es muy económico."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "El contenido necesita empatía, tono honesto y sensibilidad; claude-sonnet está optimizado para generar texto con alta calidad emocional y comunicativa."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Tarea de coding que se beneficia de un modelo rápido y competente en programación; devstral ofrece buen desempeño en generación de código y es veloz."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Se necesita producción rápida de contenido creativo y breve; gemini-flash-lite es ultra rápido y adecuado para generar múltiples piezas de texto corto."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "La validación implica tool calling y verificaciones estructuradas; minimax-m2.7 está especializado en uso de herramientas y agentes para tareas de validación."
  }
]