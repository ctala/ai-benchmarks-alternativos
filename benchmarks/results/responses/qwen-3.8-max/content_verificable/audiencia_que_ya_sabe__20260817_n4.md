# Qwen 3.8 Max — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 8.23 | quality: 10.0
- latency_total: 41.075s | tokens_per_second: 49.9
- input_tokens: 148 | output_tokens: 2050

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Un workflow puede terminar en success y no haber hecho nada porque n8n, por defecto, interpreta “terminó sin excepción” como éxito. Si un IF devuelve false, un Switch no coincide, un Filter elimina todos los ítems o un nodo opcional no se ejecuta, la ejecución sigue hasta el final con cero ítems útiles. Incluso un HTTP Request puede responder 200 con body vacío, o un webhook puede cerrar la respuesta antes del trabajo real. Si hay ramas paralelas y ninguna toca el sistema destino, el estado global sigue siendo verde.

El problema no es el estado: es la ausencia de señal. Para detectarlo, añade comprobaciones explícitas. Primero, cuenta ítems: usa un Set o Code después