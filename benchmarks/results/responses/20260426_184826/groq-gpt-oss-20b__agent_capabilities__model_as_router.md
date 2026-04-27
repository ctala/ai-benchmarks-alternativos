# GPT-OSS 20B (Groq) — agent_capabilities/model_as_router

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.71 | quality: 7.9
- latency_total: 1.037s | tokens_per_second: 716.1
- input_tokens: 320 | output_tokens: 743
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "devstral",
    "razon": "devstral es un modelo general rápido y competente para tareas de extracción y análisis de texto, ideal para identificar patrones y problemas en grandes volúmenes de reviews."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "claude-sonnet destaca en generar contenido empático y honesto, cualidades esenciales para redactar un mensaje de disculpa que reconozca el problema y mantenga la confianza del cliente."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "deepseek-v3 es excelente para razonamiento y coding, ofreciendo alta precisión y rapidez al generar scripts de procesamiento de datos."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "devstral",
    "razon": "devstral combina rapidez con capacidad creativa general, lo que lo hace adecuado para producir contenido atractivo y coherente para redes sociales."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "minimax-m2.7 es especialmente fuerte en tool‑calling y tareas de agente, lo que lo convierte en la opción ideal para verificar y validar un gran número de respuestas JSON."
  }
]
```