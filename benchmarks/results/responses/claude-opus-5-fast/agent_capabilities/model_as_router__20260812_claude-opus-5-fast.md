# Claude Opus 5 Fast — agent_capabilities/model_as_router

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 6.36 | quality: 7.5
- latency_total: 11.379s | tokens_per_second: 180.0
- input_tokens: 434 | output_tokens: 2048

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
    "subtarea": "Analizar 500 reviews y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Volumen alto + síntesis analítica. A $0.14/M procesar 500 reviews cuesta centavos, y el razonamiento es suficientemente fuerte para agrupar quejas en categorías reales en vez de repetir literales.",
    "alternativa": "Pipeline en 2 etapas: gemini-flash-lite etiqueta cada review (barato/paralelo) → deepseek-v3 consolida los 500 labels. Más preciso y aún más barato."
  },
  {
    "subtarea": "Email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Es el caso claro de empatía + honestidad. Un modelo rápido tiende a producir disculpas corporativas vacías o a sobreprometer compensaciones que no autorizaste. Aquí el tono equivocado cuesta churn real."
  },
  {
    "subtarea": "Script Python para procesar datos de ventas Q1",
    "modelo": "devstral",
    "razon": "Coding puntual con requisitos claros: devstral da buena calidad y latencia baja. Si el script crece a algo con lógica de negocio compleja o edge cases de datos sucios, escala a deepseek-v3."
  },
  {
    "subtarea": "20 posts de redes sociales sobre el nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Generación de volumen con estructura repetitiva: velocidad y costo mandan.",
    "alternativa": "Recomendado: claude-sonnet escribe 3 posts de referencia definiendo voz de marca → gemini-flash-lite genera los 17 restantes imitando ese estilo. Sin ese anclaje, los 20 posts salen genéricos e intercambiables."
  },
  {
    "subtarea": "Validar 100 respuestas JSON de la API",
    "modelo": "minimax-m2.7",
    "razon": "Solo si la validación es semántica (¿el contenido tiene sentido para el request?), donde su tool calling permite orquestar checks. Para validación estructural NO uses LLM."
  }
]
```

**Dos observaciones honestas sobre esta lista:**

**La tarea 5 probablemente no necesita un LLM.** Si lo que quieres es verificar tipos, campos requeridos y formato, eso es `jsonschema` en 20 líneas de Python: determinista, gratis, 100% de recall y sin alucinaciones. Un LLM validando JSON te dará ~95% de acierto y fallará justo en los casos raros que te importan. Usa minimax-m2.7 solo para la capa semántica que un schema no puede cubrir — y aun así, después del validador estructural, no en lugar de él.

**La tarea 1 tiene un límite de contexto.** 500 reviews probablemente no entran en una sola llamada. El pipeline de 2 etapas no es una optimización de costo, es un requisito de arquitectura: sin él vas a truncar reviews silenciosamente y tus