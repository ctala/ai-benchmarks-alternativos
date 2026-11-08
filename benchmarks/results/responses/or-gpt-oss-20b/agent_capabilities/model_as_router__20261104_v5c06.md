# GPT-OSS 20B — agent_capabilities/model_as_router

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 4.0 | quality: 2.5
- latency_total: 9.538s | tokens_per_second: 86.6
- input_tokens: 307 | output_tokens: 826

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
    "razon": "El modelo es fuerte en razonamiento y análisis de texto, lo que permite identificar patrones y extraer los problemas más recurrentes de manera precisa."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Requiere empatía y honestidad en la comunicación, cualidades que el modelo claude-sonnet maneja especialmente bien."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "El modelo sobresale en tareas de programación y puede escribir código limpio y funcional para el procesamiento de datos."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "devstral",
    "razon": "Devstral es un modelo general rápido y creativo, ideal para generar contenido de marketing atractivo y variado."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Optimizado para el llamado de herramientas y la gestión de agentes, lo que facilita la validación automatizada de estructuras JSON."
  }
]
```