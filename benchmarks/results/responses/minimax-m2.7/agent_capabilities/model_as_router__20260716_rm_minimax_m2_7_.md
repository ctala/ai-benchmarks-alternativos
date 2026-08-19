# MiniMax M2.7 — agent_capabilities/model_as_router

- model_id: `minimax/minimax-m2.7`
- success: True  | final: 7.12 | quality: 7.5
- latency_total: 11.97s | tokens_per_second: 66.7
- input_tokens: 264 | output_tokens: 798
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando asignaciones de modelos bien justificadas para cada subtarea.

## Respuesta completa

```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Excelente razonamiento analítico para procesar grandes volúmenes de texto, identificar patrones y sintetizar información. Además es muy económico."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Necesitas empatía genuina, tono apropiado y comunicación sensible. Claude es el mejor para contenido que requiere conexión emocional honesta."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Razonamiento lógico y coding son su punto fuerte. Procesamiento de datos estructurados lo maneja excelentemente."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Tarea de alto volumen con formato repetitivo. Su velocidad ultrarrápida (200+ tok/s) genera las 20 variaciones rápidamente."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2",
    "razon": "Tarea estructurada, repetitiva y posiblemente con tool calling (llamadas a la API). Minimax-m2 es óptimo para agentes y validación sistemática."
  }
]
```