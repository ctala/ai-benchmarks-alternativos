# Kimi K2 — agent_capabilities/model_as_router

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 5.19 | quality: 5.0
- latency_total: 10.993s | tokens_per_second: 41.6
- input_tokens: 306 | output_tokens: 457

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
    "razon": "Requiere razonamiento analítico sobre gran volumen de texto para identificar patrones y categorizar problemas. El costo bajo ($0.14/M) es ideal para procesar 500 reviews."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Necesita empatía genuina, tono honesto y reconocimiento de responsabilidad. Claude Sonnet es superior para comunicación delicada con clientes en situaciones de crisis."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Coding general + velocidad. Devstral combina buena capacidad de código con rapidez, ideal para scripts de procesamiento de datos sin necesidad de razonamiento profundo."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Tareas simples y repetitivas que requieren velocidad. 200+ tok/s permite generar 20 posts rápidamente a mínimo costo, sin necesidad de razonamiento complejo."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "deepseek-v3",
    "razon": "Requiere validación estructural y lógica de esquemas JSON. Deepseek-v3 ofrece buen razonamiento a muy bajo costo para tarea repetitiva de validación."
  }
]
```