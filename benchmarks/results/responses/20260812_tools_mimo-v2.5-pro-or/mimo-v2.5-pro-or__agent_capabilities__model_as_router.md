# MiMo-V2.5 Pro — agent_capabilities/model_as_router

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 18.929s | tokens_per_second: 50.2
- input_tokens: 290 | output_tokens: 950

## Respuesta completa

```json
[
  {
    "subtarea": "Analizar 500 reviews y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere razonamiento profundo para identificar patrones y sintetizar información de alto volumen. DeepSeek-V3 es excelente en análisis y extremadamente barato para procesar grandes cantidades de texto."
  },
  {
    "subtarea": "Escribir email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Necesita empatía, tono adecuado y sensibilidad. Claude-sonnet destaca en contenido que requiere honestidad y conexión emocional auténtica."
  },
  {
    "subtarea": "Generar script Python para procesar datos de ventas Q1",
    "modelo": "deepseek-v3",
    "razon": "Coding puro donde DeepSeek-V3 es top-tier. Muy barato ($0.14/M) para generación de código, ideal para scripts de procesamiento de datos."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Generación de contenido repetitivo y creativo donde la velocidad importa. 200+ tok/s permite generar los 20 posts rápidamente a bajo costo."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de la API sean correctas",
    "modelo": "gemini-flash-lite",
    "razon": "Tarea estructurada y repetitiva de validación. La velocidad ultra rápida procesa las 100 respuestas en segundos, y es suficiente para verificar estructura JSON."
  }
]
```