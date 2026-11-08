# Gemini 3.8 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 12.883s | tokens_per_second: 124.5
- input_tokens: 93 | output_tokens: 1604

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

El peor fallo en n8n no es un nodo en rojo; es un status `Success` en verde mientras tu cliente te pregunta por qué no se sincronizó su base de datos. 

Ese falso positivo suele ocurrir por tres razones:

1. **La muerte por array vacío (`[]`):** Un nodo de búsqueda, un *Filter* o un *Code* no encuentra coincidencias y escupe una lista vacía. Como n8n itera sobre los items entrantes, los nodos downstream simplemente no se ejecutan. Para el motor no hubo error: no había nada que procesar. Fin del flujo, verde impecable, cero acciones reales.
2. **APIs con código 200 mentiroso:** El nodo *HTTP Request* recibe un `200 OK`, pero el body contiene `{"success": false, "error": "rate_limit"}`. Si no parseas el payload, n8n asume éxito.
3. **Abuso de *Continue on Fail*:** Lo activas para evitar caídas críticas, pero si el nodo siguiente no valida si recibió data real o un objeto de error, el flujo sigue en piloto automático hacia la nada.

**Cómo detectarlo y evitarlo:**

* **Fuerza el fallo con *Stop and Error*:** Si una rama crítica recibe cero items, no dejes que muera en silencio. Mete un *If* (`{{ $input.all().length === 0 }}`) y manda el flujo a un nodo *Stop and Error* para que n8n registre el fallo y dispare tus alertas.
* **Valida payloads, no headers:** En llamadas HTTP críticas, añade aserciones inmediatas sobre campos clave (`id`, `status: 'created'`). 
* **Audita el nodo final:** Al monitorizar ejecuciones vía API o base de datos interna, no mires solo el status de la ejecución; verifica el `executionData` y cuenta cuántos items procesó tu nodo de destino. Cero escrituras es, por definición, un error.