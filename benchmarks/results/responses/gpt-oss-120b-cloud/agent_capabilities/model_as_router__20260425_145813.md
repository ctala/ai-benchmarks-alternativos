# GPT-OSS 120B (Ollama Cloud) — agent_capabilities/model_as_router

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 7.88 | quality: 8.8
- latency_total: 6.301s | tokens_per_second: 98.7
- input_tokens: 321 | output_tokens: 622
- judge_score: 4.4 | justificación: 

## Respuesta completa

[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere razonamiento y extracción de información clave de gran volumen de texto; deepseek‑v3 es excelente para análisis y es económico."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "El tono empático y la honestidad son críticos en una disculpa; claude‑sonnet sobresale en contenido sensible y tono humano."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Necesita razonamiento y habilidades de programación; deepseek‑v3 está optimizado para coding y es muy barato."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Tarea creativa pero sencilla y de alto volumen; gemini‑flash‑lite es ultra‑rápido, ideal para generar muchos textos rápidamente."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Requiere llamadas a herramientas y validación estructurada de datos; minimax‑m2.7 está diseñado para tool‑calling y agentes."
  }
]