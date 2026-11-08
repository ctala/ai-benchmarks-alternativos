# Muse Wonder — orchestration/tool_selection_precision

- model_id: `meta/muse-wonder`
- success: True  | final: 1.5 | quality: 0.0
- latency_total: 5.129s | tokens_per_second: 156.9
- input_tokens: 1330 | output_tokens: 805

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente orquestador. Elige SIEMPRE la herramienta mas apropiada.
No uses herramientas innecesarias. Si algo no requiere herramienta, no la uses.
Explica brevemente por que elegiste esa herramienta sobre las alternativas.

**user:**

Tengo que hacer estas 4 tareas. Para cada una, indica que herramienta usarias y por que. Luego ejecuta la tarea 1.

Tarea 1: Verificar si el servidor de produccion esta respondiendo (URL: https://api.example.com/health)
Tarea 2: Obtener el conteo de usuarios activos del ultimo mes
Tarea 3: Calcular el promedio de 3 numeros: 45, 67, 89
Tarea 4: Encontrar articulos recientes sobre competidores


## Respuesta completa

Evaluando cuatro tareas y seleccionando la herramienta de verificación HTTP para la tarea de salud del servidor.