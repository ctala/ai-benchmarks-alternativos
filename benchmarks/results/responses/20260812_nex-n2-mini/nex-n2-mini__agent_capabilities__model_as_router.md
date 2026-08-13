# Nex-N2-Mini — agent_capabilities/model_as_router

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 7.8 | quality: 7.5
- latency_total: 2.233s | tokens_per_second: 173.3
- input_tokens: 276 | output_tokens: 387

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
    "modelo": "claude-sonnet",
    "razon": "Requiere síntesis cualitativa, comprensión de matices del usuario y empatía para identificar temas relevantes y redactarlos con claridad."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Es una tarea de comunicación sensible que necesita empatía, honestidad, tono apropiado y claridad."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Es una tarea de coding y razonamiento estructurado; deepseek-v3 es especialmente fuerte en programación y ofrece muy buen rendimiento en costo."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Es una tarea simple y de alto volumen que requiere redacción rápida y variada; gemini-flash-lite es ultrarrápido y suficiente para contenido directo."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "devstral",
    "razon": "Requiere razonamiento técnico y precisión en datos estructurados; devstral es general, rápido y bueno para tareas de coding/validación."
  }
]