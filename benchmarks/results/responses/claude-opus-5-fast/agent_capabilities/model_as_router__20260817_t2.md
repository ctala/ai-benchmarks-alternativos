# Claude Opus 5 Fast — agent_capabilities/model_as_router

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 6.45 | quality: 7.5
- latency_total: 9.515s | tokens_per_second: 198.1
- input_tokens: 434 | output_tokens: 1885

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
    "razon": "Tarea de razonamiento agregado sobre alto volumen: requiere clusterizar quejas, deduplicar y priorizar por frecuencia/severidad, no solo resumir. deepseek-v3 tiene el mejor ratio razonamiento/precio ($0.14/M), clave cuando procesas ~500 textos. Sugerencia: map-reduce en lotes de 50 reviews (extracción de temas) + una pasada final de consolidación."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Caso claro de empatía + honestidad: hay que reconocer el fallo sin sobreprometer, sin lenguaje evasivo corporativo y sin minimizar el impacto al usuario. Es también el texto de mayor riesgo reputacional/legal del lote, así que justifica el modelo más caro para un solo output."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Coding de complejidad media (pandas, limpieza, agregaciones, export) donde importa la velocidad de iteración: escribir, correr, corregir. devstral es fuerte en código y rápido. Si el script crece a lógica de negocio compleja o edge cases financieros, escala a deepseek-v3 para la revisión."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Alto volumen, outputs cortos y formato repetitivo: es el caso ideal para 200+ tok/s y coste mínimo. Recomendación: genera 30-40 variantes con flash-lite y filtra manualmente las 20 mejores; sale más barato que generar 20 'perfectos' con un modelo caro."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Requiere ejecución estructurada y tool calling: invocar un validador de schema, parsear resultados y reportar qué campo falló en cada respuesta. minimax-m2.7 es el más fiable orquestando esas llamadas de forma consistente."
  }
]
```

**Notas de optimización:**

- **Tarea 5 — ojo con el over-engineering:** si solo validas contra un JSON Schema fijo, no necesitas LLM. Un script con `jsonschema` (10 líneas, generado por devstral en la tarea 3) es 100% determinista, gratis y más confiable. Usa minimax-m2.7 solo si la validación es semántica ("¿esta respuesta tiene sentido dado el request?").
- **Tarea 4 — riesgo de calidad:** flash-lite optimiza coste, no voz de marca. Si estos posts son el lanzamiento principal del feature, considera un paso de refinamiento con claude-sonnet sobre los 5 posts más visibles.
- **Orden sugerido:** ejecuta la tarea 1 primero. Los 5 problemas principales que salgan pueden alimentar el contenido del email (tarea 2) si el bug aparece entre las quejas recurrentes.
- **Coste estimado:** el grueso del gasto está en la tarea 1 por volumen de input; las tareas 2 y 3 son irrelevantes en coste aunque uses los modelos premium.