# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — agent_capabilities/model_as_router

- model_id: `nemotron-3-super:120b`
- success: True  | final: 7.18 | quality: 8.8
- latency_total: 41.523s | tokens_per_second: 18.3
- input_tokens: 282 | output_tokens: 758
- judge_score: 4.4 | justificación: 

## Respuesta completa

[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere razonamiento avanzado para resumir y detectar patrones en gran volumen de texto; deepseek-v3 destaca en tareas de razonamiento y es muy económico."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Necesita empatía, tono honesto y sensibilidad emocional; claude-sonnet es el mejor para contenido que requiere esas cualidades."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Tarea de coding; deepseek-v3 es excelente para generar código preciso y eficiente, además de ser barato."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Se necesita generar varios textos cortos y creativos rápidamente; gemini-flash-lite es ultra rápido y adecuado para tareas simples de generación de contenido."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Validación estructurada puede beneficiarse de capacidades de tool calling y agentes; minimax-m2.7 destaca en esas áreas."
  }
]