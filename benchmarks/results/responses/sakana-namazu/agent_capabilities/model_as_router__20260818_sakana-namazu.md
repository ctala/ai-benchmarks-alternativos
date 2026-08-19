# Sakana Namazu — agent_capabilities/model_as_router

- model_id: `sakana/sakana-namazu`
- success: True  | final: 5.19 | quality: 5.0
- latency_total: 7.109s | tokens_per_second: 275.3
- input_tokens: 305 | output_tokens: 1957

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
    "razon": "Requiere razonamiento complejo para identificar patrones y categorizar problemas desde un volumen masivo de texto. Su costo extremadamente bajo ($0.14/M) lo hace ideal para procesar 500 reviews sin elevar el presupuesto."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Es la mejor opción para comunicación sensible donde se requiere empatía, tono honesto y calidez humana para reconstruir la confianza con los clientes afectados."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Está especializado en coding y razonamiento lógico. Además, su bajo costo permite iterar y refinar el script de procesamiento de datos sin preocupación por el precio de los tokens."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Tarea creativa repetitiva y estructurada donde prima la velocidad (200+ tok/s) para generar grandes volumenes de contenido simple en segundos, manteniendo bajos costos operativos."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Su fortaleza en tool calling y agentes permite integrar fácilmente validadores de schema JSON o ejecutar checks automatizados de forma estructurada y confiable sobre los 100 payloads."
  }
]
```