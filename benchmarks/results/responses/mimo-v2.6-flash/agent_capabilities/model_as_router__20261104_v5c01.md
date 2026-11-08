# MiMo V2.6 Flash — agent_capabilities/model_as_router

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 7.26 | quality: 7.5
- latency_total: 21.602s | tokens_per_second: 32.0
- input_tokens: 290 | output_tokens: 692

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
  {"subtarea": "Analizar 500 reviews y extraer los 5 problemas principales", "modelo": "deepseek-v3", "razon": "Requiere razonamiento y síntesis de datos a gran volumen, y es la opción más barata ($0.14/M) para procesar mucho texto"},
  {"subtarea": "Escribir un email de disculpas a clientes afectados por un bug", "modelo": "claude-sonnet", "razon": "Tarea que requiere empatía, honestidad y tono cuidadoso; es justamente su mayor fortaleza"},
  {"subtarea": "Generar un script Python que procese datos de ventas de Q1", "modelo": "deepseek-v3", "razon": "Es el mejor en razonamiento y coding, ideal para lógica de procesamiento de datos"},
  {"subtarea": "Crear 20 posts para redes sociales sobre el nuevo feature", "modelo": "gemini-flash-lite", "razon": "Tarea simple y repetitiva que no requiere razonamiento complejo; su velocidad (200+ tok/s) y bajo costo la hacen perfecta para generar 20 piezas rápido"},
  {"subtarea": "Validar que 100 respuestas JSON de la API sean correctas", "modelo": "gemini-flash-lite", "razon": "Validación estructural simple y rápida; se beneficia de velocidad y bajo costo sin necesidad de razonamiento avanzado"}
]
```

**Resumen del reparto:**
- 🧠 **deepseek-v3** → tareas de razonamiento/coding (reviews y script Python) — la más barata para volumen
- 💛 **claude-sonnet** → comunicación sensible (email de disculpas)
- ⚡ **gemini-flash-lite** → tareas simples y en serie (posts y validación JSON)

Nota: si la validación JSON requiere hacer llamadas reales a la API de forma automatizada (tool calling), podrías considerar **minimax-m2.7** en su lugar.