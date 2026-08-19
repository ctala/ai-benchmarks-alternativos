# Nemotron 3 Super — agent_capabilities/model_as_router

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 5.18 | quality: 5.0
- latency_total: 117.323s | tokens_per_second: 5.2
- input_tokens: 282 | output_tokens: 606

## Respuesta completa



[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere razonamiento profundo y capacidad de síntesis para identificar patrones en gran volumen de texto; deepseek-v3 destaca en tareas de análisis y es muy económico."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Necesita tono empático, honesto y persuasivo; claude-sonnet es el mejor para contenido que requiere sensibilidad emocional."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Tarea de código; deepseek-v3 tiene fuerte capacidad de generación de código y es muy barato."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Requiere producción rápida de contenido creativo y conciso; gemini-flash-lite es ultra rápido y adecuado para tareas simples de generación de texto."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Involucra verificación estructurada y posible uso de herramientas para validar JSON; minimax-m2.7 destaca en tool calling y agentes."
  }
]