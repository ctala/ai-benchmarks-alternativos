# Claude Opus 5.5 — agent_capabilities/model_as_router

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.61 | quality: 7.5
- latency_total: 13.981s | tokens_per_second: 102.0
- input_tokens: 436 | output_tokens: 1426

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
    "razon": "Agrupar quejas similares, detectar patrones y priorizar por frecuencia e impacto requiere razonamiento. Con 500 reviews el volumen de tokens es alto, y su precio de $0.14/M lo hace muy rentable."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "El email debe reconocer el problema con honestidad, sin minimizarlo ni sonar corporativo, y transmitir empatía real. Un mal tono aquí puede dañar la confianza del cliente."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Está especializado en coding y es rápido, ideal para un script de procesamiento de datos con pandas, limpieza y agregaciones. deepseek-v3 sería una alternativa igual de válida y más barata si el script es complejo."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre el nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Es contenido corto y repetitivo en volumen, donde su velocidad de más de 200 tok/s permite iterar rápido y generar variaciones."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de la API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Su fuerza en tool calling permite orquestar un validador real, como jsonschema o pydantic, en lugar de validar 'a ojo' con el LLM. Puede ejecutar la herramienta sobre las 100 respuestas y reportar los errores."
  }
]
```

**Notas adicionales:**
- **Tarea 5:** validar JSON es un problema determinista. Lo más fiable y barato es un script con un JSON Schema. Usa el LLM solo para orquestar o para generar el schema, no para "leer" y aprobar cada respuesta, porque puede pasar por alto errores sutiles.
- **Tarea 4:** si los posts necesitan una voz de marca muy cuidada, conviene que claude-sonnet o un humano revise la selección final.
- **Flujo sugerido:** el output de la tarea 1 (problemas principales) puede alimentar la tarea 2 si el bug está relacionado con las quejas detectadas.