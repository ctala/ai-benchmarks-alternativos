# Mistral Large 3 675B — agent_capabilities/model_as_router

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 5.66 | quality: 5.0
- latency_total: 4.85s | tokens_per_second: 82.9
- input_tokens: 271 | output_tokens: 402

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
        "razon": "Requiere razonamiento para identificar patrones y sintetizar información de grandes volúmenes de texto. deepseek-v3 es eficiente y económico para esta tarea analítica."
    },
    {
        "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
        "modelo": "claude-sonnet",
        "razon": "Necesita empatía, honestidad y un tono adecuado para comunicar disculpas de manera efectiva. claude-sonnet es el mejor en contenido que requiere sensibilidad."
    },
    {
        "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
        "modelo": "devstral",
        "razon": "Es una tarea de coding que requiere precisión y rapidez. devstral es un modelo general fuerte en programación y rápido en ejecución."
    },
    {
        "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
        "modelo": "gemini-flash-lite",
        "razon": "Tarea repetitiva y simple que requiere velocidad para generar contenido breve y variado. gemini-flash-lite es ultra rápido y adecuado para esto."
    },
    {
        "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
        "modelo": "minimax-m2.7",
        "razon": "Requiere tool calling para interactuar con APIs o validar estructuras de datos de manera sistemática. minimax-m2.7 es el mejor para tareas con herramientas y agentes."
    }
]
```