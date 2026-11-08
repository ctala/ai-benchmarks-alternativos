# Gemini 4 Argon — agent_capabilities/model_as_router

- model_id: `google/gemini-4-argon`
- success: True  | final: 6.67 | quality: 7.5
- latency_total: 11.936s | tokens_per_second: 35.2
- input_tokens: 290 | output_tokens: 420

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
    "subtarea": "1. Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Procesar 500 reviews requiere una gran cantidad de tokens de entrada y capacidad de razonamiento para sintetizar patrones. Su costo ultra bajo ($0.14/M) y fuerte capacidad analítica lo hacen ideal."
  },
  {
    "subtarea": "2. Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Un correo de disculpas es crítico para la retención de clientes y requiere un tono altamente empático, humano y honesto, que es la principal fortaleza de este modelo."
  },
  {
    "subtarea": "3. Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Es el mejor modelo disponible para programación y lógica de procesamiento de datos, además de ser el más económico."
  },
  {
    "subtarea": "4. Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "devstral",
    "razon": "Al ser el mejor modelo de propósito general y rápido, es excelente para generar contenido creativo variado y atractivo en volumen."
  },
  {
    "subtarea": "5. Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "gemini-flash-lite",
    "razon": "La validación de estructura o sintaxis JSON es una tarea simple y repetitiva. La velocidad ultra rápida (200+ tok/s) de este modelo permitirá validar las 100 respuestas casi instantáneamente."
  }
]
```