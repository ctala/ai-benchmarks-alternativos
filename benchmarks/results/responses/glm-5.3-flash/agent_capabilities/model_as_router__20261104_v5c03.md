# GLM 5.3 Flash — agent_capabilities/model_as_router

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 5.45 | quality: 5.0
- latency_total: 14.764s | tokens_per_second: 85.3
- input_tokens: 279 | output_tokens: 1259

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
    "razon": "Tarea de razonamiento pesado sobre gran volumen de texto. deepseek-v3 destaca en razonamiento y su costo bajísimo ($0.14/M) es ideal para procesar 500 reviews sin inflar costos."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Requiere empatía, honestidad y tono cuidadoso en una situación sensible. Es exactamente la fortaleza de claude-sonnet; un email frío o robótico empeoraría la relación con el cliente."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Coding directo sin ambigüedad. devstral es el mejor general, rápido y fuerte en código, perfecto para un script bien definido como este."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Contenido de formato simple y repetitivo donde el volumen importa. A 200+ tok/s, gemini-flash-lite genera los 20 posts casi al instante a costo mínimo."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Tarea agéntica que implica hacer llamadas, iterar sobre respuestas y verificar resultados. minimax-m2.7 es el mejor en tool calling y flujos de agente."
  }
]
```

**Resumen de la estrategia:** reasoning barato a escala (deepseek-v3), empatía donde importa (claude-sonnet), velocidad en código (devstral), throughput en contenido simple (gemini-flash-lite) y orquestación agéntica (minimax-m2.7). Cada tarea usa su modelo óptimo sin pagar de más.