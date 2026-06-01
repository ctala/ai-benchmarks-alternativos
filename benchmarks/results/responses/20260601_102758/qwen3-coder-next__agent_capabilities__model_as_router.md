# Qwen3-Coder-Next (OpenRouter FP8) — agent_capabilities/model_as_router

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 8.46 | quality: 9.76
- latency_total: 3.519s | tokens_per_second: 123.9
- input_tokens: 292 | output_tokens: 436
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una buena profundidad y utilidad práctica, proporcionando asignaciones de modelos bien justificadas para cada subtarea.

## Respuesta completa

```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere análisis cualitativo profundo y razonamiento sobre patrones en texto largo; deepseek-v3 es fuerte en análisis de texto y extracción de insights, y es económico para procesar grandes volúmenes."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Este contenido debe transmitir empatía, honestidad y profesionalismo; claude-sonnet destaca en generación de texto con tono humano y adecuado para comunicación sensible."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Es una tarea de codificación estándar, bien definida y repetible; devstral es rápido, preciso y económico para generación y validación de código."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Generación creativa de contenido corto y en serie; gemini-flash-lite es ultra rápido y eficiente para tareas repetitivas de escritura creativa sin requerir profundo razonamiento."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "deepseek-v3",
    "razon": "Validación estructurada de datos requiere lógica detallada y verificación sistemática; deepseek-v3 tiene sólida capacidad de razonamiento lógico y es ideal para tareas de verificación y debugging."
  }
]
```