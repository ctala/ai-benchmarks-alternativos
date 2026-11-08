# Kimi K2.7 Code — agent_capabilities/model_as_router

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 6.87 | quality: 7.5
- latency_total: 16.527s | tokens_per_second: 59.9
- input_tokens: 304 | output_tokens: 990

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
    "razon": "Requiere procesar gran volumen de texto, identificar patrones y hacer análisis de razonamiento para priorizar problemas reales. Además es muy económico, ideal para startups."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Necesita tono empático, honesto y cuidadoso para mantener la confianza del cliente en una situación sensible."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Es excelente para coding y razonamiento lógico, lo cual es clave para manipular datos de ventas correctamente."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre el nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Es ultra rápido y barato, perfecto para tareas repetitivas de generación de contenido simple en redes sociales."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de la API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Está diseñado para tool calling y agentes, lo que lo hace ideal para validaciones estructuradas y repetitivas como verificar JSON de una API."
  }
]
```