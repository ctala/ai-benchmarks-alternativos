# Gemini 3.5 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-3.5-flash`
- success: True  | final: 8.85 | quality: 10.0
- latency_total: 4.788s | tokens_per_second: 81.7
- input_tokens: 93 | output_tokens: 391
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

**¿Tu workflow ha terminado en `success` pero no ha hecho absolutamente nada?**

Seguro que te ha pasado. El historial de ejecuciones de n8n muestra un check verde impecable, pero el cliente te escribe diciendo que los datos no han llegado. Entras al *execution plan* y ahí está el culpable: un nodo intermedio devolvió un array vacío (`[]`) y detuvo silenciosamente la ejecución sin levantar un solo error.

En n8n, **un resultado vacío no es un fallo para el motor de ejecución**. Si un nodo de búsqueda (como un *Search Rows* de Google Sheets o un *Find* de Airtable) no encuentra coincidencias, simplemente pasa 0 elementos al siguiente nodo. Para n8n, el flujo ha terminado con éxito porque no hubo un error de conexión o de sintaxis.

### Cómo evitar estos «falsos positivos»

Para mantener tus flujos bajo control y evitar que las ejecuciones vacías pasen desapercibidas, implementa estas dos estrategias:

1. **El nodo *If* como interruptor:** Justo después de cualquier nodo de búsqueda o filtrado, añade un nodo *If*. Configura la condición para verificar la longitud del array de entrada (`{{ $json.length }}` o validando si un ID existe). Si es falso (vacío), desvía el flujo.
2. **Alertas proactivas en la rama vacía:** No dejes que la rama del «No» muera en el olvido. Conéctala a un nodo de Slack, Teams o Email. Configura un mensaje del tipo: *"Búsqueda completada sin resultados para el cliente X"*. 

De esta forma, sabrás de inmediato si la falta de actividad es un comportamiento esperado o un problema de datos que requiere tu atención, antes de que tu cliente se dé cuenta.