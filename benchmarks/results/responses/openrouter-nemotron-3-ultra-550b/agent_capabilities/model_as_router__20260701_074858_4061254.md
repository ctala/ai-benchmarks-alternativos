# Nemotron 3 Ultra 550B — agent_capabilities/model_as_router

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.58 | quality: 9.2
- latency_total: 3.636s | tokens_per_second: 202.1
- input_tokens: 282 | output_tokens: 735

## Respuesta completa

[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere razonamiento complejo, síntesis de gran volumen de texto y detección de patrones; DeepSeek destaca en razonamiento y es muy barato para alto volumen"
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Necesita empatía genuina, tono honesto y cuidado diplomático; Claude Sonnet es el mejor para contenido que requiere inteligencia emocional"
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Tarea de coding puro; Devstral es rápido, bueno en coding y el mejor modelo general para desarrollo"
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Alto volumen de tareas simples y repetitivas; Gemini Flash Lite es ultra rápido (200+ tok/s) y económico para generación masiva"
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Validación estructurada y programática de APIs; Minimax destaca en tool calling y tareas de agente con formato JSON"
  }
]