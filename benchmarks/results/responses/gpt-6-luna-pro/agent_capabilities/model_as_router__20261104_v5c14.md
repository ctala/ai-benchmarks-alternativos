# GPT-6 Luna Pro — agent_capabilities/model_as_router

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 5.63 | quality: 5.0
- latency_total: 8.76s | tokens_per_second: 125.3
- input_tokens: 2918 | output_tokens: 1098

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
    "razon": "Bueno para analizar grandes cantidades de texto, identificar patrones y sintetizar los problemas principales."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Destaca en comunicación empática, cuidadosa y honesta."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Fuerte en programación y razonamiento, con un costo bajo."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre el nuevo feature",
    "modelo": "claude-sonnet",
    "razon": "Adecuado para generar contenido atractivo y mantener un tono consistente."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de la API sean correctas",
    "modelo": "gemini-flash-lite",
    "razon": "Es una tarea repetitiva y estructurada que se beneficia de su alta velocidad."
  }
]