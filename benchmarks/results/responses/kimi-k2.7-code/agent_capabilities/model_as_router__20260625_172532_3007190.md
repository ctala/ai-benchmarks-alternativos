# Kimi K2.7 Code — agent_capabilities/model_as_router

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.33 | quality: 8.92
- latency_total: 28.885s | tokens_per_second: 32.0
- input_tokens: 304 | output_tokens: 924
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Gran volumen de texto (500 reviews) que requiere razonamiento para identificar patrones y agrupar problemas. deepseek-v3 es económico y fuerte en razonamiento, ideal para procesar muchos datos sin costos altos."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Tarea que requiere empatía, tono genuino y honestidad. claude-sonnet es el mejor opción para comunicación sensible con clientes."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Tarea de coding que beneficia de un modelo general rápido y capaz. devstral destaca en velocidad y calidad de código."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Generación de contenido simple y repetitivo en gran cantidad. gemini-flash-lite es ultra rápido, perfecto para producir muchos posts en poco tiempo."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Tarea estructurada de verificación que puede aprovechar tool calling o patrones de agente. minimax-m2.7 es bueno para este tipo de validaciones sistemáticas."
  }
]
```