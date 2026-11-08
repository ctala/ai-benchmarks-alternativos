# Ling 3.0 Flash — agent_capabilities/model_as_router

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 7.42 | quality: 7.5
- latency_total: 23.231s | tokens_per_second: 68.6
- input_tokens: 321 | output_tokens: 1594

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente router inteligente. Tu trabajo es decidir que modelo de IA usar para cada subtarea basado en sus fortalezas:

Modelos disponibles:
- deepseek-v3: Mejor para razonamiento y coding, muy barato ($0.14/M)
- gemini-flash-lite: Ultra rapido (200+ tok/s), bueno para tareas simples
- claude-sonnet: Mejor para contenido que requiere empatia y honestidad
- minimax-m2.7: Bueno para tool calling y agentes
- devstral: Mejor general, rapido, bueno para coding

Para cada subtarea, responde con un JSON array:
[{"subtarea": "...", "modelo": "...", "razon": "..."}]

**user:**

Tengo estas tareas para mi startup:
1. Analizar 500 reviews de usuarios y extraer los 5 problemas principales
2. Escribir un email de disculpas a clientes afectados por un bug
3. Generar un script Python que procese los datos de ventas de Q1
4. Crear 20 posts para redes sociales sobre nuestro nuevo feature
5. Validar que 100 respuestas JSON de nuestra API sean correctas

Asigna el mejor modelo para cada una.


## Respuesta completa

```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere razonamiento profundo para procesar un gran volumen de texto, identificar patrones y extraer conclusiones clave. DeepSeek-v3 destaca en razonamiento a un costo muy bajo ($0.14/M)."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Un email de disculpas requiere empatía, tono honesto y sensibilidad emocional para mantener la confianza del cliente. Claude Sonnet es el mejor modelo para contenido que necesita estos atributos."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Tarea de codificación que requiere generar código funcional y correcto. Devstral es rápido y muy bueno para coding, además de ser un modelo general versátil para este tipo de tareas técnicas."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre el nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Generación de contenido creativo pero relativamente simple (posts cortos). Gemini Flash Lite es ultra rápido (200+ tok/s), ideal para producir múltiples piezas de contenido de forma eficiente."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de la API sean correctas",
    "modelo": "gemini-flash-lite",
    "razon": "Tarea técnica sistemática y repetitiva que se beneficia enormemente de la velocidad de procesamiento. Validar estructuras JSON es una tarea simple donde la rapidez de Gemini Flash Lite permite revisar las 100 respuestas en tiempo récord."
  }
]
```