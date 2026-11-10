# GPT-OSS 20B — agent_capabilities/model_as_router

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 4.15 | quality: 2.5
- latency_total: 5.342s | tokens_per_second: 127.1
- input_tokens: 320 | output_tokens: 679

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
    "modelo": "devstral",
    "razon": "Devstral es un modelo general rápido y competente en tareas de análisis de texto y extracción de información clave, ideal para procesar grandes volúmenes de reseñas y resumir los problemas más frecuentes."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Claude‑Sonnet sobresale en contenidos que requieren empatía, tono cuidadoso y honestidad, cualidades esenciales para una carta de disculpa que mantenga la confianza del cliente."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Deepseek‑v3 es el mejor para razonamiento y generación de código, ofreciendo precisión y velocidad en scripts que manipulan datos y realizan cálculos."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "devstral",
    "razon": "Devstral combina rapidez con creatividad, generando contenido variado y atractivo para múltiples plataformas de redes sociales."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Minimax‑m2.7 está especializado en llamadas a herramientas y manejo de agentes, lo que lo hace ideal para verificar estructuras JSON y garantizar la validez de cada respuesta."
  }
]
```