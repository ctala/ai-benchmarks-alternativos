# Tencent Hy3 — agent_capabilities/model_as_router

- model_id: `tencent/hy3`
- success: True  | final: 5.35 | quality: 5.0
- latency_total: 37.833s | tokens_per_second: 55.2
- input_tokens: 302 | output_tokens: 2090

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
    "razon": "Requiere fuerte razonamiento para sintetizar patrones en gran volumen de texto y su muy bajo costo ($0.14/M) es óptimo para procesar los muchos tokens de 500 reviews."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "El mensaje exige empatía y honestidad hacia usuarios frustrados, que es la fortaleza principal de claude-sonnet."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Es una tarea de coding donde un modelo general, rápido y eficiente como devstral ofrece gran calidad y velocidad de desarrollo."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Generar 20 contenidos cortos es una tarea simple y de alto volumen donde la ultra velocidad (200+ tok/s) de gemini-flash-lite maximiza la productividad."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "La verificación estructurada de respuestas de API es una tarea ideal para agentes y tool calling, fortaleza específica de minimax-m2.7."
  }
]