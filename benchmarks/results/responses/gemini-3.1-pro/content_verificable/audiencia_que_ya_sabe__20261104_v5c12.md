# Gemini 3.1 Pro — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 26.29s | tokens_per_second: 66.3
- input_tokens: 93 | output_tokens: 1743

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Todos conocemos la frustración: el log de ejecuciones está lleno de etiquetas verdes de "Success", pero cuando revisas la base de datos, no hay cambios. Tu workflow te está mintiendo.

¿Por qué un workflow de n8n termina en *success* sin haber hecho absolutamente nada?

Casi siempre se reduce a la arquitectura basada en *items*. Si un nodo de búsqueda o un HTTP Request devuelve un array vacío (`[]`), los nodos subsecuentes simplemente no se ejecutan. El motor de n8n asume que el trabajo terminó. No hay error, por lo tanto, es un "éxito" silencioso. Otra causa típica es habilitar *Continue On Fail* en los settings de un nodo y olvidar manejar ese escenario en el siguiente paso.

Para detectar y evitar estos falsos positivos, necesitas construir a la defensiva:

**1. Usa *Always Output Data*:** En nodos propensos a no encontrar resultados, activa esta opción en la configuración del nodo. Esto fuerza la salida de un item vacío (sin propiedades), lo que te permite usar un nodo IF inmediatamente después para validar si llegaron los datos (ej. revisando si `{{ $json.id }}` existe).

**2. Valida la longitud del input:** Antes de operaciones críticas (mutaciones en APIs, envíos de emails), usa un IF para comprobar `{{ $input.all().length > 0 }}`. Si es falso, enrrútalo a tu canal de alertas de Slack o Discord.

**3. Audita tus *Continue On Fail*:** Si permites que un nodo falle para no detener la ejecución, el nodo adyacente *debe* revisar obligatoriamente si existe la propiedad de error en el output.

Un workflow robusto no es el que nunca falla; es el que nunca miente.