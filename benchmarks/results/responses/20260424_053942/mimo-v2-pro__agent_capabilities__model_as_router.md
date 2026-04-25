# MiMo-V2-Pro — agent_capabilities/model_as_router

- model_id: `xiaomi/mimo-v2-pro`
- success: True  | final: 7.42 | quality: 8.92
- latency_total: 10.605s | tokens_per_second: 58.9
- input_tokens: 290 | output_tokens: 625
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Excelente para razonamiento y análisis de texto a gran escala. Puede procesar grandes volúmenes de datos y extraer patrones de manera precisa y económica."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Su fortaleza en empatía y honestidad lo hace ideal para comunicaciones delicadas donde se necesita un tono apropiado y genuino."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Rápido y especializado en coding, puede generar scripts eficientes y correctos para procesamiento de datos."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Ultra rápido y eficiente para tareas de generación de contenido simple donde se necesita volumen y velocidad."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Bueno para tool calling y tareas estructuradas, puede validar formatos JSON y consistencia de manera confiable."
  }
]
```