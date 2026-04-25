# Devstral Medium — agent_capabilities/model_as_router

- model_id: `mistralai/devstral-medium`
- success: True  | final: 7.67 | quality: 8.07
- latency_total: 2.635s | tokens_per_second: 123.3
- input_tokens: 271 | output_tokens: 325
- judge_score: 4.2 | justificación: 

## Respuesta completa

[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Mejor para razonamiento y análisis de texto, adecuado para extraer problemas principales de reviews."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Mejor para contenido que requiere empatía y honestidad, ideal para escribir emails de disculpas."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Mejor para razonamiento y coding, adecuado para generar scripts de procesamiento de datos."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Ultra rápido y bueno para tareas simples, ideal para generar contenido rápido para redes sociales."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Bueno para tool calling y agentes, adecuado para validar respuestas JSON de una API."
  }
]