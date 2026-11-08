# GLM 5 — content_verificable/audiencia_que_ya_sabe

- model_id: `z-ai/glm-5`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 29.65s | tokens_per_second: 60.9
- input_tokens: 107 | output_tokens: 1806

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

¿Cuántas veces has mirado el panel de ejecuciones, visto el tick verde de "Success" y descubierto después que no pasó absolutamente nada? 

Es el falso positivo más frustrante de n8n. El workflow termina bien porque, técnicamente, no hubo errores de ejecución, pero tu lógica de negocio falló silenciosamente.

Esto suele ocurrir por tres motivos principales:

1. **Filtros que se tragan el payload:** Un nodo *Filter* o *IF* descarta el ítem y la ejecución simplemente termina. No hay error, solo vacío.
2. **Respuestas API engañosas:** Haces una petición y la API devuelve un `200 OK`, pero el cuerpo de la respuesta está vacío o no modificó ningún registro (un ID que no existe, pero la API es "amable" y no lanza un 400).
3. **Bucles vacíos:** Iteras sobre un array que llegó vacío. El *Split In Batches* no tiene nada que procesar, termina al instante y n8n lo marca como éxito.

**Cómo blindar tus workflows:**

Deja de confiar ciegamente en los códigos HTTP y empieza a validar la estructura del JSON. Justo después de un nodo crítico (una API o una query de BD), añade un nodo *Code* o *IF* que verifique si `$json` realmente tiene los datos esperados o si el array de resultados tiene `length > 0`.

Si la condición no se cumple, no dejes que el flujo termine. Fuerza un fallo real usando el nodo *Stop and Error* o lanzando un `throw new Error('Payload vacío después de X nodo')` en un *Code node*. 

Un workflow que falla ruidosamente es infinitamente mejor que uno que "triunfa" en silencio.