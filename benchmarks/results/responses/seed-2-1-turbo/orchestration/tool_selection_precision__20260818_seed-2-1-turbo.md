# Seed 2.1 Turbo — orchestration/tool_selection_precision

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 6.93 | quality: 7.5
- latency_total: 14.896s | tokens_per_second: 54.6
- input_tokens: 1249 | output_tokens: 813

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

### Asignación de herramientas por tarea:
1. **Tarea 1**: `http_request`  
   Es la herramienta diseñada para enviar solicitudes HTTP a endpoints web, lo que nos permite verificar el estado de respuesta del servidor de producción consultando su endpoint de salud.
2. **Tarea 2**: `query_database`  
   La información de usuarios activos suele almacenarse en bases de datos, y esta herramienta permite ejecutar consultas SQL para extraer métricas como el conteo de usuarios en un periodo determinado.
3. **Tarea 3**: `run_script`  
   Se trata de un cálculo matemático sencillo que se resuelve con un pequeño fragmento de código (por ejemplo, en Python), y esta herramienta permite ejecutar lógica programática para realizar operaciones de cálculo.
4. **Tarea 4**: `search_web`  
   Para encontrar artículos recientes sobre competidores es necesario buscar información actualizada en internet, por lo que la herramienta de búsqueda web es la adecuada.

---

### Ejecución de la Tarea 1:
