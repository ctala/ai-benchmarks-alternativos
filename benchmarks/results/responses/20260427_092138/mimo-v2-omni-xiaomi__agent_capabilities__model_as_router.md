# MiMo V2-Omni (Xiaomi direct) — agent_capabilities/model_as_router

- model_id: `mimo-v2-omni`
- success: True  | final: 7.83 | quality: 8.8
- latency_total: 8.083s | tokens_per_second: 108.5
- input_tokens: 290 | output_tokens: 877
- judge_score: 4.4 | justificación: 

## Respuesta completa

[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere procesamiento de lenguaje natural y razonamiento para identificar patrones y sintetizar información de múltiples fuentes, donde deepseek-v3 destaca en análisis y es económico para grandes volúmenes."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "La comunicación empática y honesta es crucial para mantener la confianza del cliente; claude-sonnet está optimizado para generar contenido con tono humano y comprensivo."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Tarea de programación específica donde deepseek-v3 tiene fortalezas en coding y lógica, además de ser rentable para scripts funcionales."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Generación de contenido creativo y variado a alta velocidad; gemini-flash-lite es ideal para tareas de redacción rápida y voluminosa con buen rendimiento."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Requiere verificación sistemática y manejo de estructuras de datos, donde minimax-m2.7 destaca en tool calling y automatización de agentes para validaciones."
  }
]