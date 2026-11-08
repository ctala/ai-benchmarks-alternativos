# Nemotron 3 Ultra 550B — agent_capabilities/model_as_router

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.21 | quality: 7.5
- latency_total: 6.03s | tokens_per_second: 132.0
- input_tokens: 282 | output_tokens: 796

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

[{"subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales", "modelo": "deepseek-v3", "razon": "Mejor para razonamiento complejo a gran volumen; puede sintetizar patrones en 500 reviews barato y con alta calidad analítica"}, {"subtarea": "Escribir un email de disculpas a clientes afectados por un bug", "modelo": "claude-sonnet", "razon": "Superior en empatía, tono honesto y comunicación sensible; crítico para mantener confianza del cliente"}, {"subtarea": "Generar un script Python que procese los datos de ventas de Q1", "modelo": "devstral", "razon": "Mejor general para coding, rápido y confiable; ideal para scripts de procesamiento de datos limpios y funcionales"}, {"subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature", "modelo": "gemini-flash-lite", "razon": "Ultra rápido (200+ tok/s) y barato; perfecto para generar volumen alto de contenido simple y variado en segundos"}, {"subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas", "modelo": "minimax-m2.7", "razon": "Fuerte en tool calling y tareas de agente; puede iterar validaciones estructuradas contra schemas de forma automatizada"}]