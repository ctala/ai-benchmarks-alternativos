# MiMo V2.6 Pro — agent_capabilities/model_as_router

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 5.09 | quality: 5.0
- latency_total: 57.472s | tokens_per_second: 37.9
- input_tokens: 290 | output_tokens: 2180

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
    "razon": "Requiere razonamiento profundo sobre un gran volumen de texto: agrupar, sintetizar y priorizar patrones. Es el mejor en razonamiento y además es muy barato, ideal para procesar 500 reviews sin disparar costos."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Comunicación de crisis que exige empatía, tono humano y honestidad (asumir la culpa sin excusas ni minimizar el impacto). Es la fortaleza central de Claude Sonnet."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Tarea de coding directa y bien definida; Devstral es rápido y muy bueno generando código, lo que entrega el script en poco tiempo y con buena calidad."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre el nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Generación creativa de alto volumen y baja complejidad por unidad. A 200+ tok/s produce los 20 posts en segundos y a costo mínimo, manteniendo consistencia de tono."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Es un pipeline agéntico iterativo: recorrer 100 respuestas, validar contra esquema con herramientas, marcar errores y opcionalmente re-consultar la API. Su fuerte en tool calling y orquestación de agentes lo hace ideal."
  }
]
```