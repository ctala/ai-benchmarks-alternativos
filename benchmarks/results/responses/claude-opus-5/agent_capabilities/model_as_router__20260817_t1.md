# Claude Opus 5 — agent_capabilities/model_as_router

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.33 | quality: 7.5
- latency_total: 33.057s | tokens_per_second: 66.6
- input_tokens: 434 | output_tokens: 2201

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
    "razon": "Volumen alto de tokens + necesidad de razonamiento sintético (agrupar, priorizar, no solo resumir). A $0.14/M es el único que da buen razonamiento sin que 500 reviews duelan en costo. Recomiendo 2 etapas: gemini-flash-lite para etiquetar/categorizar cada review en paralelo, luego deepseek-v3 para consolidar los clusters en el top 5. Sale más barato y más preciso que meter todo en un solo contexto largo."
  },
  {
    "subtarea": "Email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Caso de uso exacto de su fortaleza: empatía + honestidad. En una disculpa el riesgo real no es la prosa, es el tono corporativo evasivo ('inconvenientes experimentados') o prometer cosas que no vas a cumplir. Es 1 output, el costo es irrelevante, y el daño de equivocarse es alto."
  },
  {
    "subtarea": "Script Python para procesar datos de ventas Q1",
    "modelo": "devstral",
    "razon": "Coding + rápido, y es una tarea acotada con verificación objetiva (corre o no corre). Si el schema es sucio o hay lógica de negocio no trivial (prorrateos, deduplicación, zonas horarias), cambia a deepseek-v3: su razonamiento maneja mejor los casos borde."
  },
  {
    "subtarea": "20 posts para redes sociales sobre el nuevo feature",
    "modelo": "claude-sonnet + gemini-flash-lite (híbrido)",
    "razon": "No lo trataría como tarea simple de volumen. Genera 3-4 posts con claude-sonnet para fijar la voz de marca y el ángulo del feature, luego usa esos como few-shot examples para que gemini-flash-lite produzca los 16 restantes a 200+ tok/s. Flash-lite solo, sin ejemplos, te da 20 posts genéricos e intercambiables."
  },
  {
    "subtarea": "Validar 100 respuestas JSON de la API",
    "modelo": "ninguno (código) — devstral para escribirlo",
    "razon": "Esta no es tarea de LLM. Validación de estructura JSON es determinista: usa jsonschema o pydantic. Un LLM te va a dar falsos negativos aleatorios, cuesta más y no es reproducible en CI. Usa devstral para generar el validador una vez y córrelo gratis para siempre."
  }
]
```

**Tres notas sobre las decisiones:**

1. **Tarea 5 es la más importante:** si "correctas" significa *estructura* (campos, tipos, nulls), es código, punto. Si significa *correctitud semántica* (¿el `total` coincide con la suma de `items`? ¿la respuesta tiene sentido dado el request?), sigue siendo código para las reglas verificables, y solo escalas a `deepseek-v3` los casos que el validador marca como ambiguos. Probablemente sean 5 de 100, no 100.

2. **No usé minimax-m2.7** porque ninguna de estas tareas es realmente agéntica — son transformaciones de una sola pasada. Donde sí encajaría: orquestar el pipeline completo (leer reviews de tu DB → llamar al clasificador → escribir resultados → disparar el validador), si quieres automatizar esto de forma recurrente en lugar de correrlo a mano.

3. **Dónde está tu costo real:** tarea 1 domina el gasto (~500 reviews × ~200 tokens = 100k tokens de input, más si iteras). Las otras cuatro juntas son ruido. Si vas a optimizar precio, optimiza esa; en las demás elige por calidad sin pensarlo mucho.