# GPT-5.6 Terra Pro — agent_capabilities/model_as_router

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 6.89 | quality: 7.5
- latency_total: 6.283s | tokens_per_second: 179.2
- input_tokens: 3545 | output_tokens: 1126

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
    "razon": "Es adecuado para análisis y razonamiento sobre grandes volúmenes de texto, identificando patrones, agrupando temas y priorizando problemas de forma económica."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Destaca en comunicación empática, honesta y sensible; es ideal para redactar una disculpa clara que mantenga la confianza de los clientes."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Es fuerte en tareas generales de programación y coding rápido, por lo que puede producir un script Python práctico y mantenible."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "La generación de múltiples variaciones de copy es una tarea relativamente simple donde su alta velocidad ofrece una ventaja clara."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Su fortaleza en tool calling y flujos de agentes lo hace apropiado para ejecutar validaciones estructuradas, procesar lotes y reportar errores de formato o esquema."
  }
]