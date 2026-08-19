# Claude Sonnet 5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.37 | quality: 10.0
- latency_total: 20.022s | tokens_per_second: 66.0
- input_tokens: 159 | output_tokens: 1321

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**El "success" mentiroso**

Un workflow verde no significa que haya pasado algo. Significa que ninguna excepción rompió la ejecución. Son cosas distintas, y la diferencia te puede costar caro si el workflow en cuestión mueve leads, sincroniza inventario o dispara notificaciones.

Los culpables más comunes:

- **IF sin rama que capture el caso real.** El item no matchea ninguna condición, el workflow sigue por la rama "false" vacía y termina sin tocar nada.
- **Filtros que dejan pasar 0 items.** El nodo Filter no falla si no queda nada; simplemente no manda nada al siguiente paso, y el workflow completo termina en verde.
- **Continue On Fail activado "para no romper el flujo".** Es útil en nodos no críticos, pero si lo dejás en un nodo clave, el error se traga y el resto ejecuta sobre datos vacíos o nulos.
- **APIs que responden 200 con un array vacío.** No es un error HTTP, así que n8n no lo trata como tal.

La solución no es revisar logs a mano: es instrumentar el propio workflow. Agregá un nodo Code justo después de los puntos críticos (después de un Filter, un HTTP Request que consulta datos, un Switch) que valide `items.length` y tire un error explícito si es 0 cuando no debería serlo. Eso convierte un "no pasó nada" silencioso en un fallo real que tu Error Workflow puede capturar.

Otra capa útil: métricas de ausencia. No solo alertar cuando algo falla, sino cuando algo *no ocurrió* en la ventana de tiempo esperada (ej: "0 leads procesados en las últimas 3 horas" con actividad normal debería ser 20+).

El success del workflow es una señal técnica, no de negocio. Tratalo así.