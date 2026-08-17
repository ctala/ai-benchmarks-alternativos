# Gemma 4 31B (DGX Spark Q4_K_M) — agent_capabilities/model_as_router

- model_id: `gemma4:31b`
- success: True  | final: 6.98 | quality: 8.52
- latency_total: 120.433s | tokens_per_second: 9.3
- input_tokens: 282 | output_tokens: 1125
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere una alta capacidad de razonamiento y síntesis de grandes volúmenes de datos, además de ser muy rentable para procesar mucha información."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Es el modelo especializado en contenido que requiere empatía, honestidad y un tono humano adecuado para la gestión de crisis."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Es el modelo más fuerte en coding y razonamiento lógico para estructurar scripts funcionales."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Es una tarea repetitiva y simple que requiere rapidez en la generación de contenido corto."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "gemini-flash-lite",
    "razon": "Es una tarea de validación técnica simple y volumétrica donde la velocidad de procesamiento (tok/s) es la prioridad."
  }
]
```