# Claude Opus 5 — agent_capabilities/model_as_router

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.35 | quality: 7.5
- latency_total: 31.166s | tokens_per_second: 65.7
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

## Asignación

```json
[
  {
    "subtarea": "Analizar 500 reviews y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere razonamiento agregativo (clasificar, agrupar, priorizar por frecuencia e impacto), no solo extracción. El precio bajo lo hace viable para 500 items. Sugerencia: pre-clasificar cada review con gemini-flash-lite (barato/rápido) y usar deepseek-v3 solo para la síntesis final sobre los clusters."
  },
  {
    "subtarea": "Email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Caso claro: tono empático sin sonar corporativo hueco, y honestidad sobre el alcance del fallo sin minimizarlo ni sobre-prometer. Es 1 sola generación, el costo es irrelevante aquí."
  },
  {
    "subtarea": "Script Python para procesar datos de ventas Q1",
    "modelo": "devstral",
    "razon": "Coding one-shot donde importa que el código corra bien a la primera (manejo de nulos, tipos, fechas). deepseek-v3 es alternativa válida si vas a iterar mucho y quieres bajar costo."
  },
  {
    "subtarea": "20 posts para redes sociales sobre el nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Volumen alto de texto corto y de bajo riesgo. Advertencia: solo con flash-lite los 20 posts van a sonar genéricos y repetitivos. Enfoque híbrido recomendado: claude-sonnet genera 3-4 posts que definan la voz de marca, y esos van como few-shot examples a flash-lite para escalar los 16 restantes."
  },
  {
    "subtarea": "Validar 100 respuestas JSON de la API",
    "modelo": "ninguno (código) o minimax-m2.7 si hay validación semántica",
    "razon": "Si es validación estructural (schema, tipos, campos requeridos), NO uses un LLM: jsonschema o pydantic te da 100% de precisión, determinismo y costo cero. Un LLM va a fallar silenciosamente en algunos casos. Solo si necesitas juicio semántico ('¿esta respuesta tiene sentido para este query?') usa minimax-m2.7 por su manejo de tool calling para orquestar las validaciones."
  }
]
```

## Notas sobre estas decisiones

**Dos aclaraciones de honestidad:**

1. Estas asignaciones se basan en las descripciones de fortalezas que me diste, no en benchmarks que yo haya verificado. En particular no tengo conocimiento propio de `minimax-m2.7` ni `devstral` con el detalle suficiente para confirmar que las descripciones sean exactas. Si estás construyendo un router de producción, vale la pena validar con evals sobre tus propios datos antes de fijar el mapeo.

2. La tarea 5 es la más importante de las cinco: es el caso donde meter un LLM te hace *daño* activo. La validación de estructura es un problema resuelto con código determinista. Un router bien diseñado debería tener una categoría "esto no necesita modelo".

**Sobre la tarea 1:** el patrón map-reduce (modelo barato para clasificar N items → modelo con razonamiento para sintetizar) es probablemente el que más costo te ahorra de todo el batch, y escala si pasas de 500 a 5000 reviews.

**Prioridad de revisión humana:** el email de disculpas (tarea 2). Es el único output que va directo a clientes en un momento de fricción, y donde un error de tono o una promesa implícita mal calibr