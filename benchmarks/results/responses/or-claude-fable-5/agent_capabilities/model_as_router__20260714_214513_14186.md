# Claude Fable 5 — agent_capabilities/model_as_router

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 2.87 | quality: 2.5
- latency_total: 13.962s | tokens_per_second: 61.1
- input_tokens: 434 | output_tokens: 853
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando una asignación de modelos bien justificada para cada subtarea.

## Respuesta completa

```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere razonamiento profundo para identificar patrones y sintetizar problemas recurrentes en un volumen grande de texto. Su bajo costo ($0.14/M) es clave dado el alto volumen de tokens de entrada (500 reviews)."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Es una tarea de comunicación sensible que requiere empatía genuina, tono honesto y cuidado con la relación con el cliente. Es exactamente la fortaleza de este modelo."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Tarea de coding directa donde devstral destaca: es rápido, bueno en código y el mejor generalista. deepseek-v3 sería alternativa válida, pero devstral ofrece mejor velocidad para iterar sobre el script."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Generación de contenido corto y repetitivo que no requiere razonamiento complejo. Su velocidad ultra alta (200+ tok/s) permite generar los 20 posts casi instantáneamente y a bajo costo."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Tarea de validación estructurada y repetitiva ideal para un flujo agéntico: puede iterar sobre las 100 respuestas usando tool calling (validadores de schema, parsers) de forma confiable."
  }
]
```

**Resumen de la estrategia:** Priorizo costo en tareas de alto volumen de tokens (reviews → deepseek), velocidad en tareas simples y masivas (posts → gemini-flash-lite), empatía en comunicación delicada (email → claude), tooling en validación automatizada (JSON → minimax), y calidad de código con rapidez (script → devstral).